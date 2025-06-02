import router from '@/router'

export async function authFetch(url: string, options: RequestInit = {}) {
  const token = localStorage.getItem('access-token')
  const headers = {
    ...options.headers,
    'Content-Type': 'application/json',
    Authorization: token ? `Bearer ${token}` : '',
  }

  const response = await fetch(url, {
    ...options,
    headers,
  })

  if (!response.ok) {
    if (response.status == 401) {
      localStorage.removeItem('access-token')
      router.push('/')
    }
    const errorData = await response.json()
    throw new Error(errorData.detail || 'Ошибка запроса')
  }

  return response.json()
}
