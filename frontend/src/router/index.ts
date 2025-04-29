import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../pages/App.vue'),
  },
  {
    path: '/tskBoard',
    component: () => import('../pages/TaskBoard.vue'),
  },
  {
    path: '/login',
    component: () => import('../pages/Autorisation.vue'),
  },
  {
    path: '/registration',
    component: () => import('../pages/Registration.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router

createApp(RouterView).use(router).mount('body')
