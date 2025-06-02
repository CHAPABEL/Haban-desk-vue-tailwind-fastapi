<script setup lang="ts">
import { defineEmits } from 'vue'

const emit = defineEmits(['saveTaskData'])
</script>

<template>
  <section class="flex flex-col gap-5 justify-start pt-8 pl-4 pr-4 bg-neutral-700 w-[15%]">
    <div class="flex flex-col items-center gap-2">
      <svg
        width="44"
        height="49"
        viewBox="0 0 29 29"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M14.9721 0C3.49127 0 9.02665 13.1526 9.02665 13.1526C10.2567 14.9543 11.8969 14.594 11.8969 15.8552C11.8969 16.9362 10.4618 17.2966 9.02665 17.4767C6.77149 17.4767 4.72135 17.1164 2.67121 20.3595C1.44112 22.3414 0.82608 28.8276 0.82608 28.8276H28.913C28.913 28.8276 28.298 22.3414 27.2729 20.3595C25.2228 16.9362 23.1726 17.4767 20.9175 17.2966C19.4824 17.1164 18.0473 16.756 18.0473 15.675C18.0473 14.594 19.6874 14.9543 20.9175 12.9724C20.9175 13.1526 26.4529 0 14.9721 0V0Z"
          fill="#727272"
        />
      </svg>
      <span class="text-lg text-white font-semibold">{{ 'Никита' }}</span>
    </div>
    <div class="flex flex-col border-t-2 border-b-2 gap-5 pt-5 border-neutral-400 pb-5">
      <button
        class="text-white text-left pl-4 h-10 cursor-pointer rounded-sm transition-all duration-200 ease-in-out text-lg font-semibold hover:bg-neutral-600"
      >
        Главная
      </button>

      <button
        class="text-white text-left pl-4 h-10 cursor-pointer text-lg rounded-sm transition-all duration-200 ease-in-out font-semibold hover:bg-neutral-600"
      >
        Мои задания
      </button>
    </div>
    <button
      @click="emit('saveTaskData')"
      class="text-white text-left pl-4 h-10 cursor-pointer text-lg rounded-sm transition-all duration-200 ease-in-out font-semibold hover:bg-neutral-600"
    >
      Сохранить
    </button>
  </section>
</template>
