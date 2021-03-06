import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import VueFlashMessage from 'vue-flash-message'
import 'bootstrap-vue/dist/bootstrap-vue.js'
// require('vue-flash-message/dist/vue-flash-message.min.css')
import titleMixin from './mixins/title'

Vue.config.productionTip = false

// Vue.use(VueFlashMessage)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.mixin(titleMixin)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
