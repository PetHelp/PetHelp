import Vue from 'vue'
import VueRouter from 'vue-router'
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
    component: () => import(/* webpackChunkName: "profil" */ '../views/Profile.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "profil" */ '../views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "profil" */ '../views/Register.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
