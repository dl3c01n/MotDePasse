<template>
  <div id="app" style="background-color: #a8a8a8">
    <app-key />
    <app-footer style="width: 100%" />
  </div>
</template>

<script>
import Keyword from "./components/Home.vue"
import Footer from "./components/Footer.vue"

export default {
  name: 'app',
  components:{
    appKey: Keyword,
    appFooter: Footer
  }
}
</script>

<style>

</style>
