<template>
  <div>
    <md-dialog-alert
      style="background-color: #616161; color: white;"
      :md-active.sync="second"
      md-content="
        - 3 essais par mot de passe pour le faire deviner<br />
        - Pas d'indice de la même racine/famille<br />
        - Les indices ne doivent pas commencer par la même syllabe<br />
        - Mots composés interdits<br />
        - Dire le mot à faire deviner<br />
        - Verbes pronominaux<br />
        - Traduction dans une langue étrangère<br />
        - Ne pas mimer/toucher/montrer<br />
        - Pas de découpage (example : Mot de passe : Bonjour, ne pas faire 'Bon' puis 'Jour')<br />
        - Ne pas retrouver le mot à faire deviner dans le mot indice (exemple : Mot de passe : Homo, ne pas dire 'Homogène')<br />
        - Pas d'acronymes, abréviations, marques.
      "
      md-confirm-text="Compris"
    />
    <md-toolbar class="md-accent changecolor" md-elevation="1" style="background-color: #ef4343; color: white;">
      <a href="." style="flex: 1; color: white;"><h3 class="md-title" style="flex: 1">KeyWord</h3></a>
      <md-button style="color: white;" @click="refresh" data-intro="Rafraichir la page ?">Rafraîchir</md-button>
      <md-button class="md-primary" style="color: white;" @click="second = true" data-intro="voir les règles du jeu" data-highlightClass="text-color: black">Règles du jeu</md-button>
      <md-button class="md-primary" style="color: white;" @click="help" data-intro="Tu viens de cliquer dessus !">Aide</md-button>
    </md-toolbar>

    <div class="container">
      <div class="row text-center">
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinred" @click="changeColorRed" data-intro="Changer la couleur du site et du jeu en rouge">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #ef4343">Site en rouge!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinblue" @click="changeColorBlue" data-intro="Changer la couleur du site et du jeu en bleu">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #2980b9">Site en bleu!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putingreen" @click="changeColorGreen" data-intro="Changer la couleur du site et du jeu en vert">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #27ae60">Site en vert!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinorange" @click="changeColorOrange" data-intro="Changer la couleur du site et du jeu en orange">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #d35400">Site en orange!</md-tooltip>
          </md-button>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 text-center">
          <md-button class="col-lg-12 col-md-12 col-sm-12" style="color: white; font-size: 30px;" id="showshow" @click="allowContent">
            {{ this.showContent ? 'Arrêter' : 'Jouer' }}
          </md-button>
        </div>
      </div>
    </div>

    <div class="container" v-if="showContent" style="background-color: #ecf0f1; margin-top: 20px; margin-bottom: 500px;">
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
              <md-button class="md-icon-button md-accent gamebuttons changecolor" @click="nextWord" :disabled="!playing">✓</md-button>
            </div>
            <div class="col-sm-3 col-lg-1 col-md-3">
              <md-button class="md-icon-button md-accent gamebuttons changecolor" @click="failed" :disabled="!playing">X</md-button>
            </div>
            <div class="col-sm-3 col-lg-1 col-md-3">
              <md-button class="md-icon-button md-accent gamebuttons changecolor" @click="idk" :disabled="!playing">>></md-button>
            </div>
            <div class="col-sm-3 col-lg-2 col-md-3 offset-lg-7">
              <md-button class="md-raised md-accent changecolor" @click="start()" id="startgame" :disabled="playing">Start</md-button>
            </div>
          </div>
          <div class="row text-center" style="margin-top: 130px;">
            <div
              v-for="(step, index) in steps"
              :key="step.value"
              class="col-sm-2 col-lg-2 col-md-2 text-center"
              @click="select(index)"
            >
              <div class="point text-center" :style="step.found ? 'backgroundColor: green' : ''" />
            </div>
          </div>
          <div class="row text-center" style=" margin-bottom: 50px;">
            <div class="col-sm-12 col-lg-12 col-md-12 text-center">
              <h3 style="margin-bottom: 30px;" id="keymdp" v-if="steps.length">{{ steps[this.currentIndex].value }}</h3>
            </div>
          </div>
        </div>
      </div>
      <md-dialog-confirm
        style="background-color: white;"
        :md-active.sync="lost"
        md-content="
          Tu as perdu!<br>
          Retente ta chance!
        "
        md-confirm-text="Go!"
        :md-cancel-text="null"
        @md-confirm="start()"
      />
      <md-dialog-confirm
        style="background-color: white;"
        :md-active.sync="won"
        md-content="
          Tu as gagné!<br>
          Essaye de battre ton record!
        "
        md-confirm-text="Go!"
        :md-cancel-text="null"
        @md-confirm="start()"
      />
    </div>
  </div>
</template>

<script>
import Motsdepasses from './liste_francais'
import introJs from 'intro.js'

import 'intro.js/introjs.css'

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
      playing: false,
      introJs
    }
  },
  computed: {
    won () {
      return this.steps.length && this.steps.every(step => step.found)
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
    },
    help () {
      const options = {
        nextLabel: 'suivant',
        prevLabel: 'précédent',
        doneLabel: 'terminer',
        skipLabel: 'terminer',
        overlayOpacity: 1,
        highlightClass: 'color: black',
        tooltipClass: 'color: black'
      }
      const result = introJs()
      Object.entries(options).forEach(
        ([name, value]) => result.setOption(name, value)
      )
      result.start()
      return result
    },
    changeColorBlue(){
      this.showContent = true;
      const Colors = document.getElementsByClassName("changecolor");
      Colors[0].style.backgroundColor = "#2980b9"
      Colors[1].style.backgroundColor = "#2980b9"
      Colors[2].style.backgroundColor = "#2980b9"
      Colors[3].style.backgroundColor = "#2980b9"
      Colors[4].style.backgroundColor = "#2980b9"
    },
    changeColorGreen(){
      this.showContent = true;
      const Colors = document.getElementsByClassName("changecolor");
      Colors[0].style.backgroundColor = "#27ae60"
      Colors[1].style.backgroundColor = "#27ae60"
      Colors[2].style.backgroundColor = "#27ae60"
      Colors[3].style.backgroundColor = "#27ae60"
      Colors[4].style.backgroundColor = "#27ae60"
    },
    changeColorRed(){
      this.showContent = true;
      const Colors = document.getElementsByClassName("changecolor");
      Colors[0].style.backgroundColor = "#ef4343"
      Colors[1].style.backgroundColor = "#ef4343"
      Colors[2].style.backgroundColor = "#ef4343"
      Colors[3].style.backgroundColor = "#ef4343"
      Colors[4].style.backgroundColor = "#ef4343"
    },
    changeColorOrange(){
      this.showContent = true;
      const Colors = document.getElementsByClassName("changecolor");
      Colors[0].style.backgroundColor = "#d35400"
      Colors[1].style.backgroundColor = "#d35400"
      Colors[2].style.backgroundColor = "#d35400"
      Colors[3].style.backgroundColor = "#d35400"
      Colors[4].style.backgroundColor = "#d35400"
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
a{
  text-decoration: none;
  border: none;
  font-color: white;
}
a:hover{
  text-decoration: none;
  border: none;
  font-color: white;
}
a:visited{
  text-decoration: none;
  border: none;
  font-color: white;
}
#putinred{
  color: #ef4343;
  background: #ef4343;
}
#putinblue{
  color: #2980b9;
  background: #2980b9;
}
#putingreen{
  color: #27ae60;
  background: #27ae60;
}
#putinorange{
  color: #d35400;
  background: #d35400;
}
</style>
