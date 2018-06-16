<template>
  <div id="app">
    <app-key></app-key>
  </div>
</template>

<script>
import Password from "./components/Password.vue"
import Keyword from "./components/Keyword.vue"

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components:{
    appPassword: Password,
    appKey: Keyword
  }
}
</script>

<style>

</style>
