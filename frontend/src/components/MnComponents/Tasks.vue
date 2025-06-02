<script setup lang="ts">
import { ref, defineEmits, defineProps, computed, reactive } from 'vue'
const dateRefCalendar = reactive<Record<number, HTMLInputElement | null>>({})
import type { ColumnType, Task } from '@/types'
import VueDatepicker from 'vue3-datepicker'
const dateRefs = reactive<Record<number, HTMLInputElement | null>>({})
const emit = defineEmits(['updateData', 'removeColumnRequest'])
const props = defineProps<{
  modelValue: ColumnType[]
}>()
const columnData = computed({
  get: () => props.modelValue,
  set: (val) => emit('updateData', val),
})
const nowDate = ref(new Date().toISOString().split('T')[0])
const newTask = ref('')
const dateInput = ref('')
const taskDataArray = ref<Task[]>([])

function autoResize(event: Event) {
  const textarea = event.target as HTMLTextAreaElement
  textarea.style.height = 'auto'
  textarea.style.height = `${textarea.scrollHeight}px`
}

function maxWords(event: Event) {
  const textarea = event.target as HTMLTextAreaElement
  const maxChars = 25
  if (textarea.value.length > maxChars) {
    textarea.value = textarea.value.slice(0, maxChars)
  }
}

function addToTaskList(columnIndex: number) {
  const updated = [...columnData.value]

  if (!Array.isArray(updated[columnIndex].task_value)) {
    updated[columnIndex].task_value = []
  }
  updated[columnIndex].task_value.push({
    text_id: Date.now(),
    date_value: nowDate.value,
    text_value: '',
  })

  columnData.value = updated
  newTask.value = ''
  dateInput.value = ''
}

function createPushData() {
  const updated = [...columnData.value]
  updated.push({
    task_id: Date.now(),
    task_name: 'Задача',
    task_value: [],
  })
  columnData.value = updated
  taskDataArray.value = []
}

function getDateNow(task: Task) {
  const today = new Date()
  const newDateObj = new Date(task.date_value)
  const diffInTime = newDateObj.getTime() - today.getTime()
  const diffInDays = Math.ceil(diffInTime / (1000 * 60 * 60 * 24))
  return {
    'bg-red-400': diffInDays <= 1,
    'bg-amber-400': diffInDays >= 2 && diffInDays < 5,
    'bg-green-400': diffInDays >= 5,
  }
}

function removeTask(columnIndex: number, taskId: number) {
  const updated = [...columnData.value]
  const tasks = updated[columnIndex].task_value
  if (!tasks) return

  updated[columnIndex].task_value = tasks.filter((task) => task.text_id !== taskId)
  columnData.value = updated
}

function removeColumn(columnIndex: number) {
  emit('removeColumnRequest', columnIndex)
}
defineExpose({
  dateRefs,
  columnData,
})
</script>

<template>
  <section
    class="flex overflow-x-auto w-full gap-3 p-2 flex-nowrap custom-scrollbar h-full items-start"
  >
    <div
      v-for="(item, index) in columnData"
      :key="index"
      class="snap-start flex flex-col min-w-[28%] pb-3 p-3 bg-neutral-500 gap-8 transition duration-300 easy-in-out hover:scale-[101%] rounded-lg"
    >
      <div class="flex flex-col gap-2">
        <textarea
          v-model="item.task_name"
          @input="maxWords"
          class="text-base text-white border-b-2 resize-none h-7 focus:ring-0 focus:outline-0 font-medium"
        >
        </textarea>

        <span class="text-sm text-neutral-300 font-medium"
          >Задачи: {{ item.task_value?.length }}</span
        >
      </div>
      <div class="flex gap-3 flex-col">
        <div
          v-for="(task, index) in item.task_value"
          :key="task.text_id"
          :class="getDateNow(task)"
          class="p-2 flex flex-col gap-[10px] rounded-lg"
        >
          <div class="relative">
            <input
              v-model="task.date_value"
              type="date"
              class="appearance-none focus:outline-1 focus:outline-white text-white rounded-md px-2 py-2 pr-10 w-full"
            />
            <button
              @click="removeTask(index, task.text_id)"
              class="w-5 h-5 absolute text-xl right-3 top-1/2 focus:ring-1 focus:outline-0 -translate-y-1/2 text-white cursor-pointer"
            >
              x
            </button>
          </div>

          <div class="flex relative justify-between">
            <textarea
              @input="autoResize($event)"
              rows="1"
              v-model="task.text_value"
              class="text-white form-input text-lg rounded-lg font-light pb-6 focus:ring-1 focus:outline-0 focus:ring-white px-2 py-2 pr-10 w-full placeholder-white focus:outline-none resize-none"
              placeholder="Напишите сюда задачу"
            />
          </div>
        </div>
      </div>
      <button
        @click="(event: MouseEvent) => addToTaskList(index)"
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
</template>
