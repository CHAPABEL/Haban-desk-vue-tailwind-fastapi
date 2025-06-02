<script setup lang="ts">
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import LoginSvg from '@/components/JstComponents/LoginSvg.vue'
import LoginApi from '@/components/JstComponents/LoginApi.vue'
import PasInput from '@/components/JstComponents/PasInput.vue'
import ErrorField from '@/components/MnComponents/ErrorField.vue'
const router = useRouter()
const ShowError = ref(false)
const errorTextVal = ref('')
const errorSyle = ref('border-white')

const userLogin = reactive({
  user_email: '',
  user_password: '',
})
const errorValue = ref('')
const BoolButton = ref(false)

async function checkSpaceVal() {
  BoolButton.value = true
  if (userLogin.user_email.trim() === '' || userLogin.user_password.trim() === '') {
    ShowError.value = true
    errorSyle.value = 'border-red-400'
    errorTextVal.value = 'Пустые поля'
    return
  }
  try {
    const response = await fetch('http://127.0.0.1:8000/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_email: userLogin.user_email,
        user_password: userLogin.user_password,
      }),
    })
    const data = await response.json()
    if (response.status === 422 || response.status === 400) {
      ShowError.value = true
      errorSyle.value = 'border-red-400'
      errorTextVal.value = 'Неправильно введены данные'
    }

    if (response.ok) {
      console.log('Успешный логин')
      console.log(data)
      if (data.access_token) {
        localStorage.setItem('access-token', data.access_token)
        router.push('/tasks')
      }
    } else {
      console.log('ошибка логина', data)
    }
  } catch (error) {
    console.error('Ошибка сети:', error)
    alert('Ошибка соединения с сервером')
  }
}

function pasErrorFunction() {}
</script>

<template>
  <main class="w-full flex h-screen items-center justify-center bg-neutral-700">
    <section class="flex flex-col w-[25%] items-center gap-8">
      <span class="text-white text-3xl font-extrabold pb-4">Welcome back!</span>
      <div class="flex flex-col w-full gap-7">
        <PasInput
          text="Email"
          type="text"
          :wrapperClass="errorSyle"
          :errorText="'text-white'"
          v-model="userLogin.user_email"
          :placeholder="'Enter your Email'"
          :ShowSvg="false"
        />
        <PasInput
          text="Password"
          v-model="userLogin.user_password"
          :wrapperClass="errorSyle"
          :errorText="'text-white'"
          :placeholder="'Enter your Password'"
          :ShowSvg="true"
          :ShowForgot="true"
        />
      </div>
      <div class="flex flex-col w-full items-center gap-5">
        <button
          @click="checkSpaceVal"
          class="bg-neutral-200 text-black text-lg rounded-4xl font-semibold w-full p-2 hover:bg-neutral-300 cursor-pointer transition-all ease-in-out duration-100"
        >
          Login
        </button>
        <span class="text-neutral-500">- or -</span>
        <LoginApi />
        <div class="flex gap-2 pt-2">
          <span class="text-sm font-extralight text-neutral-400">Don’t have an account?</span>
          <router-link to="/reg" class="text-sm font-extralight text-green-400 hover:text-green-500"
            >Sign up!</router-link
          >
        </div>
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
    <ErrorField :errorText="errorTextVal" v-if="ShowError" />
  </main>
</template>
