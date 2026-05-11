<script setup>
import { ref } from 'vue'

const userEnergy = ref(0)
const userId = ref('Загрузка...')

</script>

<template>
  <div class="app-container">

    <div class="button-container left">

      <div class="button-container top-center">
        <button class="main-button exit">
          <img src="@/assets/images/door-open-solid.png" draggable="false" alt="exit">
        </button>
      </div>


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
        <img src="@/assets/images/apple-whole-solid.png" draggable="false" class="status-icon" alt="apple">
        <div class="button-text-wrapper"><span>{{ userEnergy }}</span></div>
      </div>
      
      <!-- Вторая пара (ID) -->
      <div class="status-item">
        <img src="@/assets/images/id-card-solid.png" class="status-icon" draggable="false" alt="id-card">
        <div class="button-text-wrapper"><span>{{ userId }}</span></div>
      </div>
      
      <!-- Кнопка профиля -->
      <div class="status-item">
        <button class="main-button skip">
          <img src="@/assets/images/user-solid.png" draggable="false" alt="add">
        </button>
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
