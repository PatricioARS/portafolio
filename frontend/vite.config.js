import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],
  server: {
    proxy: {
      // Redirige las peticiones de la API a Django
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      // Redirige las peticiones de las imágenes a Django
      '/media': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      }
    }
  }
})