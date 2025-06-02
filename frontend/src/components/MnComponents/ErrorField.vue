<script setup lang="ts">
const props = defineProps({
  errorText: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <div class="flex absolute top-0 right-0 animate-bounce bg-red-400 p-4">
    <span class="text-2xl text-white font-semibold">{{ errorText }}</span>
  </div>
</template>
