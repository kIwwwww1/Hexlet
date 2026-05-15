<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { goToGithub } from '@/navigator'

const route = useRoute()
const router = useRouter()
const questions = ref([])

const selectedAnswers = ref([])

const currentQuestionIndex = ref(0)
const selectedAnswer = ref('')
const errorMessage = ref('')

const isPageLoading = ref(true)

const currentQuestion = computed(() => {
  return questions.value[currentQuestionIndex.value]
})

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
  router.push('/')
}

const goBack = () => {
  router.go(-1)
}

const checkAnswer = () => {

  const correctAnswers = currentQuestion.value.curr_answer

  // ---------- ОДИН ОТВЕТ ----------
  if (correctAnswers.length === 1) {

    if (!selectedAnswer.value) {
      errorMessage.value = 'Выберите вариант ответа'
      return
    }

    if (correctAnswers.includes(selectedAnswer.value)) {

      errorMessage.value = ''
      nextQuestion()

    } else {

      errorMessage.value = 'Неверный ответ'

    }

  }

  // ---------- НЕСКОЛЬКО ОТВЕТОВ ----------
  else {

    if (selectedAnswers.value.length === 0) {
      errorMessage.value = 'Выберите хотя бы один ответ'
      return
    }

    const sortedUserAnswers = [...selectedAnswers.value].sort()
    const sortedCorrectAnswers = [...correctAnswers].sort()

    const isCorrect =
      JSON.stringify(sortedUserAnswers) ===
      JSON.stringify(sortedCorrectAnswers)

    if (isCorrect) {

      errorMessage.value = ''
      nextQuestion()

    } else {

      errorMessage.value = 'Неверный ответ'

    }

  }

}

const selectOption = (option) => {

  if (currentQuestion.value.curr_answer.length === 1) {
    selectedAnswer.value = option
  }

  else {
    if (selectedAnswers.value.includes(option)) {

      selectedAnswers.value =
        selectedAnswers.value.filter(item => item !== option)

    } else {
      selectedAnswers.value.push(option)
    }
  }
}

const nextQuestion = () => {

  if (currentQuestionIndex.value < questions.value.length - 1) {

    currentQuestionIndex.value++
    selectedAnswer.value = ''
    selectedAnswers.value = []

  } else {
    submitTest()
  }
}

</script>

<template>
  <div class="quiz-page">

    <!-- Прелоадер -->
    <Transition name="page-preload">
      <div v-if="isPageLoading" class="page-preloader">
        <div class="preloader-spinner"></div>
        <p class="preloader-text">Загрузка задания...</p>
      </div>
    </Transition>

    <!-- Контент -->
    <div
      v-if="questions.length > 0 && currentQuestion"
      class="quiz-container"
    >

      <!-- Вопрос -->
      <div class="question-box">
        <h2>
          {{ currentQuestion.question_text }}
        </h2>
      </div>

      <!-- Картинка -->
      <div class="image-wrapper">
        <img
          src="@/assets/images/kapi1.png"
          alt="quiz-image"
          draggable="false"
          class="quiz-image"
        />
      </div>

      <!-- Ответы -->
      <div class="answers-grid">

        <button
          v-for="(option, index) in currentQuestion.options"
          :key="index"
          class="main-button answer-button"
          :class="{
            active:
              currentQuestion.curr_answer.length === 1
                ? selectedAnswer === option
                : selectedAnswers.includes(option)
          }"
          @click="selectOption(option)"
        >
          {{ option }}
        </button>

      </div>

      <p v-if="errorMessage" class="error-text">
        {{ errorMessage }}
      </p>

      <button class="main-button next-question" @click="checkAnswer">
        <img src="@/assets/images/angle-right-solid.png" draggable="false" alt="info">
      </button>

    </div>

    <!-- Левый нижний угол -->
    <div class="button-container left">
      <button @click="handleAddEnergyClick" :disabled="isProcessing" class="main-button">
        <img src="@/assets/images/question-solid.png" draggable="false" alt="info">
      </button>
      <button class="main-button skip">
        <img src="@/assets/images/forward-solid.png" draggable="false" alt="add">
      </button>
    </div>

    <div class="button-container center">
      <button @click="router.push('/')" class="main-button home">
        <img src="@/assets/images/house-solid.png" draggable="false" alt="settings">
      </button>
    </div>

    <div class="button-container right">
      <div class="status-item">
        <button class="main-button skip" @click="goToGithub">
          <img src="@/assets/images/user-solid.png" draggable="false" alt="add">
        </button>
      </div>
    </div>

  </div>
</template>


<style scoped>

.quiz-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
  font-family: sans-serif;
  /* background-color: #F0FDF4; */
}

.quiz-container {
  width: 100%;
  max-width: 1100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* ВОПРОС */

.question-box {
  width: 100%;
  background: #FFFBEC;
  padding: 25px 35px;
  border-radius: 20px;
  box-shadow: 0 4px 0 #D9C5B2;
  margin-bottom: 30px;
  margin-top: -300px;
  border: 3px solid #D9C5B2;
}

.question-box h2 {
  font-size: 32px;
  line-height: 1.4;
  color: #2d2d2d;
  margin: 0;
  text-align: center;
}

/* КАРТИНКА */

.image-wrapper {
  margin-bottom: 20px;
}

.quiz-image {
  width: 400px;
  user-select: none;
}

/* ОТВЕТЫ */

.answers-grid {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 25px;
}

/* .answer-button {
  height: 90px;
  border: none;
  border-radius: 18px;
  background: #f4ecdf;
  box-shadow: 0 5px 0 #c9b8a3;
  font-size: 28px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #1f1f1f;
}

.answer-button:hover {
  transform: translateY(-4px);
}

.answer-button:active {
  transform: translateY(2px);
}

.answer-button.active {
  background: #d9c3a3;
  transform: scale(0.97);
} */


/* ОШИБКА */
.error-text {
  margin-top: 20px;
  color: #d11a2986;
  font-size: 20px;
  font-weight: bold;
}

/* PRELOADER */
.page-preloader {
  position: fixed;
  inset: 0;
  background: white;
  z-index: 999;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.preloader-spinner {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  border: 4px solid #eee;
  border-top: 4px solid #4f46e5;
  animation: spin 0.7s linear infinite;
}

.preloader-text {
  margin-top: 20px;
  color: #4f46e5;
  font-size: 18px;
}

@keyframes spin {

  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }

}


</style>