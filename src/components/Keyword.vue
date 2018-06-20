<template>
  <div>
    <md-dialog-alert
      style="background-color: white;"
      :md-active.sync="second"
      md-content="
        -3 essais par mot de passe pour le faire deviner<br>
        -Pas d'indice de la même racine/famille<br>
        -Les indices ne doivent pas commencer par la même syllabe<br>
        -Mots composés interdits<br>
        -Dire le mot à faire deviner<br>
        -Verbes pronominaux<br>
        -Traduction dans une langue étrangère<br>
        -Ne pas mimer/toucher/montrer<br>
        -Pas de découpage (example : Mot de passe : Bonjour, ne pas faire 'Bon' puis 'Jour')<br>
        -Ne pas retrouver le mot à faire deviner dans le mot indice (exemple : Mot de passe : Homo, ne pas dire 'Homogène')<br>
        -Pas d'acronymes, abréviations, marques.
      "
      md-confirm-text="Compris"
    />
    <md-toolbar class="md-accent" md-elevation="1" style="background-color: #ef4343; color: white;">
      <h3 class="md-title" style="flex: 1">KeyWord</h3>
      <md-button style="color: white;" @click="refresh">Rafraîchir</md-button>
      <md-button class="md-primary" style="color: white;" @click="second = true">Règles du jeu</md-button>
    </md-toolbar>
    <div class="container">
      <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 text-center">
          <md-button class="col-lg-12 col-md-12 col-sm-12" style="color: white;" id="showshow" @click="allowContent">
            {{ this.showContent ? 'Arrêter' : 'Jouer' }}
          </md-button>
        </div>
      </div>
    </div>

    <div class="container" v-if="showContent" style="border: 5px solid red; background-color: white; margin-top: 20px; margin-bottom: 30px;">
      <div class="row">
        <div class="col-sm-12 col-lg-8 col-md-10 offset-lg-2 offset-md-1">
          <div class="row  text-center">
            <div class="col-sm-12 col-lg-12 col-md-10 text-center">
              <h1 style="font-weight: bold; text-transform: uppercase; margin-top: -30px;">{{ welcome }}</h1>
            </div>
          </div>
          <div class="row text-center">
            <div class="col-sm-12 col-lg-3 col-md-10">
              <p id="timetime">{{ count }}</p>
            </div>
          </div>
          <div class="row">
            <div class="col-sm-3 col-lg-1 col-md-3">
              <md-button class="md-icon-button md-accent gamebuttons" @click="nextWord" :disabled="!playing">✓</md-button>
            </div>
            <div class="col-sm-3 col-lg-1 col-md-3">
              <md-button class="md-icon-button md-accent gamebuttons" @click="failed" :disabled="!playing">X</md-button>
            </div>
            <div class="col-sm-3 col-lg-1 col-md-3">
              <md-button class="md-icon-button md-accent gamebuttons" @click="idk" :disabled="!playing">>></md-button>
            </div>
            <div class="col-sm-3 col-lg-2 col-md-3 offset-lg-7">
              <md-button class="md-raised md-accent" @click="start()" id="startgame">Start</md-button>
            </div>
          </div>
          <div class="row text-center" style="margin-top: 130px;">
            <div
              v-for="(step, index) in steps"
              :key="step.value"
              class="col-sm-2 col-lg-2 offset-lg-1 col-md-2 offset-md-1 text-center"
              @click="select(index)"
            >
              <div class="point" :style="step.found ? 'backgroundColor: green' : ''" />
            </div>
          </div>
          <div class="row text-center" style=" margin-bottom: 50px;">
            <div class="col-sm-12 col-lg-12 col-md-12">
              <h3 style="margin-bottom: 30px;" id="keymdp" v-if="steps.length">{{ steps[this.currentIndex].value }}</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Motsdepasses from './liste_francais'

const getRandomInt = max => Math.floor(Math.random() * Math.floor(max))

export default {
  data () {
    return {
      welcome: "Mot De Passe",
      Motsdepasses,
      count: 30,
      steps: [],
      currentIndex: 0,
      second: false,
      showContent: false,
      playing: false
    }
  },
  computed: {
    won () {
      return this.steps.every(step => step.found)
    },
    lost () {
      return this.count === 0
    }
  },
  methods: {
    select (index) {
      if (! this.steps[index].found) {
        this.currentIndex = index
      }
    },
    nextWord() {
      this.steps[this.currentIndex].found = true
      if (!this.won) {
        for (let index = this.currentIndex; index < this.steps.length; index++) {
          if (!this.steps[index].found) {
            this.currentIndex = index
            break
          }
        }
        if (this.steps[this.currentIndex].found) {
          for (let index = 0; index < this.currentIndex; index++) {
            if (!this.steps[index].found) {
              this.currentIndex = index
              break
            }
          }
        }
      } else {
        this.playing = false
      }
    },
    failed (){
      this.currentIndex = (this.currentIndex + 1) % this.steps.length
    },
    idk (){
      this.currentIndex = (this.currentIndex + 1) % this.steps.length
    },
    countDown () {
      setTimeout(() => {
        if (this.playing) {
          this.count -= 1
          if (this.count > 0 && this.playing) {
              this.countDown()
          } else {
            this.playing = false
          }
        }
      }, 1000)
    },
    start (n = 5) {
      this.steps = Object.assign(
        [],
        new Array(n).fill().map(
          (_, index) => ({
            value: Motsdepasses[getRandomInt(Motsdepasses.length)],
            found: false
          })
        )
      )
      this.currentIndex = 0
      this.count = 30
      this.playing = true
      this.countDown()
    },
    refresh(){
      location.reload();
    },
    allowContent() {
      this.showContent = !this.showContent
      if (!this.showContent) {
        this.playing = false
      }
    }
  }
}
</script>

<style scoped>
.row{
    margin-top: 40px;
}
#timetime{
    font-size: 50px;
    margin-right: -10px;
}
.point{
    background:black;
    width:30%;
    height:30px;
}
#startgame{
    background-color: #ef4343;
    color: white;
}
#resetgame{
    background-color: #ef4343;
    color: white;
}
.gamebuttons{
    background-color: #ef4343;
    color: white;
}
.goodpoint{
    color: green;
    background-color: green;
}
</style>
