<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const questions = ref([])

onMounted(() => {
  // Выводим в консоль весь объект для диагностики
  console.log('Полный history.state:', window.history.state)

  // В Vue Router данные state лежат на верхнем уровне window.history.state
  if (window.history.state && window.history.state.questions) {
    questions.value = window.history.state.questions
    console.log('Вопросы успешно получены:', questions.value)
  } else {
    console.warn('Данные в history.state отсутствуют. Делаем резервный запрос...')
    // РЕЗЕРВНЫЙ ВАРИАНТ: Если пользователь обновил страницу (F5) или отработал Vite,
    // нужно загрузить данные заново по ID из URL
    fetchBackupQuestions(route.params.id)
  }
})

// Функция на случай потери состояния (например, при F5)
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
      console.log('Вопросы восстановлены из бэкенда:', questions.value)
    }
  } catch (error) {
    console.error('Не удалось восстановить данные:', error)
  }
}
</script>


<template>
  <div class="questions-container">
    <h1>Вопросы к уроку №{{ route.params.id }}</h1>
    
    <div v-if="questions.length > 0">
      <div v-for="(question, index) in questions" :key="index" class="question-block">
        
        <!-- 1. Выводим текст самого вопроса (замените .text на нужный ключ, если он называется иначе) -->
        <h3 class="question-text">
          {{ index + 1 }}. {{ question.text || question.question || 'Текст вопроса отсутствует в API' }}
        </h3>

        <!-- 2. Красивый вывод вариантов ответов списком, а не одной строкой -->
        <ul class="options-list">
          <li v-for="(option, oIndex) in question.options" :key="oIndex" class="option-item">
            <label>
              <input type="radio" :name="'question-' + index" :value="option" />
              {{ option }}
            </label>
          </li>
        </ul>

      </div>
    </div>
    <div v-else>
      <p>Вопросы не найдены.</p>
    </div>
  </div>
</template>

<style scoped>
/* Ваши стили */
</style>
