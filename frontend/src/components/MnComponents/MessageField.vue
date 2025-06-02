<script setup lang="ts">
import { ref } from 'vue'
const visible = ref(false)
const props = defineProps({
  message: {
    type: String,
    default: '',
  },
})

function showOptionaly() {
  visible.value = true
  setTimeout(() => {
    visible.value = false
  }, 3000)
}
</script>

<template>
  <div class="flex absolute top-0 right-0 animate-bounce bg-green-500 p-4">
    <span class="text-2xl text-white font-semibold">{{ message }}</span>
  </div>
</template>
