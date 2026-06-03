<template>
  <a
    class="cloud-edit-link"
    href="https://github.com/adolfosalasgomez3011/ximena-sisol-proposal-v2/edit/v2/slides.md"
    target="_blank"
    rel="noopener noreferrer"
  >
    Editar deck
  </a>
</template>

<style scoped>
.cloud-edit-link {
  position: fixed;
  top: 14px;
  left: 14px;
  z-index: 80;
  padding: 0.4rem 0.7rem;
  border-radius: 999px;
  border: 1px solid rgba(105, 227, 219, 0.55);
  background: rgba(2, 12, 12, 0.72);
  color: #d8f9f6;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  text-decoration: none;
  backdrop-filter: blur(10px);
}

.cloud-edit-link:hover {
  background: rgba(8, 30, 30, 0.88);
  border-color: rgba(105, 227, 219, 0.85);
  color: #ffffff;
}
</style>