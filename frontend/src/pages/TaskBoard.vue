<script setup lang="ts">
import { ref, type Reactive } from 'vue'
import { computed, reactive } from 'vue'
import MenuSection from '../components/MnComponents/MenuSection.vue'
import NavBar from '@/components/JstComponents/NavBar.vue'
const nowDate = ref(new Date().toISOString().split('T')[0])

const columnData = ref<column[]>([])
const newTask = ref('')
const dateInput = ref('')
const taskName = ref('')
const taskDataArray = ref<Task[]>([])

function autoResize(event: Event) {
  const textarea = event.target as HTMLTextAreaElement
  textarea.style.height = 'auto'
  textarea.style.height = `${textarea.scrollHeight}px`
}

const dateRefs = reactive<Record<number, HTMLInputElement | null>>({})
function openDateHeader(taskId: number) {
  const inputRef = dateRefs[taskId]
  if (inputRef) {
    inputRef.click()
  }
  console.log(dateRefs)
}

interface Task {
  id: number
  dateInp: string
  textValue: string
}

interface column {
  taskValue: number
  nameTask: string
  taskData: Task[]
}

function createPushData() {
  columnData.value.push({
    taskValue: Date.now(),
    nameTask: 'Задача',
    taskData: [],
  })
  taskDataArray.value = []
  console.log(columnData.value)
}

function getDateNow(task: Task) {
  const today = new Date()
  const newDate = new Date(task.dateInp)
  const newDateObj = new Date(newDate)
  const diffInTime = newDateObj.getTime() - today.getTime()
  const diffInDays = Math.ceil(diffInTime / (1000 * 60 * 60 * 24))
  console.log('осталось дней:', diffInDays)
  return {
    'bg-red-400': diffInDays <= 1,
    'bg-amber-400': diffInDays >= 2,
    'bg-green-400': diffInDays >= 5,
  }
}

function addToTaskList(columnIndex: number, event: MouseEvent) {
  columnData.value[columnIndex].taskData.push({
    id: Date.now(),
    textValue: '',
    dateInp: nowDate.value,
  })
  newTask.value = ''
  dateInput.value = ''
  console.log(columnData.value[columnIndex].taskData)
}

defineExpose({
  dateRefs,
})
</script>

<template>
  <main class="w-full flex h-screen flex-row">
    <MenuSection />
    <section class="bg-neutral-600 w-[80%] p-8 flex flex-col h-full gap-7 pt-7">
      <NavBar />
      <section
        class="flex overflow-x-auto w-full gap-5 flex-nowrap custom-scrollbar h-full items-start"
      >
        <div
          v-for="(item, index) in columnData"
          :key="index"
          class="snap-start flex flex-col min-w-[27%] pb-3 p-3 bg-neutral-500 gap-8 transition duration-300 easy-in-out hover:scale-[101%] rounded-lg"
        >
          <div class="flex flex-col gap-2">
            <textarea
              v-model="item.nameTask"
              class="text-base text-white siz resize-none h-6 focus:ring-0 focus:outline-0 font-medium"
            >
            </textarea>
            <span class="text-sm text-neutral-300 font-medium"
              >Задачи: {{ item.taskData.length }}</span
            >
          </div>
          <div class="flex gap-3 flex-col">
            <div
              v-for="(task, index) in item.taskData"
              :key="task.id"
              :class="getDateNow(task)"
              class="p-2 flex flex-col gap-[10px] rounded-lg"
            >
              <div class="relative">
                <input
                  v-model="task.dateInp"
                  type="date"
                  class="appearance-none focus:outline-1 focus:outline-white text-white rounded-md px-2 py-2 pr-10 w-full"
                />
                <svg
                  @click="console.log(columnData)"
                  class="w-5 h-5 absolute right-3 top-1/2 focus:ring-1 focus:outline-0 -translate-y-1/2 text-white cursor-pointer"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M8 7V3m8 4V3m-9 8h10m-10 4h6m-6 4h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                  />
                </svg>
              </div>

              <div class="flex relative justify-between">
                <textarea
                  @input="autoResize($event)"
                  rows="1"
                  v-model="task.textValue"
                  class="text-white form-input text-lg rounded-lg font-light pb-6 focus:ring-1 focus:outline-0 focus:ring-white px-2 py-2 pr-10 w-full placeholder-white focus:outline-none resize-none"
                  placeholder="Напишите сюда задачу"
                />
                <!-- <svg
                @click=""
                class="absolute right-2 top-1/3 -translate-y-1/2 text-white cursor-pointer transition-all duration-100 ease-in-out hover:scale-110"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5 15.8633L4 19.9633L8.1 18.9633L17.3 9.76333L14.2 6.66333L5 15.8633ZM5.5 18.9633L5.1 18.4633L5.5 16.4633L7.5 18.4633L5.5 18.9633ZM14.9 8.36333L6.8 16.3633L6.2 15.7633L14.3 7.76333L14.9 8.36333Z"
                  fill="white"
                />
                <path
                  d="M19.3 4.66333C18.2 3.56333 16.7 4.16333 16.7 4.16333L15.2 5.66333L18.3 8.76333L19.8 7.26333C19.8 7.16333 20.4 5.76333 19.3 4.66333V4.66333ZM17.4 5.56333L16.9 5.06333C17.5 4.46333 18 4.96333 18 4.96333L17.4 5.56333Z"
                  fill="white"
                />
              </svg> -->
              </div>
            </div>
          </div>
          <button
            @click="(event) => addToTaskList(index, event)"
            class="bg-none flex items-center gap-2 transition-all rounded-lg justify-center duration-200 ease-in-out hover:bg-neutral-600 text-white"
          >
            <svg
              width="15"
              height="15"
              viewBox="0 0 12 12"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clip-path="url(#clip0_4_500)">
                <path
                  d="M11.6695 5.03846H6.90255V0.230774H4.99577V5.03846H0.228821V6.96155H4.99577V11.7692H6.90255V6.96155H11.6695V5.03846Z"
                  fill="white"
                />
              </g>
              <defs>
                <clipPath id="clip0_4_500">
                  <rect width="11.8983" height="12" fill="white" />
                </clipPath>
              </defs>
            </svg>
            <span>Добавить задачу</span>
          </button>
        </div>
        <button
          @click="createPushData"
          class="bg-none flex min-w-[162px] items-center mt-3 font-extralight gap-2 transition-all justify-center duration-200 ease-in-out hover:shadow-[0px_1px_0px_0px_white] pb-2 text-white"
        >
          <svg
            width="15"
            height="15"
            viewBox="0 0 12 12"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g clip-path="url(#clip0_4_500)">
              <path
                d="M11.6695 5.03846H6.90255V0.230774H4.99577V5.03846H0.228821V6.96155H4.99577V11.7692H6.90255V6.96155H11.6695V5.03846Z"
                fill="white"
              />
            </g>
            <defs>
              <clipPath id="clip0_4_500">
                <rect width="11.8983" height="12" fill="white" />
              </clipPath>
            </defs>
          </svg>
          <span>Добавить Колонку</span>
        </button>
      </section>
    </section>
  </main>
</template>
