<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Берем имя пользователя из параметров или стейта. Если пусто — пишем Гость
const username = computed(() => route.query.username || 'Игрок')

// Функция для обработки клика по кнопке приза
const claimPrize = () => {
  // Перенаправляем пользователя обратно на карту или страницу призов
  router.push('/')
}

</script>

<template>
  <div class="winner-screen">
    <!-- Иллюстрация бобра-программиста в правом верхнем углу -->
    <div class="illustration-container">
      <img src="@/assets/images/kapi2.png" draggable="false" class="beaver-img" alt="Winner Beaver" />
    </div>

    <!-- Основной контент по центру -->
    <div class="main-content">
      <h1 class="winner-title">
        <span class="username">{ {{ username }} }</span> WINNER !!!
      </h1>
      
      <p class="subtitle">ЗАБЕРИ СВОЙ ПРИЗ</p>

      <button class="main-button winner">
        <img src="@/assets/images/crown-solid.png" draggable="false" alt="exit">
      </button>
    </div>
  </div>
</template>

<style scoped>

.winner-screen {
  position: relative;
  width: 100%;
  height: 100vh;
  background-color: #FFC107;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Arial Black', 'Impact', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.illustration-container {
  position: absolute;
  top: 2%;
  right: 2%;
  width: 42%;
  max-width: 480px;
}

.beaver-img {
  width: 100%;
  height: auto;
  display: block;
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  z-index: 10;
}

.winner-title {
  font-size: 3.5rem;
  color: #000000;
  margin: 0 0 15px 0;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.username {
  font-weight: 900;
}

.subtitle {
  font-family: sans-serif;
  font-size: 1.1rem;
  font-weight: bold;
  color: #333333;
  margin: 0 0 30px 0;
  letter-spacing: 1.5px;
}

.prize-button {
  background-color: #ff8c42;
  border: none;
  border-radius: 12px;
  width: 65px;
  height: 65px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
  transition: transform 0.1s ease, background-color 0.2s ease;
}

.prize-button:hover {
  background-color: #f07b33;
  transform: scale(1.05);
}

.prize-button:active {
  transform: scale(0.95);
}

.crown-icon {
  width: 35px;
  height: 35px;
  color: #ffffff;
}

</style>
