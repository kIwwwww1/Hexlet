<script setup>
import { ref } from 'vue'

const message = ref('Привет, Vue 3!')
</script>

<template>
  <div class="app-container">
    <h1>{{ message }}</h1>

    <div class="button-container left">
      <button class="main-button">
        <img src="@/assets/images/question-solid.png" draggable="false" alt="info">
      </button>

      <button class="main-button skip">
        <img src="@/assets/images/forward-solid.png" draggable="false" alt="add">
      </button>
    </div>

    <div class="button-container center">
      <button class="main-button home">
        <img src="@/assets/images/house-solid.png" draggable="false" alt="settings">
      </button>
    </div>
  </div>
</template>


<style scoped>
.app-container {
  font-family: sans-serif;
  text-align: center;
}
</style>
