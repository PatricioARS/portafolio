import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite' // <-- 1. Importamos el nuevo motor

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(), // <-- 2. Lo conectamos aquí
  ],
})