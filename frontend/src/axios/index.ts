import axios from 'axios'

const instance = axios.create({
  baseURL: process.env.VUE_APP_BASEURL ?? 'http://localhost:8080/api'
})

export default instance
