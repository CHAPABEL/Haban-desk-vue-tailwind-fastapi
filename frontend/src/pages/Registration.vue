<script setup lang="ts">
import LoginSvg from '@/components/JstComponents/LoginSvg.vue'
</script>

<template>
  <main class="w-full flex h-screen items-center justify-center bg-neutral-700">
    <section class="flex flex-col w-[25%] items-center gap-8">
      <span class="text-white text-3xl font-extrabol pb-4">Welcome back!</span>
      <div class="flex flex-col w-full gap-10">
        <div class="relative">
          <label
            class="bg-neutral-700 font-semibold text-white absolute top-[-25px] p-2 left-[30px]"
            >Email</label
          >
          <input
            type="text"
            class="ring-1 ring-white w-full font-extralight text-sm placeholder:text-neutral-400 bg-neutral-700 focus:outline-2 focus:outline-white text-white pt-3 pb-3 pl-4 rounded-4xl"
            placeholder="email@gmail.com"
          />
        </div>
        <div class="relative flex flex-col gap-1">
          <label
            class="bg-neutral-700 font-semibold text-white absolute top-[-25px] p-2 left-[30px]"
            >Password</label
          >
          <input
            type="text"
            class="ring-1 ring-white w-full font-extralight text-sm placeholder:text-neutral-400 bg-neutral-700 focus:outline-2 focus:outline-white text-white pt-3 pb-3 pl-4 rounded-4xl"
            placeholder="Enter your password"
          />
          <a href="#" class="text-[12px] w-[34%] flex text-white font-semibold">
            Forgot Password?
          </a>
        </div>
      </div>
      <button
        class="bg-neutral-200 text-neutral-700 text-xl rounded-4xl font-semibold w-full p-2 hover:bg-neutral-300 cursor-pointer transition-all ease-in-out duration-100"
      >
        Login
      </button>
    </section>
    <LoginSvg />
  </main>
</template>
