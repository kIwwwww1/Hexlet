<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { goToGithub } from '@/navigator'

const route = useRoute()
const router = useRouter()
const questions = ref([])

const isPageLoading = ref(true)

onMounted(() => {
  // Искусственная задержка в 500мс для плавной анимации входа
  setTimeout(() => {
    isPageLoading.value = false
  }, 500)

  if (window.history.state && window.history.state.questions) {
    questions.value = window.history.state.questions
    console.log('Вопросы успешно загружены из состояния:', questions.value)
  } else {
    console.warn('Данные отсутствуют в history.state. Запускаем резервную загрузку...')
    fetchBackupQuestions(route.params.id)
  }
})

const fetchBackupQuestions = async (id) => {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/lessons/${id}`, {
      method: 'GET',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' }
    })
    if (response.ok) {
      const data = await response.json()
      questions.value = data.questions
    }
  } catch (error) {
    console.error('Ошибка при восстановлении данных:', error)
  }
}

const submitTest = () => {
  console.log('Тест завершен')
  router.push('/winner')
}

const goBack = () => {
  router.go(-1)
}
</script>

<template>
  <div class="page-wrapper">

    <!-- Анимация появления/исчезновения самого экрана загрузки -->
    <Transition name="page-preload">
      <div v-if="isPageLoading" class="page-preloader">
        <div class="preloader-spinner"></div>
        <p class="preloader-text">Загрузка задания...</p>
      </div>
    </Transition>

    <div class="questions-container">
      <header class="questions-header">
        <h1>Задание #{{ route.params.id }}</h1>
      </header>
      
      <Transition name="fade" mode="out-in">
        <!-- Основной блок с вопросами -->
        <div v-if="questions.length > 0" class="questions-list" key="questions-content">
          <div v-for="(question, index) in questions" :key="index" class="question-card">
            
            <h3 class="question-title">
              Вопрос {{ index + 1 }}: {{ question.question_text }}
            </h3>

            <ul class="options-list">
              <li v-for="(option, oIndex) in question.options" :key="oIndex" class="option-item">
                <label class="option-label">
                  <input 
                    type="radio" 
                    :name="'question-' + index" 
                    :value="option" 
                    class="option-input"
                  />
                  <span class="option-text">{{ option }}</span>
                </label>
              </li>
            </ul>

          </div>
        </div>
        
        <div v-else class="loading-state" key="loading-skeleton">
          <div class="skeleton-card" v-for="i in 3" :key="i">
            <div class="skeleton-line title"></div>
            <div class="skeleton-line option"></div>
            <div class="skeleton-line option"></div>
            <div class="skeleton-line option"></div>
          </div>
        </div>
      </Transition>
      
      <div class="button-container left">
        <button class="main-button">
          <img src="@/assets/images/question-solid.png" draggable="false" alt="info">
        </button>
        <button class="main-button skip">
          <img src="@/assets/images/forward-solid.png" draggable="false" alt="forward">
        </button>
      </div>
      
      <div class="button-container center">
        <button @click="router.push('/')" class="main-button home">
          <img src="@/assets/images/house-solid.png" draggable="false" alt="home">
        </button>
        
        <button @click="goBack" class="main-button go-tests">
          <img src="@/assets/images/angle-right-solid.png" draggable="false" alt="back">
        </button>
      </div>

      <div class="button-container right">
        <div class="status-item">
          <button class="main-button skip" @click="goToGithub">
            <img src="@/assets/images/user-solid.png" draggable="false" alt="user">
          </button>
        </div>
      </div>
    </div>

  </div>
</template>


<style scoped>

.main-button img {
  width: 24px;
  height: 24px;
  display: block;
  object-fit: contain;
  color: transparent;
  font-size: 0;
}

.questions-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.questions-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.question-card {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}

.question-title {
  margin-top: 0;
  color: #333;
}

.options-list {
  list-style: none;
  padding: 0;
}

.option-item {
  margin: 10px 0;
}

.option-label {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.option-input {
  margin-right: 10px;
}

/* Отражение иконки стрелочки влево */
.main-button.go-tests :deep(img),
.main-button.go-tests img {
    transform: scaleX(-1) !important;
}

/* --- ПОЛНОЭКРАННЫЙ ПРЕЛОАДЕР НА ПОЛСЕКУНДЫ --- */
.page-preloader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #ffffff; /* Цвет фона под тему вашего приложения */
  z-index: 9999;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.preloader-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #4f46e5; /* Индиго/Синий акцент */
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.preloader-text {
  margin-top: 15px;
  font-family: sans-serif;
  color: #4f46e5;
  font-weight: 500;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Анимация исчезновения прелоадера */
.page-preload-leave-active {
  transition: opacity 0.3s ease;
}
.page-preload-leave-to {
  opacity: 0;
}

/* --- АНИМАЦИЯ ПЕРЕХОДА ДЛЯ ВОПРОСОВ --- */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* --- СТИЛИ ДЛЯ СКЕЛЕТОНА ЗАГРУЗКИ --- */
.loading-state {
  display: flex;
  flex-direction: column;
}

.skeleton-card {
  background: #f1f1f1;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}

.skeleton-line {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: loading-shimmer 1.5s infinite;
  border-radius: 4px;
}

.skeleton-line.title {
  height: 24px;
  width: 70%;
  margin-bottom: 20px;
}

.skeleton-line.option {
  height: 16px;
  width: 40%;
  margin: 12px 0;
}

@keyframes loading-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
</style>
