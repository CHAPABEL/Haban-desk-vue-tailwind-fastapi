<script setup lang="ts">
import Buttons from './Buttons.vue'
</script>

<template>
  <div class="flex justify-between items-center">
    <div class="flex gap-2">
      <Buttons>Таймлайн</Buttons>
      <Buttons>Задачи</Buttons>
    </div>
    <span class="text-sm text-white">Задач решено: 0</span>
  </div>
</template>
