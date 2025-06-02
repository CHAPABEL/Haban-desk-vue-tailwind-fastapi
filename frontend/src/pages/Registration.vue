<script setup lang="ts">
import { reactive, ref, computed } from 'vue'
import ErrorField from '@/components/MnComponents/ErrorField.vue'
import PasInput from '@/components/JstComponents/PasInput.vue'
import LoginApi from '@/components/JstComponents/LoginApi.vue'
import type { create } from 'domain'
import router from '@/router'
const BoolButton = ref(false)
const ShowError = ref(false)
const errorTextVal = ref('')

const confirmPass = computed(
  () =>
    ShowError.value === true ||
    (userInfoObj.userPass === userInfoObj.userSecondPass &&
      userInfoObj.userPass.trim() !== '' &&
      userInfoObj.userSecondPass.trim() !== ''),
)

const showValidationError = computed(() => !confirmPass.value || ShowError.value)

function pasErrorFunction() {
  if (!BoolButton.value) return 'border-neutral-400 text-white'
  return showValidationError.value ? 'border-red-400 text-red-400' : 'border-white text-white'
}

const userInfoObj = reactive({
  userEmail: '',
  userPass: '',
  userSecondPass: '',
})

async function passwordCheked() {
  BoolButton.value = true
  if (!confirmPass.value) {
    console.log('Пароли не совпадают')
    errorTextVal.value = 'Пароли не совпадают'
    return
  }
  try {
    const response = await fetch('http://127.0.0.1:8000/auth/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_email: userInfoObj.userEmail,
        user_password: userInfoObj.userPass,
        user_create_at: new Date().toISOString(),
      }),
    })
    const data = await response.json()

    if (response.ok) {
      localStorage.setItem('jwt_token', data.token)
      router.push('/tasks')
    } else if (response.status === 422 || response.status === 400) {
      ShowError.value = true
      errorTextVal.value = data.detail || 'Неправильно веденное поле'
    }
  } catch (error) {
    console.log(error)
  }
}
</script>
<template>
  <main class="w-full flex h-screen items-center justify-center bg-neutral-700">
    <section
      class="relative z-50 flex flex-col items-center w-[70%] md:w-[30%] lg:w-[45%] xl:w-[25%] gap-8"
    >
      <span class="text-white text-3xl font-extrabold pb-4"> Start now! </span>
      <div class="flex w-full flex-col gap-7">
        <PasInput
          text="Email"
          v-model="userInfoObj.userEmail"
          type="text"
          placeholder="Enter your Email"
          :errorText="pasErrorFunction()"
          :wrapperClass="pasErrorFunction()"
          :ShowSvg="false"
        />

        <PasInput
          text="Password"
          placeholder="Enter your Password"
          :errorText="pasErrorFunction()"
          :wrapperClass="pasErrorFunction()"
          v-model="userInfoObj.userPass"
          :boolSpan="BoolButton"
        />
        <PasInput
          text="Second password"
          placeholder="Repeat your Password"
          v-model="userInfoObj.userSecondPass"
          :errorText="pasErrorFunction()"
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
    </section>
    <svg
      class="absolute z-30 top-0 left-0 size-[35%] md:w-[100px] md:h-[200px] lg:w-[450px] lg:h-[450px] xl:w-[550px] xl:h-[450px]"
      viewBox="0 0 341 508"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle cx="35.5" cy="202.5" r="305.5" fill="#8BDA7D" />
    </svg>
    <svg
      class="absolute z-30 bottom-0 right-0 size-[35%] md:w-[100px] md:h-[200px] lg:w-[450px] lg:h-[450px] xl:w-[550px] xl:h-[450px]"
      viewBox="0 0 405 522"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle cx="305.5" cy="305.5" r="305.5" fill="#F187C5" />
    </svg>
    <ErrorField :errorText="errorTextVal" v-if="showValidationError && BoolButton" />
  </main>
</template>
