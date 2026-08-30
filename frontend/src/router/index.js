import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/data-analysis',
    name: 'dataAnalysis',
    component: () => import('../views/DataAnalysisView.vue')
  },
  // NUEVA RUTA: Galería completa de proyectos
  {
    path: '/proyectos',
    name: 'projects',
    component: () => import('../views/ProjectsView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      // Si la ruta tiene un #, hace un scroll suave hasta esa sección
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
    // Si no hay #, simplemente sube al inicio de la página
    return { top: 0 }
  }
});

export default router;