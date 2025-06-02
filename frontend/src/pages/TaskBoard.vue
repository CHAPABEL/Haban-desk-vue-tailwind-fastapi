<script setup lang="ts">
import { onMounted, ref } from 'vue'
import MessageField from '@/components/MnComponents/MessageField.vue'
import { computed, reactive } from 'vue'
import type { ColumnType, UserTask } from '@/types.ts'
import MenuSection from '../components/MnComponents/MenuSection.vue'
import NavBar from '@/components/JstComponents/NavBar.vue'
import Tasks from '@/components/MnComponents/Tasks.vue'
const visible = ref(false)
const columns = ref<ColumnType[]>([])
import { authFetch } from '@/api/api'

async function loadTasks() {
  try {
    const data = await authFetch('http://127.0.0.1:8000/tasks/', {
      method: 'GET',
    })
    console.log('Loaded tasks:', data.tasks)
    columns.value = data.tasks.map((item: UserTask) => item.task_data).flat()
  } catch (error: any) {
    console.log(error)
  }
}

onMounted(() => {
  loadTasks()
})

function prePaylad() {
  return {
    task_data: columns.value.map((column) => ({
      task_id: column.task_id,
      task_name: column.task_name,
      task_value: column.task_value.map((task) => ({
        text_id: task.text_id,
        date_value: task.date_value,
        text_value: task.text_value,
      })),
    })),
  }
}

async function pushTaskData() {
  const token = localStorage.getItem('access-token')
  const payload = prePaylad()
  try {
    console.log('Payload to send:', JSON.stringify(payload, null, 2))
    const response = await fetch('http://127.0.0.1:8000/tasks/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(payload),
    })
    const data = await response.json()
    if (!response.ok) {
      console.error('Validation error:', data)
      return
    }

    visible.value = true
    setTimeout(() => {
      visible.value = false
    }, 2000)

    console.log('Success:', data)
  } catch (error) {
    console.error('Fetch error:', error)
  }
}
</script>

<template>
  <main class="w-full flex h-screen flex-row">
    <MenuSection @saveTaskData="pushTaskData" />
    <section class="bg-neutral-600 w-[85%] p-8 flex flex-col h-full gap-7 pt-7">
      <NavBar />
      <Tasks :modelValue="columns" @updateData="columns = $event" />
    </section>
    <MessageField v-if="visible" :message="'Изменения сохранены'" />
  </main>
</template>
