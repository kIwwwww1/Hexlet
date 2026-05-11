<template>
  <button :class="['icon-button', colorClass]">
    <!-- Слот для иконки, чтобы можно было вставить любую -->
    <slot></slot>
  </button>
</template>

<script setup>
defineProps({
  colorClass: {
    type: String,
    default: 'blue' // по умолчанию синяя
  }
})
</script>

<style scoped>
.icon-button {
  width: 50px;
  height: 50px;
  border: none;
  border-radius: 12px; /* как на макете */
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.1s, opacity 0.2s;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.icon-button:active {
  transform: scale(0.95);
}

/* Классы цветов */
.blue { background-color: var(--color-blue); color: white; }
.green { background-color: var(--color-green); color: white; }
.orange { background-color: var(--color-orange); color: white; }
</style>
