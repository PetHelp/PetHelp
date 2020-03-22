import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from '../axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: {
      refresh: null,
      access: null
    }
  },
  mutations: {
    authUser (state, token) {
      state.token.refresh = token.refresh
      state.token.access = token.access
    }
  },
  actions: {
    register ({ commit, dispatch }, authData) {
      axios.post('/register/', {
        name: authData.name,
        email: authData.email,
        password: authData.password
      })
        .then(res => {
          console.log(res)
          dispatch('login', { email: authData.email, password: authData.password })
        })
        .catch(error => console.log(error))
    },
    login ({ commit, dispatch }, authData) {
      axios.post('/token/', {
        email: authData.email,
        password: authData.password
      })
        .then(res => {
          console.log(res)
          commit('authUser', {
            refreshToken: res.data.refresh,
            accessToken: res.data.access
          })
          localStorage.setItem('refreshToken', res.data.refresh)
          localStorage.setItem('accessToken', res.data.access)
          //flash('Du wurdest erfolgreich angemeldet', 'success')
          router.replace('/profil')
        })
        .catch(error => console.log(error))
    },
    logout ({ commit }) {
      commit('clearAuthData')
      localStorage.removeItem('refreshToken')
      localStorage.removeItem('accessToken')
      router.replace('/')
    }
  },
  modules: {
  }
})
