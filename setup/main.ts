import { defineAppSetup } from '@slidev/types'

const slides = [
  { n: 1, t: 'El Puente que Falta' },
  { n: 2, t: 'Hamer Quote' },
  { n: 3, t: 'Problema de la Medicina Moderna' },
  { n: 4, t: 'Salud Fisica en Peru' },
  { n: 5, t: 'Salud Mental en Peru' },
  { n: 6, t: 'Problema Central' },
  { n: 7, t: 'Implicacion 1: Costo Clinico' },
  { n: 8, t: 'Paciente como Sistema' },
  { n: 9, t: 'La Ciencia que lo Sustenta' },
  { n: 10, t: 'Ciencia Visual' },
  { n: 11, t: 'Tres Fundamentos Cientificos' },
  { n: 12, t: 'Historia de Hamer' },
  { n: 13, t: 'Decision de Modelo' },
  { n: 14, t: 'Criterio de Solucion' },
  { n: 15, t: 'La Propuesta' },
  { n: 16, t: 'Modelo de Atencion' },
  { n: 17, t: 'Los Tres Pilares' },
  { n: 18, t: 'Tres Pilares' },
  { n: 19, t: 'Pilar 1: Biologia del Conflicto' },
  { n: 20, t: 'Pilar 2: Terapias Sistemicas' },
  { n: 21, t: 'Pilar 3: Medicina Funcional' },
  { n: 22, t: 'Objetivos Medibles' },
  { n: 23, t: 'Impacto Esperado' },
  { n: 24, t: 'El Nombre del Departamento' },
  { n: 25, t: 'Opciones de Nombre' },
  { n: 26, t: 'Perfil de la Directora' },
  { n: 27, t: 'Plan de Implementacion' },
  { n: 28, t: 'Fase 1' },
  { n: 29, t: 'Fase 2' },
  { n: 30, t: 'Fase 3' },
  { n: 31, t: 'Implementacion' },
  { n: 32, t: 'Inversion' },
  { n: 33, t: 'Evidencia Internacional' },
  { n: 34, t: 'Vision de Futuro' },
  { n: 35, t: 'Cierre' },
]

function currentSlideNumber(pathname: string) {
  const n = Number(pathname.replace('/', ''))
  return Number.isFinite(n) && n > 0 ? n : 1
}

function slideHref(slideNumber: number) {
  return `/${slideNumber}${window.location.search || ''}`
}

function ensureMobileZoomEnabled() {
  const existing = document.querySelector('meta[name="viewport"]') as HTMLMetaElement | null
  const content = 'width=device-width, initial-scale=1, maximum-scale=5, user-scalable=yes'

  if (existing) {
    if (existing.content !== content) existing.content = content
    return
  }

  const meta = document.createElement('meta')
  meta.name = 'viewport'
  meta.content = content
  document.head.appendChild(meta)
}

function bindPinchZoomFallback() {
  const w = window as any
  if (w.__slidevPinchZoomBound) return
  w.__slidevPinchZoomBound = true

  if (window.matchMedia('(min-width: 901px)').matches) return

  let currentScale = 1
  let currentTx = 0
  let currentTy = 0

  let pinchStartDistance = 0
  let pinchStartScale = 1
  let pinchStartTx = 0
  let pinchStartTy = 0
  let pinchStartCenterX = 0
  let pinchStartCenterY = 0

  let panStartX = 0
  let panStartY = 0
  let panStartTx = 0
  let panStartTy = 0
  let isPanning = false

  const clamp = (value: number, min: number, max: number) => Math.min(max, Math.max(min, value))
  const distance = (a: Touch, b: Touch) => Math.hypot(b.clientX - a.clientX, b.clientY - a.clientY)
  const center = (a: Touch, b: Touch) => ({ x: (a.clientX + b.clientX) / 2, y: (a.clientY + b.clientY) / 2 })

  const getTarget = () =>
    (document.querySelector('.slidev-slide-content') ||
      document.querySelector('.slidev-layout') ||
      document.querySelector('#app')) as HTMLElement | null

  const getBaseSize = (target: HTMLElement) => {
    if (!target.dataset.baseWidth || !target.dataset.baseHeight) {
      target.dataset.baseWidth = String(target.offsetWidth)
      target.dataset.baseHeight = String(target.offsetHeight)
    }
    return {
      width: Number(target.dataset.baseWidth) || target.offsetWidth,
      height: Number(target.dataset.baseHeight) || target.offsetHeight,
    }
  }

  const limitPan = (target: HTMLElement, scale: number, tx: number, ty: number) => {
    const base = getBaseSize(target)
    const maxX = Math.max(0, ((base.width * scale) - base.width) / 2)
    const maxY = Math.max(0, ((base.height * scale) - base.height) / 2)
    return {
      tx: clamp(tx, -maxX, maxX),
      ty: clamp(ty, -maxY, maxY),
    }
  }

  const applyScale = () => {
    const target = getTarget()
    if (!target) return
    if (currentScale <= 1.001) {
      currentScale = 1
      currentTx = 0
      currentTy = 0
      target.style.transformOrigin = 'center center'
      target.style.transform = 'translate(0px, 0px) scale(1)'
      return
    }

    const bounded = limitPan(target, currentScale, currentTx, currentTy)
    currentTx = bounded.tx
    currentTy = bounded.ty

    target.style.transformOrigin = 'center center'
    target.style.transform = `translate(${currentTx}px, ${currentTy}px) scale(${currentScale})`
  }

  const inCustomMapPanel = (target: EventTarget | null) => {
    const panel = document.getElementById('custom-map-panel')
    return !!(panel && target instanceof Node && panel.contains(target))
  }

  document.addEventListener(
    'touchstart',
    (ev) => {
      if (inCustomMapPanel(ev.target)) return

      if (ev.touches.length === 2) {
        pinchStartDistance = distance(ev.touches[0], ev.touches[1])
        pinchStartScale = currentScale
        pinchStartTx = currentTx
        pinchStartTy = currentTy
        const c = center(ev.touches[0], ev.touches[1])
        pinchStartCenterX = c.x
        pinchStartCenterY = c.y
        isPanning = false
        return
      }

      if (ev.touches.length === 1 && currentScale > 1.001) {
        panStartX = ev.touches[0].clientX
        panStartY = ev.touches[0].clientY
        panStartTx = currentTx
        panStartTy = currentTy
        isPanning = true
      }
    },
    { passive: true }
  )

  document.addEventListener(
    'touchmove',
    (ev) => {
      if (inCustomMapPanel(ev.target)) return

      if (ev.touches.length === 2) {
        ev.preventDefault()
        const d = distance(ev.touches[0], ev.touches[1])
        if (!pinchStartDistance) pinchStartDistance = d
        const factor = d / pinchStartDistance
        currentScale = clamp(pinchStartScale * factor, 1, 2.5)

        const c = center(ev.touches[0], ev.touches[1])
        currentTx = pinchStartTx + (c.x - pinchStartCenterX)
        currentTy = pinchStartTy + (c.y - pinchStartCenterY)
        applyScale()
        return
      }

      if (ev.touches.length === 1 && isPanning && currentScale > 1.001) {
        ev.preventDefault()
        currentTx = panStartTx + (ev.touches[0].clientX - panStartX)
        currentTy = panStartTy + (ev.touches[0].clientY - panStartY)
        applyScale()
      }
    },
    { passive: false }
  )

  document.addEventListener(
    'touchend',
    (ev) => {
      if (ev.touches.length === 0) {
        pinchStartDistance = 0
        isPanning = false
      }

      if (ev.touches.length === 1 && currentScale > 1.001) {
        panStartX = ev.touches[0].clientX
        panStartY = ev.touches[0].clientY
        panStartTx = currentTx
        panStartTy = currentTy
        isPanning = true
      }

      if (currentScale < 1.01) {
        applyScale()
      }
    },
    { passive: true }
  )

  document.addEventListener(
    'touchcancel',
    () => {
      pinchStartDistance = 0
      isPanning = false
    },
    { passive: true }
  )
}

function mountMapPanel() {
  if (typeof document === 'undefined') return

  ensureMobileZoomEnabled()
  bindPinchZoomFallback()
  document.body.classList.add('custom-map-active')

  let root = document.getElementById('custom-map-panel')
  if (!root) {
    root = document.createElement('div')
    root.id = 'custom-map-panel'
    document.body.appendChild(root)
  }

  const current = currentSlideNumber(window.location.pathname)
  const prev = current > 1 ? current - 1 : null
  const next = current < slides.length ? current + 1 : null
  const items = slides
    .map((s) => {
      const active = s.n === current ? ' map-item-active' : ''
      return `<a class="map-item${active}" href="/${s.n}"><span class="num">${s.n}</span><span class="title">${s.t}</span></a>`
    })
    .join('')

  root.innerHTML = `
    <button class="map-toggle" type="button" aria-label="Toggle map">MAP <span class="arrow">▾</span></button>
    <div class="map-nav">
      ${prev ? `<a class="map-nav-btn map-nav-prev" href="${slideHref(prev)}" aria-label="Go to previous slide">↑</a>` : `<span class="map-nav-btn map-nav-prev map-nav-disabled" aria-hidden="true">↑</span>`}
      ${next ? `<a class="map-nav-btn map-nav-next" href="${slideHref(next)}" aria-label="Go to next slide">↓</a>` : `<span class="map-nav-btn map-nav-next map-nav-disabled" aria-hidden="true">↓</span>`}
    </div>
    <div class="map-panel">${items}</div>
  `

  const toggle = root.querySelector('.map-toggle') as HTMLButtonElement | null
  const panel = root.querySelector('.map-panel') as HTMLDivElement | null
  if (toggle && panel) {
    toggle.onclick = () => {
      const open = root?.classList.toggle('open')
      const arrow = root?.querySelector('.arrow')
      if (arrow) arrow.textContent = open ? '▴' : '▾'
    }
  }

  if (!document.getElementById('custom-map-style')) {
    const style = document.createElement('style')
    style.id = 'custom-map-style'
    style.textContent = `
      html, body, #app, #slidev-root,
      .slidev-layout, .slidev-page, .slidev-slide-container, .slidev-slide-content {
        touch-action: pan-x pan-y pinch-zoom !important;
      }
      body.custom-map-active nav .slidev-icon-btn[title="Go to previous slide"],
      body.custom-map-active nav .slidev-icon-btn[title="Go to next slide"] {
        display: none !important;
      }
      #custom-map-panel { position: fixed; top: 12px; right: 14px; width: 64px; z-index: 95; transition: width .22s ease; }
      #custom-map-panel:hover, #custom-map-panel:focus-within, #custom-map-panel.open { width: 340px; }
      #custom-map-panel .map-toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; border-radius: 10px; border: 1px solid rgba(116,239,231,.45); background: rgba(6,16,16,.86); color: #a9fff8; padding: .35rem .75rem; font-size: .68rem; letter-spacing: .14em; font-weight: 800; overflow: hidden; }
      #custom-map-panel:not(:hover):not(:focus-within):not(.open) .map-toggle { justify-content: center; padding-inline: .35rem; }
      #custom-map-panel:not(:hover):not(:focus-within):not(.open) .map-toggle .arrow { display: none; }
      #custom-map-panel .map-panel { display: none; margin-top: .32rem; border-radius: 12px; border: 1px solid rgba(116,239,231,.34); background: rgba(6,16,16,.93); box-shadow: 0 10px 30px rgba(0,0,0,.42); max-height: calc(100vh - 82px); overflow: auto; }
      #custom-map-panel:hover .map-panel, #custom-map-panel:focus-within .map-panel, #custom-map-panel.open .map-panel { display: block; }
      #custom-map-panel .map-nav { position: fixed; right: 14px; top: calc(50% - 3.9rem); z-index: 96; display: flex; flex-direction: column; gap: .72rem; }
      #custom-map-panel .map-nav-btn { width: 3.2rem; height: 3.2rem; display: inline-flex; align-items: center; justify-content: center; border-radius: 999px; border: 1px solid rgba(122,240,232,.55); background: rgba(4,14,14,.84); color: #eafdfc; text-decoration: none; font-size: 1.45rem; line-height: 1; box-shadow: 0 10px 26px rgba(0,0,0,.45); outline: none; }
      #custom-map-panel .map-nav-btn:hover { transform: scale(1.06); background: rgba(18,52,50,.96); border-color: rgba(122,240,232,.9); }
      #custom-map-panel .map-nav-btn:focus-visible { box-shadow: 0 0 0 2px rgba(122,240,232,.55), 0 10px 26px rgba(0,0,0,.45); }
      #custom-map-panel .map-nav-disabled { opacity: .35; pointer-events: none; }
      #custom-map-panel .map-item { display: grid; grid-template-columns: 2.1rem 1fr; gap: .5rem; align-items: start; text-decoration: none; color: rgba(224,248,246,.9); padding: .34rem .56rem; border-bottom: 1px solid rgba(116,239,231,.1); font-size: .73rem; }
      #custom-map-panel .map-item:last-child { border-bottom: none; }
      #custom-map-panel .map-item .num { opacity: .68; text-align: right; }
      #custom-map-panel .map-item:hover { background: rgba(78,205,196,.1); }
      #custom-map-panel .map-item-active { background: rgba(78,205,196,.16); color: #fff; }
      @media (max-width: 900px) {
        #custom-map-panel { width: min(92vw, 340px); right: 8px; top: 8px; }
        #custom-map-panel:hover, #custom-map-panel:focus-within, #custom-map-panel.open { width: min(92vw, 340px); }
        #custom-map-panel .map-panel { display: none !important; }
        #custom-map-panel.open .map-panel { display: block !important; }
        #custom-map-panel .map-nav { right: 8px; }
      }
    `
    document.head.appendChild(style)
  }
}

export default defineAppSetup(({ router }) => {
  if (typeof window === 'undefined') return

  const remount = () => {
    window.requestAnimationFrame(() => mountMapPanel())
  }

  remount()
  router.afterEach(() => remount())
})
