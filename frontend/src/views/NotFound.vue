<script setup lang="ts"></script>

<template>
  <div class="flex flex-col animate-spin items-center justify-center h-screen bg-neutral-600">
    <h1 class="font-bold text-[200px] text-white mb-4">404</h1>
    <p class="text-xl text-white mb-8">Страница не найдена</p>
    <router-link to="/" class="text-red-400 hover:underline">Вернуться на главную</router-link>
  </div>
</template>
