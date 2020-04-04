import axios from 'axios'

import router from '../router'
import store from '../store'

const instance = axios.create({
  baseURL: process.env.VUE_APP_BASEURL ?? 'http://localhost:8001/api'
})

instance.interceptors.response.use((response) => {
  return response
}, function (error) {
  const originalRequest = error.config

  if (error.response.status === 401 && originalRequest.url.includes('refresh')) {
    router.replace('/login')
    return Promise.reject(error)
  }

  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true
    const refreshToken = localStorage.getItem('refreshToken')
    return instance.post('/token/refresh/', { refresh: refreshToken })
      .then(res => {
        if (res.status === 200) {
          localStorage.setItem('refreshToken', res.data.refresh)
          localStorage.setItem('accessToken', res.data.access)
          store.commit('authUser', {
            refresh: res.data.refresh,
            access: res.data.access
          })
          originalRequest.headers.Authorization = 'Bearer ' + res.data.access
          console.log(originalRequest)
          return instance(originalRequest)
        }
      })
  }
  return Promise.reject(error)
})

export default instance
