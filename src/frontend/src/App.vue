<script setup>
import { ref } from 'vue'

const userEnergy = ref(0)
const userId = ref('Загрузка...')

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
    <div class="button-container right">

      <!-- Первая пара (Яблоко) -->
      <div class="status-item">
        <img src="@/assets/images/apple-whole-solid.png" class="status-icon" alt="apple">
        <div class="button-text-wrapper"><span>{{ userEnergy }}</span></div>
      </div>

      <!-- Вторая пара (ID) -->
      <div class="status-item">
        <img src="@/assets/images/id-card-solid.png" class="status-icon" alt="id-card">
        <div class="button-text-wrapper"><span>{{ userId }}</span></div>
      </div>
    </div>




  </div>
</template>


<style scoped>
.app-container {
  font-family: sans-serif;
  text-align: center;
}
</style>
