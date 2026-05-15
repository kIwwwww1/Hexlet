// Уменьшение энергии пользователя
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

// Повышение энергии пользователя
export const addUserEnergy = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/v1/users/add-energy', {
      method: 'PATCH',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      }
    })

    if (response.ok) {
      const data = await response.text()
      console.log('Энергия успешно добавлена (ответ сервера):', data)

      return Number(data)
      
    } else {
      console.error('Ошибка сервера при добавлении энергии:', response.status)
      throw new Error(`Ошибка сервера: ${response.status}`)
    }
  } catch (error) {
    console.error('Сетевая ошибка при запросе add-energy:', error)
    throw error 
  }
}
