<template>
  <div class="hello">
    <div v-if="entries.length">

      <span v-for="(entry, index) in entries" :key="index" @click="nextHandler(index)" >{{ entry.checked ? '1' : '0'}}</span>
      <input type="text" disabled :value="entries[index].word" />
      <span v-if="finished">{{ lost ? 'lost' : 'won' }}</span>
      <span v-else>you have 30s to find the words</span>
      <button @click="nextHandler()" :disabled="finished || index === 4">next</button>
      <button @click="foundHandler()" :disabled="finished || entries[index].checked">found</button>
    </div>
    <button v-if="!playing" @click="startHandler">{{ `${entries.length ? 're' : ''}start` }}</button>
  </div>
</template>

<script>
const words = ['bilbon', 'test', 'kwak', 'fifou', 'brochette']

export default {
  name: 'Password',
  props: {
    words: {
      type: Array,
      default: () => words
    }
  },
  data () {
    return {
      entries: [],
      timer: false,
      playing: false,
      index: 0
    }
  },
  computed: {
    step () {
      if (this.playing) {
        return 'next'
      } else {
        if (this.entries.length) {
          return 'restart'
        }
        return 'start'
      }
    },
    finished () {
      return this.won || this.lost
    },
    won () {
      return this.entries.every(entry => entry.checked)
    },
    lost () {
      return !this.timer
    }
  },
  watch: {
    index (val) {
      this.index = Math.min(this.entries.length - 1, val)
    }
  },
  methods: {
    nextHandler (index) {
      if (index !== undefined) {
        if (this.entries[index].checked) {
          return
        }
      }
      this.index = index === undefined ? (this.index + 1) : index
    },
    foundHandler () {
      this.entries[this.index].checked = true
      this.index = this.index + 1
      this.playing = !this.won
    },
    startHandler () {
      this.entries = Object.assign([], this.words.map(
        word => ({
          word,
          checked: false
        })
      ))
      this.index = 0
      this.timer = true
      this.playing = true
      setTimeout(() => {
        if (!this.won) {
          this.timer = false
          this.playing = false
        }
      }, 30000)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
