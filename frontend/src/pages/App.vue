<script setup>
import router from '@/router'
import Main from '@/components/JstComponents/Main.vue'
</script>

<template>
  <header class="flex items-center bg-neutral-700 justify-between p-3 pl-8 pr-8">
    <span class="text-5xl text-white font-semibold">TASKA</span>
    <div class="flex gap-2">
      <router-link
        to="/login"
        class="bg-neutral-800 p-2 rounded-lg font-semibold text-lg text-white"
        >login
      </router-link>
      <router-link to="/reg" class="bg-white p-2 rounded-lg font-semibold text-lg text-neutral-800"
        >Registration</router-link
      >
    </div>
  </header>
  <main class="flex flex-col items-center w-full h-screen bg-neutral-600">
    <section
      class="bg-neutral-60 items-center bg-purple-400 h-[20%] flex flex-col justify-center w-full"
    >
      <span class="text-6xl text-white animate-pulse font-semibold">Новый таск трекер</span>
      <span class="text-4xl text-purple-300 animate-pulse font-semibold">Новый таск трекер</span>
    </section>
  </main>
</template>
