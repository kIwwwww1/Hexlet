<script setup>
import { computed, ref, onMounted} from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

// Реактивная переменная для отслеживания показа видео
const isVideoVisible = ref(false)

const showVideo = () => {
  isVideoVisible.value = true
}

const setVideoVolume = (el) => {
  if (el) {
    el.volume = 0.25
  }
}

const userName = ref('')

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

    userName.value = data.user_name

  } catch (error) {
    console.error('Не удалось загрузить данные с бэкенда:', error)
  }
}

onMounted(async () => {
  await loadUserData()
})

</script>

<template>
  <div class="winner-screen">

    <!-- Иллюстрация скрывается, когда воспроизводится видео -->
    <div v-if="!isVideoVisible" class="illustration-container">
      <img src="@/assets/images/kapi2.png" draggable="false" class="beaver-img" alt="Winner Beaver" />
    </div>

    <!-- Основной контент (скрывается после клика на кнопку) -->
    <div v-if="!isVideoVisible" class="main-content">
      <h1 class="winner-title">
        <span class="username">{{ userName }}</span> WINNER !!!
      </h1>
      
      <p class="subtitle">ЗАБЕРИ СВОЙ ПРИЗ</p>
      <!-- <h1>↓</h1> -->
      <!-- При нажатии вызываем функцию показа видео -->
      <button @click="showVideo" class="main-button winner">
        <img src="@/assets/images/crown-solid.png" draggable="false" alt="exit">
      </button>
    </div>

    <!-- Контейнер с видеоплеером (показывается только после клика) -->
    <div v-else class="video-container">
      <video :ref="setVideoVolume" class="prize-video" controls autoplay>
        <source src="@/assets/videos/kapi.mp4" type="video/mp4" />
        Ваш браузер не поддерживает встроенные видео.
      </video>
      
      <!-- Кнопка закрытия видео, если нужно вернуться обратно к экрану победы -->
      <button @click="isVideoVisible = false" class="close-video-btn">✕ Закрыть видео</button>
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


/* СТИЛИ ДЛЯ ВИДЕОПЛЕЕРА */
.video-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80%;
  max-width: 800px;
  z-index: 20;
}

.prize-video {
  width: 100%;
  height: auto;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  background-color: #000000;
}

.close-video-btn {
  margin-top: 15px;
  background-color: #333333;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  font-family: sans-serif;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.close-video-btn:hover {
  background-color: #000000;
}

</style>
