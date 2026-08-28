import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

// Importamos el componente global de ECharts
import ECharts from 'vue-echarts'

const app = createApp(App)

// Le decimos a Vue: "Oye, cada vez que veas <v-chart> en el HTML, usa ECharts"
app.component('v-chart', ECharts)
app.use(router)

app.mount('#app')