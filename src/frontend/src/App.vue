<script setup>
import { ref } from 'vue'

const message = ref('Привет, Vue 3!')
</script>

<template>
  <div class="app-container">
    <h1>{{ message }}</h1>
    <MyComponent />
    <button class="info-button">
            <img src="@/assets/images/question-solid.png" alt="info">
    </button>
</div>
</template>

<style scoped>
.app-container {
  font-family: sans-serif;
  text-align: center;
}
</style>
