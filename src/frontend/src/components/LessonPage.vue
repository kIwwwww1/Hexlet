<script setup>
import { useRoute, useRouter } from 'vue-router'
import { computed, onMounted, ref } from 'vue'

const route = useRoute()
const router = useRouter()

const lessonId = computed(() => route.params.id)

const lessonData = ref(null)

// Асинхронная функция для запроса данных урока
const loadLessonData = async () => {
  try {
    const response = await fetch(`http://localhost:8000/api/v1/lessons/${lessonId.value}`, {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      }
    });

    if (!response.ok) {
      const errorData = await response.json(); 
      throw new Error(`Ошибка HTTP: ${response.status}. Сообщение: ${JSON.stringify(errorData)}`);
    }

    const data = await response.json();
    
    console.log('Данные успешно получены:', data); 
    lessonData.value = data;

  } catch (error) {
    console.error('Ошибка при загрузке данных урока:', error);
  }
};

onMounted(async () => {
  await loadLessonData()
})

</script>

<template>
  <div class="lesson-container">

    <!-- Ждем, пока данные загрузятся -->
    <div v-if="lessonData" class="lesson-content">
      <h1 class="lesson-title">{{ lessonData.title }}</h1>

      <div class="lesson-info" v-html="lessonData.information"></div>
      
      <div class="lesson-image-wrapper">
        <img src="@/assets/images/kapi3.png" alt="Иллюстрация к уроку" class="lesson-image" />
      </div>
    </div>
    
    <!-- Индикатор загрузки, пока fetch не завершился -->
    <div v-else class="loading-state">
      Загрузка данных урока...
    </div>

    <div class="button-container left">
      <button class="main-button">
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
      <button @click="router.push('/')" class="main-button go-tests">
        <img src="@/assets/images/angle-right-solid.png" draggable="false" alt="settings">
      </button>
    </div>

    <div class="button-container right">
      <div class="status-item">
        <button class="main-button skip">
          <img src="@/assets/images/user-solid.png" draggable="false" alt="add">
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>

.main-button {
  opacity: 0.5;
}

.main-button.home {
  opacity: 0.95;
}

.main-button.go-tests{
  opacity: 0.95;
}

/* Общий контейнер страницы */
.lesson-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: sans-serif;
  padding-bottom: 120px;
}

/* Стилизация контента */
.lesson-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Основной заголовок урока (из поля title) */
.lesson-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 30px;
  color: #2c3e50;
  text-align: center;
}

/* Блок с HTML-информацией */
.lesson-info {
  font-size: 1.15rem;
  line-height: 1.7;
  color: #34495e;
  width: 100%;
  margin-bottom: 40px;
}

/* Стилизация HTML-тегов внутри v-html через :deep() */

/* Абзацы текста */
.lesson-info :deep(p) {
  margin-bottom: 18px;
  text-align: justify;
}

/* Стили для подзаголовков, которые могут прийти в разметке (h2, h3, h4) */
.lesson-info :deep(h2),
.lesson-info :deep(h3),
.lesson-info :deep(h4) {
  color: #1a252f;
  font-weight: 600;
  margin-top: 32px;
  margin-bottom: 16px;
  text-align: center;
}

.lesson-info :deep(h2) { font-size: 1.8rem; }
.lesson-info :deep(h3) { font-size: 1.5rem; }

/* Списки (маркированные и нумерованные) */
.lesson-info :deep(ul), 
.lesson-info :deep(ol) {
  margin: 16px 0;
  padding-left: 30px;
}

.lesson-info :deep(li) {
  margin-bottom: 24px;
}

/* Выделение важного текста */
.lesson-info :deep(strong),
.lesson-info :deep(b) {
  color: #2c3e50;
  font-weight: 700;
}

/* Выделение цитат или важных блоков текста */
.lesson-info :deep(blockquote) {
  border-left: 4px solid #42b983;
  background-color: #f8f9fa;
  padding: 12px 20px;
  margin: 20px 0;
  font-style: italic;
  border-radius: 0 8px 8px 0;
}

/* Стили терминала перенесены внутрь :deep() */
.lesson-info :deep(.terminal-window) {
  background-color: #1e1e1e;
  color: #75beff;
  padding: 15px;
  border-radius: 6px;
  border: 1px solid #3c3c3c;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  margin: 12px 0 0 0;
  overflow-x: auto;
  text-align: left;
  display: block;
}

.lesson-info :deep(.terminal-window code) {
  font-family: 'Consolas', 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.5;
  background: none;
  padding: 0;
  color: #75beff;
}

/* Стили для маленького встроенного кода прямо в строке */
.lesson-info :deep(code) {
  background-color: #f4f4f4;
  color: #d63384;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.95em;
}

/* --- Изображение --- */
.lesson-image-wrapper {
  width: 100%;
  max-width: 400px;
  display: flex;
  justify-content: center;
  margin-top: -20px;
}

.lesson-image {
  width: 100%;
  height: auto;
  /* border-radius: 16px; */
  /* box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08); */
}

/* Состояние загрузки */
.loading-state {
  text-align: center;
  font-size: 1.3rem;
  margin-top: 80px;
  color: #95a5a6;
}

</style>
