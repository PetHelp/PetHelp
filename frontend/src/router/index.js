import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/hilfe-suchen',
    name: 'search-help',
    component: () => import(/* webpackChunkName: "hilfe-suchen" */ '../views/SearchHelp.vue')
  },
  {
    path: '/hilfe-anbieten',
    name: 'offer-help',
    component: () => import(/* webpackChunkName: "hilfe-anbieten" */ '../views/OfferHelp.vue')
  },
  {
    path: '/guideline',
    name: 'guideline',
    component: () => import(/* webpackChunkName: "guideline" */ '../views/Guideline.vue')
  },
  {
    path: '/faq',
    name: 'faq',
    component: () => import(/* webpackChunkName: "faq" */ '../views/Faq.vue')
  },
  {
    path: '/profil',
    name: 'profile',
    component: () => import(/* webpackChunkName: "profile" */ '../views/Profile.vue')
    /* beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next()
      } else {
        next('/login')
      }
    }, */
  },
  {
    path: '/profil/haustier/add',
    name: 'addPet',
    component: () => import(/* webpackChunkName: "addPet" */ '../views/AddAnimal.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
    /* beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next('/profile')
      } else {
        next()
      }
    } */
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "register" */ '../views/Register.vue')
    /* beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next('/profile')
      } else {
        next()
      }
    } */
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
