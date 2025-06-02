import path from 'path'
import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../pages/App.vue'),
  },
  {
    path: '/tasks',
    component: () => import('../pages/TaskBoard.vue'),
  },
  {
    path: '/reg',
    component: () => import('../pages/Registration.vue'),
  },
  {
    path: '/login',
    component: () => import('../pages/Login.vue'),
  },
  {
    path: '/:pathMAtch(.*)*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router

createApp(RouterView).use(router).mount('body')
