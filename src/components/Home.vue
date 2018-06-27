<template>
  <div>
    <md-dialog-alert
      style="background-color: #616161; color: white;"
      :md-active.sync="showRules"
      md-content="
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
    </md-toolbar>

    <div class="container">
      <div class="row text-center">
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
          <md-button class="col-lg-12 col-md-12 col-sm-12" style="color: white;" id="showshow" @click="startHandler()">
            {{ playing ? 'Arrêter' : 'Jouer' }}
          </md-button>
        </div>
      </div>
    </div>

    <div v-if="playing" class="container bordercolor" style="border: 5px solid red; background-color: white; margin-top: 20px; margin-bottom: 30px;">
      <game
        @won="wonHandler"
        @lost="lostHandler"
        ref="game"
      />
    </div>

    <md-dialog-confirm
      style="background-color: #fff; color: #EF4343;"
      :md-active.sync="lost"
      :md-backdrop="false"
      md-content="
        Tu as perdu!<br />
        Retente ta chance!
      "
      md-confirm-text="Réessayer!"
      :md-cancel-text="null"
      @md-confirm="$refs.game.start()"
    />
    <md-dialog-confirm
      style="background-color: white;"
      :md-active.sync="won"
      :md-backdrop="false"
      md-content="
        Tu as gagné!<br />
        Essaye de battre ton record!
      "
      md-confirm-text="Go!"
      :md-cancel-text="null"
      @md-confirm="$refs.game.start()"
    />
  </div>
</template>

<script>
import Game from './Game.vue'
import introJs from 'intro.js'
import 'intro.js/introjs.css'

export default {
  components: {
    Game
  },
  data () {
    return {
      showRules: false,
      lost: false,
      won: false,
      playing: false
    }
  },
  methods: {
    refresh () {
      location.reload();
    },
    startHandler () {
      this.playing = true
    },
    wonHandler () {
      this.won = true
    },
    lostHandler () {
      this.lost = true
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
