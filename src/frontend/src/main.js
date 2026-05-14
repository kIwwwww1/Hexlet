import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router' 
import App from './App.vue'

import LevelPage from './components/LessonPage.vue'
import HOME from './components/MapPage.vue'
import WinPage from './components/WinPage.vue'


const routes = [
  { 
    path: '/',
    component: HOME
  },
  { 
    path: '/lessons/:id',
    component: LevelPage 
  },
  { 
    path: '/winner',
    component: WinPage 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)

app.use(createPinia())

app.use(router) 

app.mount('#app')
