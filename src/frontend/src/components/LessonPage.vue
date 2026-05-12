<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

const currentPath = computed(() => route.path)

const fullPath = computed(() => route.fullPath)

const lessonId = computed(() => route.params.id)

console.log(currentPath.value)
</script>

<template>
  <div>
    <h1>Текущий путь: {{ currentPath }}</h1>
    <p>ID урока: {{ lessonId }}</p>
  </div>
</template>

<style scoped>
</style>
