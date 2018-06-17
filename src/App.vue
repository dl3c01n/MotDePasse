<template>
  <div id="app" style="background-color: #a8a8a8">
    <app-navbar></app-navbar>
    <app-key></app-key>
  </div>
</template>

<script>
import Password from "./components/Password.vue"
import Keyword from "./components/Keyword.vue"
import Navbar from "./components/Navbar.vue"

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components:{
    appPassword: Password,
    appKey: Keyword,
    appNavbar: Navbar
  }
}
</script>

<style>

</style>
