export const reduceUserEnergy = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/users/reduce-energy', {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      }
    })

    if (response.ok) {
      const data = await response.json()
      console.log('Энергия успешно уменьшена:', data)
      return data
    } else {
      console.error('Ошибка сервера при уменьшении энергии:', response.status)
      throw new Error(`Ошибка сервера: ${response.status}`)
    }
  } catch (error) {
    console.error('Сетевая ошибка при запросе reduce-energy:', error)
    throw error 
  }
}
