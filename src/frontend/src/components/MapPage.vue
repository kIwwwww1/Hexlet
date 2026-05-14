<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { goToGithub } from '@/navigator'
import { reduceUserEnergy } from '@/func'

const router = useRouter()

const userEnergy = ref(0)
const userId = ref('XXXXXX')
const maxPassedLevel = ref(0) 


// Функция для определения цвета кнопки
const getLvlClass = (levelNum) => {
  if (levelNum <= maxPassedLevel.value) {
    return 'passed'
  } else if (levelNum === maxPassedLevel.value + 1) {
    return 'current'
  } else {
    return 'locked'
  }
}

// Асинхронная функция для запроса данных пользователя
const loadUserData = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/users/my', {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      }
    })

    if (!response.ok) {
      throw new Error(`Ошибка сервера: ${response.status}`)
    }

    const data = await response.json()

    userId.value = data.unique_id
    userEnergy.value = data.energy
    maxPassedLevel.value = data.floor_level

  } catch (error) {
    console.error('Не удалось загрузить данные с бэкенда:', error)
    
    userId.value = 'Ошибка загрузки'
    maxPassedLevel.value = 0 
  }
}

const goToLevel = (levelNum) => {
  if (levelNum <= maxPassedLevel.value + 1) {
    router.push(`/lessons/${levelNum}`)
  } else {
    alert('Этот уровень еще заблокирован!')
  }
}

const handleLevelClick = async (levelNumber) => {
  try {
    await reduceUserEnergy() 
    
    goToLevel(levelNumber) 
  } catch (error) {
    console.error('Не удалось списать энергию, переход отменен:', error)
  }
}

onMounted(async () => {
  await loadUserData()
})
</script>


<template>
  <div class="app-container">

    <!-- Кнопка ВЫХОД -->
    <div class="button-container top-center">
      <button v-if="maxPassedLevel == 10" @click="router.push('/winner')" class="main-button exit">
        <img src="@/assets/images/door-open-solid.png" draggable="false" alt="exit">
      </button>
    </div>

        <!-- КАРТА УРОВНЕЙ -->
    <div class="levels-map">
      <!-- Уровень 1 -->
      <button @click="handleLevelClick(1)" :class="['main-button level-node lvl-1', getLvlClass(1), { 'hidden-level': !(1 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/terminal-solid.png" draggable="false" alt="level-1">
      </button>

      <!-- Уровень 2 -->
      <button @click="handleLevelClick(2)" :class="['main-button level-node lvl-2', getLvlClass(2), { 'hidden-level': !(2 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/lightbulb-solid.png" draggable="false" alt="level-2">
      </button>

      <!-- Уровень 3 -->
      <button @click="handleLevelClick(3)" :class="['main-button level-node lvl-3', getLvlClass(3), { 'hidden-level': !(3 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/code-solid.png" draggable="false" alt="level-3">
      </button>

      <!-- Уровень 4 -->
      <button @click="handleLevelClick(4)" :class="['main-button level-node lvl-4', getLvlClass(4), { 'hidden-level': !(4 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/dumbbell-solid.png" draggable="false" alt="level-4">
      </button>

      <!-- Уровень 5 -->
      <button @click="handleLevelClick(5)" :class="['main-button level-node lvl-5', getLvlClass(5), { 'hidden-level': !(5 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/terminal-solid.png" draggable="false" alt="level-5">
      </button>

      <!-- Уровень 6 -->
      <button @click="handleLevelClick(6)" :class="['main-button level-node lvl-6', getLvlClass(6), { 'hidden-level': !(6 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/layer-group-solid.png" draggable="false" alt="level-6">
      </button>

      <!-- Уровень 7 -->
      <button @click="handleLevelClick(7)" :class="['main-button level-node lvl-7', getLvlClass(7), { 'hidden-level': !(7 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/lightbulb-solid.png" draggable="false" alt="level-7">
      </button>

      <!-- Уровень 8 -->
      <button @click="handleLevelClick(8)" :class="['main-button level-node lvl-8', getLvlClass(8), { 'hidden-level': !(8 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/code-solid.png" draggable="false" alt="level-8">
      </button>

      <!-- Уровень 9 -->
      <button @click="handleLevelClick(9)" :class="['main-button level-node lvl-9', getLvlClass(9), { 'hidden-level': !(9 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/dumbbell-solid.png" draggable="false" alt="level-9">
      </button>

      <!-- Уровень 10 -->
      <button @click="handleLevelClick(10)" :class="['main-button level-node lvl-10', getLvlClass(10), { 'hidden-level': !(10 <= maxPassedLevel + 1) }]">
        <img src="@/assets/images/brain-solid.png" draggable="false" alt="level-10">
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
      <button @click="router.push('/')" class="main-button home">
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
        <button class="main-button skip" @click="goToGithub">
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
