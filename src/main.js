import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueTimers from 'vue-timers'

Vue.use(VueTimers)

Vue.use(BootstrapVue);

new Vue({
  el: '#app',
  render: h => h(App)
})
