<template>
    <div class="row">
      <md-dialog-confirm
        :md-active.sync="shortcut"
        :md-backdrop="false"
        md-cancel-text="Jouer les qualifications"
        md-confirm-text="Aller en phase finale"
        @md-cancel="start()"
        @md-confirm="start(true)"
      />

      <md-dialog-alert
        v-if="attempt > 1"
        :md-active.sync="finished"
        :md-backdrop="false"
        :md-title="`Phase ${final ? 'finale' : 'de qualification'} - manche ${attempt} / ${final ? 6 : 3} terminée`"
        md-content="Appuyer sur START pour démarrer la manche suivante !"
      />

      <div class="col-sm-12 col-lg-8 col-md-10 offset-lg-2 offset-md-1">
        <div class="row text-center">
          <div class="col-sm-12 col-lg-12 col-md-10 text-center">
            <h1 style="font-weight: bold; text-transform: uppercase; margin-top: -30px;">Mot De Passe</h1>
            <h4 style="font-weight: bold; text-transform: uppercase;" data-intro="Mot de passe se compose d'une phase de qualification et d'une phase finale">Phase {{ final ? 'finale' : 'de qualification' }}</h4>
            <h5 style="font-weight: bold; text-transform: uppercase;" data-intro="La phase de qualification comprend 3 manches et la phase finale comprend 6 manches">Manche {{ attempt }} / {{ final ? 6 : 3 }}</h5>
            <h5 v-if="final" style="font-weight: bold; text-transform: uppercase;" data-intro="Gain en jeu">{{ gains[attempt - 1] }} €</h5>
            <h5 v-else style="font-weight: bold; text-transform: uppercase;" data-intro="Pour passer en phase finale, il vous faudra trouver 11 mots">Mots trouvés : {{ found }} / 11</h5>
          </div>
        </div>
        <div class="row text-center">
          <div class="col-sm-12 col-lg-3 col-md-10">
            <timer ref="timer" :duration="duration" :disabled="!playing" @timeout="timeoutHandler" />
          </div>
        </div>
        <div class="row">
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="successHandler" :disabled="!playing" data-intro="Valider un mot" >✓</md-button>
          </div>
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="skipHandler" :disabled="!playing" data-intro="Passer un mot">>></md-button>
          </div>
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="failHandler" :disabled="!playing" data-intro="Invalider un mot pour non respect des règles">X</md-button>
          </div>
          <div class="col-sm-3 col-lg-2 col-md-3 offset-lg-7">
            <md-button class="md-raised md-accent backgroundcolor" @click="startHandler()" id="startgame" :disabled="playing" data-intro="Commencer la partie">Start</md-button>
          </div>
        </div>
        <div class="row text-center" style="margin-top: 130px;">
          <div
            v-for="(step, index) in steps"
            :key="step.value"
            :class="`col-sm-${Math.round(12 / steps.length)} col-lg-${Math.round(12 / steps.length)} col-md-${Math.round(12 / steps.length)} text-center`"
            @click="select(index)"
          >
            <div class="point" :style="step.found ? 'backgroundColor: green' : (index === currentIndex ? 'backgroundColor: orange' : (step.failed ? 'backgroundColor: red' : ''))" />
          </div>
        </div>
        <div class="row text-center" style=" margin-bottom: 50px;">
          <div class="col-sm-12 col-lg-12 col-md-12">
            <h3 style="margin-bottom: 30px;" id="keymdp" v-if="steps.length">
              {{ steps[this.currentIndex].value }}
            </h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Motsdepasses from './liste_francais'
import Timer from './Timer.vue'

const getRandomInt = max => Math.floor(Math.random() * Math.floor(max))

const newWord = () => Motsdepasses[getRandomInt(Motsdepasses.length)]

const gains = [10000, 20000, 25000, 50000, 75000, 100000]

export default {
  components: {
    Timer
  },
  data () {
    return {
      shortcut: true,
      final: false,
      timeout: false,
      steps: [],
      currentIndex: 0,
      playing: false,
      attempt: 1,
      found: 0,
      finished: false,
      gains
    }
  },
  computed: {
    duration () {
      return 30 // this.final ? (30 + (6 - this.attempt) * 6) : 30
    },
    foundSteps () {
      return (this.steps.length && this.steps.map(step => step.found ? 1 : 0).reduce((a, b) => a + b)) || 0
    },
    failed () {
      return (this.steps.length && this.steps.map(step => step.failed ? 1 : 0).reduce((a, b) => a + b)) || 0
    },
    won () {
      return this.foundSteps >= 5 || this.found >= 11
    },
    lost () {
      return this.timeout || (this.steps.length - this.failed) > this.nfound
    }
  },
  methods: {
    select (index) {
      if (this.final && !(this.steps[index].found || this.steps[index].failed)) {
        this.currentIndex = index
      }
    },
    nextIndex () {
      for (let index = 1; index < this.steps.length; index++) {
        const finalIndex = (this.currentIndex + index) % this.steps.length
        if (!(this.steps[finalIndex].found || this.steps[finalIndex].failed)) {
          this.currentIndex = finalIndex
          break
        }
      }
      if (this.steps[this.currentIndex].failed || this.steps[this.currentIndex].found) {
        this.nextPhase()
      }
    },
    successHandler () {
      this.steps[this.currentIndex].found = true

      if (!this.final) {
        this.found += 1
      }
      if (this.won) {
        this.finishPhase(true)
      } else {
        this.nextIndex()
      }
    },
    failHandler () {
      if (this.final) {
        this.steps[this.currentIndex].failed = true
        if ((this.steps.length - this.failed) < 5) {
          this.finishGame(false)
        }
        this.nextIndex()
      } else {
        this.skipHandler()
      }
    },
    timeoutHandler () {
      this.timeout = true
      this.finishPhase(this.won)
    },
    skipHandler () {
      if (this.final) {
        this.nextIndex()
      } else {
        this.steps[this.currentIndex].value = newWord()
      }
    },
    finishGame (won = true) {
      if (won) {
        if (this.final) {
          this.$emit('won')
        }
      } else {
        this.$emit('lost')
      }
      this.playing = false
      this.$refs.timer.stop()
    },
    finishPhase (won = false) {
      this.playing = false
      if (won) {
        if (this.final) {
          this.finished = this.attempt !== 6
        } else {
          this.finished = this.attempt !== 1
        }
      }
      this.$refs.timer.stop()
      if (won) {
        if ((this.final && this.attempt === 6) || (this.attempt === 3 && !this.final)) {
          this.finishGame(true)
        }
      } else {
        this.finishGame(false)
      }
    },
    nextPhase () {
      this.playing = false

      if (this.final) {
        if (this.attempt === 6) {
          if (this.foundSteps === 5) {
            return this.finishGame(true)
          } else {
            return this.finishGame(false)
          }
        } else {
          if (this.foundSteps === 5 || this.attempt === 0) {
            this.attempt += 1
          } else {
            return this.finishGame(false)
          }
        }
      } else {
        if (this.found >= 11) {
          this.final = true
          this.found = 0
          this.attempt = 1
        } else if (this.attempt === 3) {
          return this.finishGame(false)
        } else {
          this.attempt += 1
        }
      }

      const nsteps = this.final ? (11 - this.attempt) : 5

      this.steps = Object.assign(
        [],
        new Array(nsteps).fill().map(
          (_, index) => ({
            value: newWord(),
            found: false,
            failed: false
          })
        )
      )

      this.currentIndex = 0

      this.$refs.timer.stop()
    },
    startHandler () {
      this.nextPhase()
      this.playing = true
      this.$refs.timer.start()
    },
    start (final = false) {
      this.final = final
      this.shortcut = false
      this.attempt = 0
      this.found = 0
      this.currentIndex = 0
      this.startHandler()
    },
    restart () {
      this.shortcut = true
    }
  }
}
</script>

<style scoped>
.row {
    margin-top: 40px;
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
