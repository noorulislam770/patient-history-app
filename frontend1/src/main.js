import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import './assets/tailwind.css';

const app = createApp(App);

app.config.globalProperties.$axios = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Django backend URL
});

app.use(router);
app.mount('#app');
