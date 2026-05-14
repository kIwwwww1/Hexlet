<script setup>
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const questions = ref([])

onMounted(() => {
  if (window.history.state && window.history.state.questions) {
    questions.value = window.history.state.questions
    console.log('Вопросы успешно загружены из состояния:', questions.value)
  } else {
    console.warn('Данные отсутствуют в history.state. Запускаем резервную загрузку...')
    fetchBackupQuestions(route.params.id)
  }
})

// Резервная загрузка на случай перезагрузки страницы
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
</script>

<template>
  <div class="questions-container">
    <header class="questions-header">
      <h1>Тестирование по уроку №{{ route.params.id }}</h1>
      <button @click="router.push(`/lessons/${route.params.id}`)" class="back-button">
        Вернуться к уроку
      </button>
    </header>
    
    <div v-if="questions.length > 0" class="questions-list">
      <div v-for="(question, index) in questions" :key="index" class="question-card">
        
        <!-- текст вопроса из нового поля question_text -->
        <h3 class="question-title">
          Вопрос {{ index + 1 }}: {{ question.question_text }}
        </h3>

        <!-- список вариантов ответов -->
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
    
    <div v-else class="loading-state">
      Загрузка вопросов...
    </div>
  </div>
</template>

<style scoped>
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
.back-button {
  padding: 10px 15px;
  background-color: #4f46e5;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
