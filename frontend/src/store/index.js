import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'
import axios from '../axios'

Vue.use(Vuex)

/* const messageOptions = {
  timeout: 8000,
  important: true,
  clickable: true,
  autoEmit: true
} */

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
      animals: []
    },
    masterdata: {
      animalTypes: [],
      helpTypes: []
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
    },
    storeAnimals (state, animals) {
      state.profile.animals = animals
    },
    addAnimal (state, animal) {
      state.profile.animals.push(animal)
    },
    updateAnimal (state, animal) {
      for (var i in state.profile.animals) {
        if (state.profile.animals[i].id === animal.id) {
          state.profile.animals[i] = animal
          break
        }
      }
    },
    deleteAnimal (state, animalId) {
      state.profile.animals = state.profile.animals.filter(a => a.id !== animalId)
    },
    storeAnimalTypes (state, types) {
      state.masterdata.animalTypes = types
    },
    storeHelpTypes (state, types) {
      state.masterdata.helpTypes = types
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
        .catch(error => {
          // Vue.prototype.$flashStorage.flash('Die E-Mail-Adresse ist bereits vergeben', 'error', messageOptions)
          console.log(error)
        })
    },
    login ({ commit, dispatch }, authData) {
      axios.post('/token/', {
        email: authData.email,
        password: authData.password
      })
        .then(res => {
          commit('authUser', {
            refresh: res.data.refresh,
            access: res.data.access
          })
          localStorage.setItem('refreshToken', res.data.refresh)
          localStorage.setItem('accessToken', res.data.access)
          // Vue.prototype.$flashStorage.flash('Du wurdest erfolgreich angemeldet', 'success', messageOptions)
          dispatch('getProfile')
          router.replace('/profil')
        })
        .catch(error => {
          // Vue.prototype.$flashStorage.flash('Deine eingegebenen Anmeldedaten sind nicht korrekt', 'error', messageOptions)
          console.log(error)
        })
    },
    attemptLogin ({ commit }) {
      const refreshToken = localStorage.getItem('refreshToken')
      const accessToken = localStorage.getItem('accessToken')
      if (refreshToken && accessToken) {
        // At a later point check if token is still valid
        commit('authUser', {
          refresh: refreshToken,
          access: accessToken
        })
      }
    },
    refreshToken ({ state, commit }) {
      axios.post('/token/refresh', {
        refresh: state.token.refresh
      })
        .then(res => {
          console.log(res)
          commit('authUser', {
            refresh: res.data.refresh,
            access: res.data.access
          })
        })
        .catch(error => console.log(error))
    },
    logout ({ commit }) {
      commit('clearAuthData')
      localStorage.removeItem('refreshToken')
      localStorage.removeItem('accessToken')
      // Vue.prototype.$flashStorage.flash('Du wurdest erfolgreich abgemeldet', 'success', messageOptions)
      router.replace('/')
    },
    getProfile ({ commit, getters }) {
      axios.get('/users/', getters.axiosConfig)
        .then(res => {
          console.log(res)
          const data = res.data[0]
          commit('storeProfile', {
            id: data.id,
            name: data.name,
            bio: data.bio,
            address: data.address,
            emergencyContactEmail: data.emergency_contact_email
          })
        })
        .catch(error => console.log(error))
    },
    updateProfile ({ commit, getters }, profile) {
      axios.patch(`/users/${profile.id}/`, {
        name: profile.name,
        bio: profile.bio,
        address: profile.address,
        emergency_contact_email: profile.emergencyContactEmail
      }, getters.axiosConfig)
        .then(res => {
          console.log(res)
          commit('storeProfile', {
            id: profile.id,
            name: profile.name,
            bio: profile.bio,
            address: profile.address,
            emergencyContactEmail: profile.emergencyContactEmail
          })
        })
        .catch(error => console.log(error))
    },
    getAnimals ({ commit, getters }) {
      axios.get('/animals/', getters.axiosConfig)
        .then(res => {
          console.log(res)
          commit('storeAnimals', res.data)
        })
        .catch(error => console.log(error))
    },
    createAnimal ({ commit, getters }, animal) {
      axios.post('/animals/', {
        type: 'DOG',
        name: animal.name,
        image: null,
        description: animal.description,
        care_person: null
      }, getters.axiosConfig)
        .then(res => {
          console.log(res)
          commit('addAnimal', res.data)
          router.replace('/profil')
        })
        .catch(error => console.log(error))
    },
    updateAnimal ({ commit, getters }, animal) {
      axios.put(`/animals/${animal.id}/`, {
        type: animal.type,
        name: animal.name,
        image: animal.image,
        description: animal.description,
        care_person: animal.care_person
      }, getters.axiosConfig)
        .then(res => {
          console.log(res)
          commit('updateAnimal', res.data)
          router.replace('/profil')
        })
        .catch(error => console.log(error))
    },
    deleteAnimal ({ commit, getters }, animalId) {
      axios.delete(`/animals/${animalId}/`, getters.axiosConfig)
        .then(res => {
          console.log(res)
          commit('deleteAnimal', animalId)
        })
        .catch(error => console.log(error))
    },
    getMasterData ({ dispatch }) {
      dispatch('getAnimalTypes')
      dispatch('getHelpTypes')
    },
    getAnimalTypes ({ commit }) {
      axios.get('/animal-types/')
        .then(res => {
          console.log(res)
          commit('storeAnimalTypes', res.data)
        })
        .catch(error => console.log(error))
    },
    getHelpTypes ({ commit }) {
      axios.get('/help-types/')
        .then(res => {
          console.log(res)
          commit('storeHelpTypes', res.data)
        })
        .catch(error => console.log(error))
    }
  },
  getters: {
    axiosConfig (state) {
      return {
        headers: {
          Authorization: `Bearer ${state.token.access}`
        }
      }
    },
    isAuthenticated (state) {
      return state.token.access !== null
    },
    getAnimalById: (state) => (id) => {
      return state.profile.animals.find(a => parseInt(a.id) === parseInt(id))
    }
  },
  modules: {
  }
})
