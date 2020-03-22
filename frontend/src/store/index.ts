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
    },
    profile: {
      id: null,
      name: null,
      bio: null,
      address: null,
      emergencyContactEmail: null,
      animals: {}
    }
  },
  mutations: {
    authUser (state, token) {
      state.token.refresh = token.refresh
      state.token.access = token.access
    },
    storeProfile (state, profile) {
      state.profile.id = profile.id
      state.profile.name = profile.name
      state.profile.bio = profile.bio
      state.profile.address = profile.address
      state.profile.emergencyContactEmail = profile.emergencyContactEmail
    }
  },
  actions: {
    register ({ dispatch }, authData) {
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
    login ({ commit }, authData) {
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
    },
    getProfile ({ commit }) {
      axios.get('/users/')
        .then(res => {
          console.log(res)
          commit('storeProfile', {
            id: res.data[0].id,
            name: res.data[0].name,
            bio: res.data[0].bio,
            address: res.data[0].address,
            emergencyContactEmail: res.data[0].emergencyContactEmail
          })
        })
        .catch(error => console.log(error))
    },
    updateProfile ({ commit }, profile) {
      axios.patch(`/users/${profile.id}/`, {
        name: profile.name,
        bio: profile.bio,
        address: profile.address,
        emergencyContactEmail: profile.emergencyContactEmail
      })
        .then(res => {
          console.log(res)
          commit('storeProfile', {
            name: profile.name,
            bio: profile.bio,
            address: profile.address,
            emergencyContactEmail: profile.emergencyContactEmail
          })
        })
        .catch(error => console.log(error))
    }
  },
  modules: {
  }
})
