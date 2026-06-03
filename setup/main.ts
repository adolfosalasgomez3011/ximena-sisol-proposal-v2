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

function mountMapPanel() {
  if (typeof document === 'undefined') return

  let root = document.getElementById('custom-map-panel')
  if (!root) {
    root = document.createElement('div')
    root.id = 'custom-map-panel'
    document.body.appendChild(root)
  }

  const current = currentSlideNumber(window.location.pathname)
  const items = slides
    .map((s) => {
      const active = s.n === current ? ' map-item-active' : ''
      return `<a class="map-item${active}" href="/${s.n}"><span class="num">${s.n}</span><span class="title">${s.t}</span></a>`
    })
    .join('')

  root.innerHTML = `
    <button class="map-toggle" type="button" aria-label="Toggle map">MAP <span class="arrow">▾</span></button>
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

  root.classList.add('open')

  if (!document.getElementById('custom-map-style')) {
    const style = document.createElement('style')
    style.id = 'custom-map-style'
    style.textContent = `
      #custom-map-panel { position: fixed; top: 12px; right: 14px; width: 340px; z-index: 95; }
      #custom-map-panel .map-toggle { width: 100%; display: flex; align-items: center; justify-content: space-between; border-radius: 10px; border: 1px solid rgba(116,239,231,.45); background: rgba(6,16,16,.86); color: #a9fff8; padding: .35rem .75rem; font-size: .68rem; letter-spacing: .14em; font-weight: 800; }
      #custom-map-panel .map-panel { display: none; margin-top: .32rem; border-radius: 12px; border: 1px solid rgba(116,239,231,.34); background: rgba(6,16,16,.93); box-shadow: 0 10px 30px rgba(0,0,0,.42); max-height: calc(100vh - 82px); overflow: auto; }
      #custom-map-panel.open .map-panel { display: block; }
      #custom-map-panel .map-item { display: grid; grid-template-columns: 2.1rem 1fr; gap: .5rem; align-items: start; text-decoration: none; color: rgba(224,248,246,.9); padding: .34rem .56rem; border-bottom: 1px solid rgba(116,239,231,.1); font-size: .73rem; }
      #custom-map-panel .map-item:last-child { border-bottom: none; }
      #custom-map-panel .map-item .num { opacity: .68; text-align: right; }
      #custom-map-panel .map-item:hover { background: rgba(78,205,196,.1); }
      #custom-map-panel .map-item-active { background: rgba(78,205,196,.16); color: #fff; }
      @media (max-width: 900px) { #custom-map-panel { width: min(92vw, 340px); right: 8px; top: 8px; } }
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
