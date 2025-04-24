<script setup lang="ts">
import { ref } from 'vue'
import Buttons from '../JstComponents/Buttons.vue'

const today = new Date()
const yyyy = today.getFullYear()
const mm = String(today.getMonth() + 1).padStart(2, '0')
const dd = String(today.getDate()).padStart(2, '0')
const startDate = ref(`${yyyy}-${mm}-${dd}`)
</script>

<template>
  <div class="absolute w-full h-full bg-black/70 flex items-center justify-center">
    <div class="flex p-16 flex-col bg-neutral-700 rounded-xl w-[40%]">
      <div class="flex gap-4 justify-center flex-col">
        <div class="flex flex-col gap-2">
          <span class="text-xl text-white">Выберите Таймлайн</span>
          <input
            type="date"
            v-model="startDate"
            style="color-scheme: dark"
            class="bg-green-400 p-2 rounded-xl text-lg text-white"
          />
        </div>
        <div class="flex flex-col gap-2">
          <span class="text-xl text-white">Введите задачу</span>
          <textarea
            placeholder="Напишите здесь"
            oninput="this.style.height = 'auto'; this.style.minHeight = '100%'; this.style.height = this.scrollHeight + 'px'"
            class="bg-red-400 text-white text-lg font p-3 rounded-xl resize-none focus:outline-0"
          />
        </div>
        <button @click="" class="bg-neutral-500 text-lg p-1 rounded-xl text-white w-[30%]">
          Нажмите
        </button>
      </div>
    </div>
  </div>
</template>
