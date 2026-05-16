<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { goToGithub } from '@/navigator'
import { reduceUserEnergy, addUserEnergy } from '@/func'

const router = useRouter()

const userEnergy = ref(0)
const userId = ref('XXXXXX')
const maxPassedLevel = ref(0)
const isProcessing = ref(false)

const DEFAULT_ICON = 'terminal-solid.png'
const PASSED_ICON = 'location-dot-solid.png'

const LEVEL_ICONS = {
  1: 'terminal-solid.png',
  2: 'lightbulb-solid.png',
  3: 'code-solid.png',
  4: 'dumbbell-solid.png',
  5: 'terminal-solid.png',
  6: 'layer-group-solid.png',
  7: 'lightbulb-solid.png',
  8: 'code-solid.png',
  9: 'dumbbell-solid.png',
  10: 'brain-solid.png',
  11: 'location-dot-solid.png',
}

const getIconUrl = (levelNum) => {
  if (levelNum === maxPassedLevel.value + 1) {
    return new URL(`/src/assets/images/${PASSED_ICON}`, import.meta.url).href
  }
     
  const filename = LEVEL_ICONS[levelNum] || DEFAULT_ICON
  return new URL(`/src/assets/images/${filename}`, import.meta.url).href
}

const getLvlClass = (levelNum) => {
  if (levelNum <= maxPassedLevel.value) return 'passed'
  if (levelNum === maxPassedLevel.value + 1) return 'current'
  return 'locked'
}

const loadUserData = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/users/my', {
      method: 'GET',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' }
    })

    if (!response.ok) throw new Error(`Ошибка сервера: ${response.status}`)

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

const handleAddEnergyClick = async () => {
  if (isProcessing.value) return
  try {
    isProcessing.value = true
    const newEnergy = await addUserEnergy()
    userEnergy.value = newEnergy
  } catch (error) {
    alert('Не удалось добавить энергию. Попробуйте позже.')
  } finally {
    isProcessing.value = false
  }
}

const handleLevelClick = async (levelNumber) => {
  if (levelNumber > maxPassedLevel.value + 1) {
    alert('Этот уровень еще заблокирован!')
    return
  }

  if (isProcessing.value) return

  try {
    isProcessing.value = true
         
    const newEnergy = await reduceUserEnergy()
         
    userEnergy.value = newEnergy
         
    router.push(`/lessons/${levelNumber}`)
  } catch (error) {
    console.error('Произошла ошибка при обработке входа:', error)
    if (error.message && error.message.includes('400')) {
      alert('У вас закончились жизни! Дождитесь восстановления энергии, чтобы войти.')
    } else {
      alert('Ошибка при попытке начать уровень. Попробуйте позже.')
    }
  } finally {
    isProcessing.value = false
  }
}

// Функция для генерации случайных строк
const generateRandomData = () => {
  const randomStr = Math.random().toString(36).substring(2, 10)
  return {
    user_name: `user_${randomStr}`,
    email: `test_${randomStr}@example.com`,
    password: `Pass_${randomStr}123`
  }
}

// Функция создания нового пользователя
const handleCreateUserClick = async () => {
  if (isProcessing.value) return
  
  try {
    isProcessing.value = true
    const randomPayload = generateRandomData()

    const response = await fetch('http://localhost:8000/api/v1/users/create', {
      method: 'POST',
      credentials: 'include',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(randomPayload)
    })

    if (!response.ok) throw new Error(`Ошибка создания: ${response.status}`)

    const data = await response.json()
    alert(`Пользователь успешно создан! ID: ${data.unique_id || 'ОК'}`)
    
    // Опционально: перезагружаем данные, если создали текущего юзера
    await loadUserData()

  } catch (error) {
    console.error('Ошибка при создании пользователя:', error)
    alert('Не удалось создать пользователя.')
  } finally {
    isProcessing.value = false
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
      <button v-if="maxPassedLevel === 10" @click="router.push('/winner')" class="main-button exit">
        <img src="@/assets/images/door-open-solid.png" draggable="false" alt="exit">
      </button>
    </div>

    <!-- КАРТА УРОВНЕЙ -->
    <div class="levels-map">
      <button 
         v-for="level in 10" 
         :key="level"
        :disabled="isProcessing" 
         @click="handleLevelClick(level)" 
         :class="[
          'main-button level-node', 
          `lvl-${level}`,
          getLvlClass(level),
          { 'hidden-level': !(level <= maxPassedLevel + 1) }
        ]"
      >
        <img :src="getIconUrl(level)" draggable="false" :alt="`level-${level}`">
      </button>
    </div>

    <!-- Левый нижний угол -->
    <div class="button-container left">
      <button @click="handleAddEnergyClick" :disabled="isProcessing" class="main-button">
        <img src="@/assets/images/question-solid.png" draggable="false" alt="info">
      </button>
      <button @click="router.push('/winner')" class="main-button skip">
        <img src="@/assets/images/forward-solid.png" draggable="false" alt="add">
      </button>
    </div>
         
    <!-- Центральная нижняя кнопка ДОМ и новая кнопка ПЛЮС -->
    <div class="button-container center">
      <button @click="router.push('/')" class="main-button home">
        <img src="@/assets/images/house-solid.png" draggable="false" alt="settings">
      </button>

      <button @click="handleCreateUserClick" :disabled="isProcessing" class="main-button create-user">
        <img src="@/assets/images/user-solid.png" draggable="false" alt="create-user">
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

/* Стили для выстраивания кнопок в ряд внутри центрального контейнера */
.button-container.center {
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
</style>
