<template>
  <div class="custom-map" :class="{ open: isOpen }">
    <button class="map-toggle" type="button" @click="toggleMap" aria-label="Open slide map">
      <span class="map-label">MAP</span>
      <span class="map-arrow">{{ isOpen ? '▴' : '▾' }}</span>
    </button>

    <div v-if="isOpen" class="map-panel" role="navigation" aria-label="Slide map">
      <a
        v-for="slide in slides"
        :key="slide.n"
        class="map-item"
        :class="{ active: currentSlide === slide.n }"
        :href="`/${slide.n}`"
      >
        <span class="num">{{ slide.n }}</span>
        <span class="title">{{ slide.t }}</span>
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const currentSlide = Number((globalThis.location?.pathname || '/1').replace('/', '')) || 1
const isOpen = ref(true)

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

function toggleMap() {
  isOpen.value = !isOpen.value
}
</script>

<style scoped>
.custom-map {
  position: fixed;
  top: 12px;
  right: 14px;
  z-index: 90;
  width: 340px;
}

.map-toggle {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 10px;
  border: 1px solid rgba(116, 239, 231, 0.45);
  background: rgba(6, 16, 16, 0.86);
  color: #a9fff8;
  padding: 0.35rem 0.75rem;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  font-weight: 800;
}

.map-panel {
  margin-top: 0.32rem;
  border-radius: 12px;
  border: 1px solid rgba(116, 239, 231, 0.34);
  background: rgba(6, 16, 16, 0.93);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.42);
  max-height: calc(100vh - 82px);
  overflow: auto;
}

.map-item {
  display: grid;
  grid-template-columns: 2.1rem 1fr;
  gap: 0.5rem;
  align-items: start;
  text-decoration: none;
  color: rgba(224, 248, 246, 0.9);
  padding: 0.34rem 0.56rem;
  border-bottom: 1px solid rgba(116, 239, 231, 0.1);
  font-size: 0.73rem;
}

.map-item:last-child {
  border-bottom: none;
}

.map-item .num {
  opacity: 0.68;
  text-align: right;
}

.map-item.active {
  background: rgba(78, 205, 196, 0.16);
  color: #ffffff;
}

.map-item:hover {
  background: rgba(78, 205, 196, 0.1);
}

.map-arrow {
  font-size: 0.75rem;
}

@media (max-width: 900px) {
  .custom-map {
    width: min(92vw, 340px);
    right: 8px;
    top: 8px;
  }
}
</style>
