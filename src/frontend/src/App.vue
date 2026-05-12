<script setup>
import { ref } from 'vue'

const userEnergy = ref(0)
const userId = ref('Загрузка...')

</script>

<template>
  <div class="app-container">

    <!-- Кнопка ВЫХОД -->
    <div class="button-container top-center">
      <button class="main-button exit">
        <img src="@/assets/images/door-open-solid.png" draggable="false" alt="exit">
      </button>
    </div>

    <!-- КАРТА УРОВНЕЙ -->
    <div class="levels-map">
      <!-- Уровень 10 -->
      <button class="main-button home level-node lvl-10">
        <img src="@/assets/images/brain-solid.png" draggable="false" alt="level-10">
      </button>
      
      <!-- Уровень 9 -->
      <button class="main-button home level-node lvl-9">
        <img src="@/assets/images/dumbbell-solid.png" draggable="false" alt="level-9">
      </button>
      
      <!-- Уровень 8 -->
      <button class="main-button home level-node lvl-8">
        <img src="@/assets/images/code-solid.png" draggable="false" alt="level-8">
      </button>
      
      <!-- Уровень 7 -->
      <button class="main-button home level-node lvl-7">
        <img src="@/assets/images/lightbulb-solid.png" draggable="false" alt="level-7">
      </button>
      
      <!-- Уровень 6 -->
      <button class="main-button home level-node lvl-6">
        <img src="@/assets/images/layer-group-solid.png" draggable="false" alt="level-6">
      </button>
      
      <!-- Уровень 5 -->
      <button class="main-button home level-node lvl-5">
        <img src="@/assets/images/terminal-solid.png" draggable="false" alt="level-5">
      </button>
      
      <!-- Уровень 4 -->
      <button class="main-button home level-node lvl-4">
        <img src="@/assets/images/dumbbell-solid.png" draggable="false" alt="level-4">
      </button>
      
      <!-- Уровень 3 -->
      <button class="main-button home level-node lvl-3">
        <img src="@/assets/images/code-solid.png" draggable="false" alt="level-3">
      </button>
      
      <!-- У–ровень 2 -->
      <button class="main-button home level-node lvl-2">
        <img src="@/assets/images/lightbulb-solid.png" draggable="false" alt="level-2">
      </button>
      
      <!-- Уровень 1 (Первый уровень у дома) -->
      <button class="main-button home level-node lvl-1">
        <img src="@/assets/images/terminal-solid.png" draggable="false" alt="level-1">
      </button>
    </div>



    <!-- Левый нижний угол -->
    <div class="button-container left">
      <button class="main-button">
        <img src="@/assets/images/question-solid.png" draggable="false" alt="info">
      </button>
      <button class="main-button skip">
        <img src="@/assets/images/forward-solid.png" draggable="false" alt="add">
      </button>
    </div>
    
    <!-- Центральная нижняя кнопка ДОМ -->
    <div class="button-container center">
      <button class="main-button home">
        <img src="@/assets/images/house-solid.png" draggable="false" alt="settings">
      </button>
    </div>

    <!-- Правый нижний угол -->
    <div class="button-container right">
      <div class="status-item">
        <img src="@/assets/images/apple-whole-solid.png" draggable="false" class="status-icon" alt="apple">
        <div class="button-text-wrapper"><span>{{ userEnergy }}</span></div>
      </div>
      <div class="status-item">
        <img src="@/assets/images/id-card-solid.png" class="status-icon" draggable="false" alt="id-card">
        <div class="button-text-wrapper"><span>{{ userId }}</span></div>
      </div>
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



.levels-map {
  position: fixed;
  top: 120px;
  bottom: 120px;
  left: 50%;
  transform: translateX(-50%);
  
  width: 200px;
  display: flex;
  flex-direction: column-reverse;
  justify-content: space-between;
  align-items: center; 
}

.level-node img {
  width: 28px;
  height: 28px;
  object-fit: contain;
}


.level-node {
  font-size: 18px;
  font-weight: bold;
  color: white;
}


.lvl-1, .lvl-5, .lvl-9 {
  transform: translateX(0);
}

.lvl-2, .lvl-4, .lvl-10 {
  transform: translateX(50px);
}

.lvl-3, .lvl-6, .lvl-8 {
  transform: translateX(-50px);
}

.lvl-7 {
  transform: translateX(-25px);
}


.level-node:active { transform: translateY(4px); }
.lvl-1:active, .lvl-5:active, .lvl-9:active { transform: translateX(0) translateY(4px); }
.lvl-2:active, .lvl-4:active, .lvl-10:active { transform: translateX(50px) translateY(4px); }
.lvl-3:active, .lvl-6:active, .lvl-8:active { transform: translateX(-50px) translateY(4px); }
.lvl-7:active { transform: translateX(-25px) translateY(4px); }


</style>
