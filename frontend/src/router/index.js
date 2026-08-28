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
});

export default router;