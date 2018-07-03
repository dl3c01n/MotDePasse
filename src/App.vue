<template>
  <div id="app" style="background-color: #a8a8a8">
    <app-key></app-key>
    <app-foot style="width: 100%"></app-foot>
  </div>
</template>

<script>
import Keyword from "./components/Home.vue"
import Foot from "./components/Foot.vue"

export default {
  name: 'app',
  components:{
    appKey: Keyword,
    appFoot: Foot
  }
}
</script>

<style>

</style>
