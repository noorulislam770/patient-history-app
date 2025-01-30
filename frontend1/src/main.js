import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import './assets/tailwind.css'

const app = createApp(App)

app.config.globalProperties.$axios = axios.create({
  baseURL: "https://patient-history-app.onrender.com/", // Django backend URL
})

app.use(router)
app.mount('#app')
