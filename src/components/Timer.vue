<template>
  <div>
    <p id="timetime">{{ timeout }}</p>
  </div>
</template>

<script>
export default {
  props: {
    duration: {
      type: Number,
      description: 'Timer duration in seconds',
      default: 30
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      timeout: this.duration,
      enabled: !this.disabled
    }
  },
  computed: {
    isEnabled () {
      return this.enabled && !this.disabled
    }
  },
  methods: {
    start () {
      this.timeout = this.duration
      this.enabled = true
      this.elapse()
    },
    elapse () {
      setTimeout(
        () => {
          if (this.isEnabled) {
            if (this.timeout === 0) {
              this.enabled = false
              this.$emit('timeout')
            } else {
              this.timeout -= 1
              this.elapse()
            }
          }
        },
        1000
      )
    },
    stop () {
      this.enabled = false
    },
    again () {
      if (this.enabled === false) {
        this.enabled = true
        this.elapse()
      }
    }
  }
}
</script>

<style scoped>
.row {
    margin-top: 40px;
}
#timetime {
    font-size: 50px;
    margin-right: -10px;
}
.point {
    background:black;
    width:30%;
    height:30px;
}
#startgame {
    background-color: #ef4343;
    color: white;
}
#resetgame {
    background-color: #ef4343;
    color: white;
}
.gamebuttons {
    background-color: #ef4343;
    color: white;
}
.goodpoint {
    color: green;
    background-color: green;
}
</style>
