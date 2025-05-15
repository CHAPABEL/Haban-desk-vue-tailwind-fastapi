<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import LoginInput from '@/components/JstComponents/LoginInput.vue'
import PasInput from '@/components/JstComponents/PasInput.vue'
import LoginApi from '@/components/JstComponents/LoginApi.vue'
const userPassVal = ref()
const userSecondPassVal = ref()
const BoolButton = ref(false)

const confirmPass = computed(() => userPassVal.value === userSecondPassVal.value)

function passwordCheked() {
  BoolButton.value = true
  if (confirmPass.value) {
    userInfoObj.userPass = userPassVal.value
    console.log(userInfoObj)
  } else {
    console.log('40404')
  }
}

function pasErrorFunction() {
  if (!BoolButton.value) {
    return 'border-white'
  } else {
    return confirmPass.value ? 'border-white' : 'border-red-500'
  }
}

const userInfoObj = reactive({
  userId: Date.now(),
  userEmail: '',
  userPass: '',
})
</script>
<template>
  <main class="w-full flex h-screen items-center justify-center bg-neutral-700">
    <section class="flex flex-col items-center w-[25%] gap-8">
      <span class="text-white text-3xl font-extrabold pb-4"> Start now! </span>
      <div class="flex w-full flex-col gap-7">
        <div class="relative flex flex-col gap-1">
          <label
            class="bg-neutral-700 font-semibold text-white absolute top-[-25px] p-2 left-[30px]"
            >Email</label
          >
          <div
            class="bg-neutral-700 flex w-full items-center justify-between rounded-4xl border border-white px-4"
          >
            <input
              type="text "
              class="font-extralight text-sm w-full placeholder:text-neutral-400 rounded-4xl bg-neutral-700 text-white pt-3 pb-3 focus:outline-none"
              placeholder="Enter your Email"
              v-model="userInfoObj.userEmail"
            />
          </div>
        </div>
        <PasInput
          text="Password"
          :wrapperClass="pasErrorFunction()"
          v-model="userPassVal"
          :boolSpan="BoolButton"
        />
        <PasInput
          text="Second password"
          v-model="userSecondPassVal"
          :wrapperClass="pasErrorFunction()"
          :boolSpan="BoolButton"
        />
      </div>
      <div class="flex flex-col w-full items-center gap-5">
        <button
          @click="passwordCheked"
          class="bg-neutral-200 text-black text-lg rounded-4xl font-semibold w-full p-2 hover:bg-neutral-300 cursor-pointer transition-all ease-in-out duration-100"
        >
          Register
        </button>
        <span class="text-neutral-500">- or -</span>
        <LoginApi />
      </div>
      <svg
        class="absolute top-0 left-0"
        width="341"
        height="508"
        viewBox="0 0 341 508"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="35.5" cy="202.5" r="305.5" fill="#8BDA7D" />
      </svg>
      <svg
        class="absolute bottom-0 right-0"
        width="405"
        height="522"
        viewBox="0 0 405 522"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="305.5" cy="305.5" r="305.5" fill="#F187C5" />
      </svg>
    </section>
  </main>
</template>
