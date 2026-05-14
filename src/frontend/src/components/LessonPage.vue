<script setup>
import { useRoute, useRouter } from 'vue-router'
import { computed, onMounted, ref } from 'vue'

const route = useRoute()
const router = useRouter()

const currentPath = computed(() => route.path)
const fullPath = computed(() => route.fullPath)
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
  <div>
    <h1>Текущий путь: {{ currentPath }}</h1>
    <p>ID урока: {{ lessonId }}</p>

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
        <button class="main-button skip">
          <img src="@/assets/images/user-solid.png" draggable="false" alt="add">
        </button>
      </div>
    </div>

  </div>

  
</template>

<style scoped>
</style>
