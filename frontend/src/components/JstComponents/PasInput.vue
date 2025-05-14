<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue'
const showPasswordNum = ref(false)

const labelVal = defineProps({
  text: String,
})
const props = defineProps({
  modelValue: String,
})
const emit = defineEmits(['update:modelVale'])
</script>

<template>
  <div class="relative flex flex-col gap-1">
    <label class="bg-neutral-700 font-semibold text-white absolute top-[-25px] p-2 left-[30px]">{{
      labelVal.text
    }}</label>
    <div
      class="bg-neutral-700 flex w-full items-center justify-between rounded-4xl border border-white px-4"
    >
      <input
        v-model="modelValue"
        :type="showPasswordNum ? 'text' : 'password'"
        placeholder="Enter your password"
        class="font-extralight text-sm w-full placeholder:text-neutral-400 rounded-4xl bg-neutral-700 text-white pt-3 pb-3 focus:outline-none"
      />
      <svg
        @click="showPasswordNum = !showPasswordNum"
        class="group cursor-pointer"
        width="25"
        height="25"
        viewBox="0 0 25 25"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g opacity="0.8">
          <path
            d="M20.2049 15.939C21.1295 15.0212 21.8434 14.1091 22.3099 13.455C22.6139 13.0287 22.7659 12.8155 22.7659 12.5C22.7659 12.1845 22.6139 11.9713 22.3099 11.545C20.9438 9.62944 17.4551 5.5 12.7659 5.5C11.8581 5.5 10.9953 5.65476 10.1841 5.91827M7.51329 7.24742C5.49705 8.6072 4.00802 10.4427 3.22191 11.545C2.91788 11.9713 2.76587 12.1845 2.76587 12.5C2.76587 12.8155 2.91788 13.0287 3.22191 13.455C4.58797 15.3706 8.07665 19.5 12.7659 19.5C14.7567 19.5 16.531 18.7557 18.0185 17.7526"
            class="stroke-[#9E9E9E] group-active:stroke-white"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M10.6237 10.5C10.0937 11.03 9.76587 11.7623 9.76587 12.5711C9.76587 14.1887 11.0772 15.5 12.6948 15.5C13.5036 15.5 14.2359 15.1722 14.7659 14.6421"
            class="stroke-[#9E9E9E] group-active:stroke-white"
            stroke-width="1.5"
            stroke-linecap="round"
          />
          <path
            d="M3.76587 3.5L21.7659 21.5"
            stroke=""
            class="stroke-[#9E9E9E] group-active:stroke-white"
            stroke-width="1.5"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </g>
      </svg>
    </div>
  </div>
</template>
