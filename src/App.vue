<template>
  <div id="app" style="background-color: #a8a8a8">
    <app-key></app-key>
  </div>
</template>

<script>
import Keyword from "./components/Home.vue"

export default {
  name: 'app',
  components:{
    appKey: Keyword
  }
}
</script>

<style>

</style>
