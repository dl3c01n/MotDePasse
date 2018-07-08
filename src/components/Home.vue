<template>
  <div>
    <md-dialog-alert
      style="background-color: #616161; color: white;"
      :md-active.sync="showRules"
      md-content="
        KeyWord est un jeu de lettre par équipe de 2 joueurs , où le but est de faire deviner à l'autre joueur un mot en donnant un seul indice en respectant les règles suivants :<br />
        <br />
        - 3 essais par mot de passe pour le faire deviner<br />
        - Pas d'indice de la même racine/famille<br />
        - Les indices ne doivent pas commencer par la même syllabe<br />
        - Mots composés interdits<br />
        - Ne pas dire le mot à faire deviner<br />
        - Pas de verbes pronominaux<br />
        - Pas de traduction dans une langue étrangère<br />
        - Ne pas mimer/toucher/montrer<br />
        - Pas de découpage (example : Mot de passe : Bonjour, ne pas faire 'Bon' puis 'Jour')<br />
        - Ne pas retrouver le mot à faire deviner dans le mot indice (exemple : Mot de passe : Homo, ne pas dire 'Homogène')<br />
        - Pas d'acronymes, abréviations, marques.
      "
      md-confirm-text="Compris"
    />

    <md-toolbar class="md-accent backgroundcolor" md-elevation="1" style="background-color: #ef4343; color: white;">
      <a href="." style="flex: 1; color: white;">
        <h3 class="md-title" style="flex: 1">KeyWord</h3>
      </a>
      <md-button style="color: white;" @click="refresh" data-intro="actualise la page en case de soucis">Rafraîchir</md-button>
      <md-button class="md-primary" style="color: white;" @click="showRules = true" data-intro="affiche les règles du jeu">Règles du jeu</md-button>
      <md-button class="md-primary" style="color: white;" @click="help()">Aide</md-button>
      <a href="mailto:b3j0fs+2hpvlb7u9j07xjq2yzr+2qionn0vdzeqqsd4m31+0ou74vv1s7@boards.trello.com?subject=bug" class="md-primary" style="color: white;" data-intro="signaler un bug">Signaler un problème</a>
    </md-toolbar>

    <div class="container">
      <div class="row text-center" data-intro="changer la couleur du jeu">
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinred" @click="changeColor('#ef4343')" data-intro="Changer la couleur du site et du jeu en rouge">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #ef4343">Site en rouge!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinblue" @click="changeColor('#2980b9')" data-intro="Changer la couleur du site et du jeu en bleu">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #2980b9">Site en bleu!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putingreen" @click="changeColor('#27ae60')" data-intro="Changer la couleur du site et du jeu en vert">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #27ae60">Site en vert!</md-tooltip>
          </md-button>
        </div>
        <div class="col-sm-12 col-md-3 col-lg-3">
          <md-button class="md-icon-button" id="putinorange" @click="changeColor('#d35400')" data-intro="Changer la couleur du site et du jeu en orange">
              <md-icon>home</md-icon>
              <md-tooltip md-direction="top" style="background-color: #323232; color: #d35400">Site en orange!</md-tooltip>
          </md-button>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 text-center">
          <md-button
            v-for="_type in types" :key="_type"
            :class="`${_type === type ? 'md-flat' : 'md-raised'} backgroundcolor`"
            style="background-color: #ef4343;"
            @click="startHandler(_type)"
            >
            {{ _type }}
          </md-button>
        </div>
      </div>
    </div>

    <div class="container bordercolor" style="border: 5px solid red; background-color: white; margin-top: 20px; margin-bottom: 30px;">
      <game
        @won="wonHandler"
        @lost="lostHandler"
        ref="game"
      />
    </div>

    <md-dialog-confirm
      :md-active.sync="final"
      :md-backdrop="true"
      md-title="Vous venez de vous qualifier pour la finale"
      md-confirm-text="Aller en finale !"
      md-cancel-text="Rejouer les qualifications"
      @md-confirm="startHandler('final')"
      @md-cancel="retry()"
      :md-close-on-esc="false"
      :md-click-outside-to-close="false"
      style="background: white"
    />

    <md-dialog-confirm
      style="background-color: #fff; color: #EF4343;"
      :md-active.sync="finished"
      :md-backdrop="true"
      :md-content="`
        Tu as ${won ? 'gagné' : 'perdu'}!<br />
        ${won ? 'Essaye de battre ton record' : 'Retente ta chance'} !`
      "
      :md-confirm-text="`${won ? 'Go' : 'Réessayer'} !`"
      md-cancel-text=""
      @md-confirm="retry()"
    />
  </div>
</template>

<script>
import Game from './Game.vue'
import introJs from 'intro.js'
import 'intro.js/introjs.css'

const types = ['qualification', 'final', 'time attack']

export default {
  components: {
    Game
  },
  data () {
    return {
      showRules: false,
      finished: false,
      result: '',
      type: types[0],
      final: false,
      types
    }
  },
  mounted () {
    this.startHandler(this.type)
  },
  computed: {
    won () {
      return this.result === 'won'
    }
  },
  methods: {
    retry () {
      this.finished = false
      this.startHandler(this.type === 'final' ? 'qualification' : this.type)
    },
    refresh () {
      location.reload();
    },
    startHandler (type) {
      this.type = type
      this.$refs.game.start(type)
    },
    wonHandler () {
      if (this.$refs.game.type === 'qualification') {
        this.final = true
      } else {
        this.finished = true
        this.result = 'won'
      }
    },
    lostHandler () {
      this.finished = true
      this.result = 'lost'
    },
    help (options = {}) {
      const finalOptions = {
        nextLabel: 'suivant',
        prevLabel: 'précédent',
        skipLabel: 'terminer',
        doneLabel: 'terminer',
        exitOnEsc: true,
        exitOnOverlayClick: true,
        keyboardNavigation: true,
        showBullets: true,
        showProgress: true
      }
      const result = introJs()
      Object.entries(finalOptions).forEach(
        ([name, value]) => result.setOption(name, value)
      )
      result.start()
      return result
    },
    changeColor (color) {
      this.showContent = true
      const backgrounds = Array.from(document.getElementsByClassName('backgroundcolor'))
      backgrounds.forEach(
        item => {
          item.style.backgroundColor = color
        }
      )
      const borders = Array.from(document.getElementsByClassName('bordercolor'))
      borders.forEach(
        item => {
          item.style.border = `5px solid ${color}`
        }
      )
    }
  }
}
</script>

<style scoped>
.row {
    margin-top: 40px;
}
a {
  text-decoration: none;
  border: none;
  font-color: white;
}
a:hover {
  text-decoration: none;
  border: none;
  font-color: white;
}
a:visited {
  text-decoration: none;
  border: none;
  font-color: white;
}
#putinred {
  color: #ef4343;
  background: #ef4343;
}
#putinblue {
  color: #2980b9;
  background: #2980b9;
}
#putingreen {
  color: #27ae60;
  background: #27ae60;
}
#putinorange {
  color: #d35400;
  background: #d35400;
}
</style>
