import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './css/reset.css'
import './css/style.css'
import axios from 'axios'
import './assets/tailwind.css'


axios.defaults.baseURL = 'http://127.0.0.1:8000'

//axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access')

createApp(App).use(store).use(router, axios).mount('#app')
