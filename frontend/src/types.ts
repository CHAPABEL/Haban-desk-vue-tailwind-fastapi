export interface Task {
  text_id: number
  date_value: string
  text_value: string
}

export interface ColumnType {
  task_id?: number
  task_name: string
  task_value: Task[]
}

export interface UserTask {
  task_data: ColumnType[]
}
