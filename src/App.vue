<template>
  <div id="app" style="background-color: #a8a8a8">
    <app-key></app-key>
  </div>
</template>

<script>
import Keyword from "./components/Keyword.vue"

export default {
  name: 'app',
  data () {
    return {

    }
  },
  components:{
    appKey: Keyword
  }
}
</script>

<style>

</style>
