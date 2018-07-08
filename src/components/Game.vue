<template>
    <div class="row">
      <md-dialog-confirm
        v-if="phase > 0"
        :md-active.sync="pause"
        :md-backdrop="true"
        :md-title="`Phase ${type === 'final' ? 'finale' : 'de qualification'} - manche ${phase} / ${type === 'final' ? finalPhases : qualificationPhases} terminée`"
        :md-content="`Appuyer sur START pour démarrer la ${type === 'qualitication' && phase === qualificationPhases ? 'finale' : 'manche suivante'} !`"
        md-cancel-text="Sauvegarder la partie"
        md-confirm-text="Prochaine manche"
        @md-cancel="save()"
        @md-confirm="nextPhase()"
        style="background: white"
        :md-close-on-esc="false"
        :md-click-outside-to-close="false"
      />

      <div class="col-sm-12 col-lg-8 col-md-10 offset-lg-2 offset-md-1">
        <div class="row text-center">
          <div class="col-sm-12 col-lg-12 col-md-10 text-center">
            <h1 style="font-weight: bold; text-transform: uppercase; margin-top: -30px;">Mot De Passe</h1>
            <h4 style="font-weight: bold; text-transform: uppercase;" data-intro="Mot de passe se compose d'une phase de qualification et d'une phase finale">Phase {{ type === 'final' ? 'finale' : 'de qualification' }}</h4>
            <h5 style="font-weight: bold; text-transform: uppercase;" data-intro="La phase de qualification comprend 2 manches et la phase finale comprend 6 manches">Manche {{ phase }} / {{ type === 'final' ? finalPhases : qualificationPhases }}</h5>
            <h5 v-if="type === 'final'" style="font-weight: bold; text-transform: uppercase;" data-intro="Gains si manche terminée">Gain possible {{ gains[phase -1] }}€ {{ phase > 1 ? `(en poche : ${gains[phase - 2]}€)` : '' }}</h5>
            <h5 v-else style="font-weight: bold; text-transform: uppercase;" data-intro="Pour passer en phase finale, il vous faudra trouver 7 mots">Mots trouvés : {{ found }} / 7</h5>
          </div>
        </div>
        <div class="row text-center">
          <div class="col-sm-12 col-lg-3 col-md-10">
            <timer ref="timer" :duration="duration" :disabled="!playing" @timeout="timeoutHandler" />
          </div>
        </div>
        <p v-if="ready">Appuyez sur START pour démarrer</p>
        <div class="row">
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="foundHandler" :disabled="state !== 'playing'" data-intro="Valider un mot" >✓</md-button>
          </div>
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="skipHandler" :disabled="state !== 'playing'" data-intro="Passer un mot">>></md-button>
          </div>
          <div class="col-sm-3 col-lg-1 col-md-3">
            <md-button class="md-icon-button md-accent gamebuttons backgroundcolor" @click="failHandler" :disabled="state !== 'playing'" data-intro="Invalider un mot pour non respect des règles">X</md-button>
          </div>
          <div class="col-sm-3 col-lg-2 col-md-3 offset-lg-7">
            <md-button class="md-raised md-accent backgroundcolor" @click="startHandler()" id="startgame" :disabled="state === 'playing'" data-intro="Commencer la partie">Start</md-button>
          </div>
        </div>
        <div class="row text-center offset-lg-1" style="margin-top: 130px; margin-bottom: 30px;">
          <div
            v-for="(step, index) in steps"
            :key="step.value"
            :class="`col-sm-${Math.round(12 / steps.length)} col-lg-${Math.round(12 / steps.length)} col-md-${Math.round(12 / steps.length)} text-center`"
            @click="select(index)"
          >
            <div class="point" :style="step.state === 'found' ? 'backgroundColor: green' : (index === currentIndex ? 'backgroundColor: orange' : (step.state === 'failed' ? 'backgroundColor: red' : ''))" />
          </div>
        </div>
        <div class="row text-center" style=" margin-bottom: 50px;">
          <div class="col-sm-12 col-lg-12 col-md-12">
            <h3 style="margin-bottom: 30px; text-transform: capitalize" id="keymdp" v-if="steps.length">
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
  props: {
    qualificationPhases: {
      type: Number,
      default: 2
    },
    qualificationObjective: {
      type: Number,
      default: 7
    },
    finalPhases: {
      type: Number,
      default: 6
    }
  },
  data () {
    return {
      state: 'pause',
      timeout: false,
      steps: [],
      currentIndex: 0,
      phase: 0,
      found: 0,
      gains,
      type: 'qualification'
    }
  },
  computed: {
    duration () {
      return 30 // this.final ? (30 + (6 - this.phase) * 6) : 30
    },
    pause () {
      return this.state === 'pause'
    },
    availableSteps () {
      return this.countSteps('available')
    },
    foundSteps () {
      return this.countSteps('found')
    },
    failedSteps () {
      return this.countSteps('failed')
    },
    pause () {
      return this.state === 'pause'
    },
    won () {
      return this.state === 'won'
    },
    lost () {
      return this.state === 'lost'
    },
    playing () {
      return this.state === 'playing'
    },
    ready () {
      return this.state === 'ready'
    }
  },
  methods: {
    countSteps (state) {
      return (this.steps.length && this.steps.map(step => step.state === state ? 1 : 0).reduce((a, b) => a + b)) || 0
    },
    select (index) {
      if (this.type === 'final' && this.steps[index].state === 'available') {
        this.currentIndex = index
      }
    },
    nextAvailableIndex () {
      if (this.availableSteps) {
        for (let index = 1; index < this.steps.length; index++) {
          const finalIndex = (this.currentIndex + index) % this.steps.length
          if (this.steps[finalIndex].state === 'available') {
            this.currentIndex = finalIndex
            break
          }
        }
      } else {
        this.finishPhase()
      }
    },
    loose () {
      this.$refs.timer.stop()
      this.state = 'lost'
      this.$emit('lost')
    },
    win () {
      this.$refs.timer.stop()
      this.state = 'won'
      this.$emit('won')
    },
    save () {
      alert('disponible dans la prochaine version...')
    },
    finishPhase () {
      this.$refs.timer.stop()
      this.state = 'pause'
    },
    foundHandler () {
      this.steps[this.currentIndex].state = 'found'

      switch (this.type) {
        case 'qualification':
          this.found += 1
          if (this.found === this.qualificationObjective) {
            this.win()
          } else {
            this.nextAvailableIndex()
          }
          break
        case 'final':
          if (this.foundSteps === 5) {
            if (this.phase === this.finalPhases) {
              this.win()
            } else {
              this.finishPhase()
            }
          } else {
            this.nextAvailableIndex()
          }
          break
        default: throw new Error(`Unknown game type: "${this.type}"`)
      }
    },
    failHandler () {
      this.steps[this.currentIndex].state = 'failed'

      switch (this.type) {
        case 'qualification':
          if (this.availableSteps === 0) {
            if ((this.found + this.availableSteps + (this.qualificationPhases - this.phase) * 5) < this.qualificationObjective) {
              this.loose()
            } else {
              this.finishPhase()
            }
          } else {
            this.nextAvailableIndex()
          }
          break
        case 'final':
          if ((this.steps.length - this.failedSteps) < 5) {
            this.loose()
          } else {
            this.nextAvailableIndex()
          }
          break
        default: throw new Error(`Unknown game type: "${this.type}"`)
      }
    },
    timeoutHandler () {
      this.timeout = true

      switch (this.type) {
        case 'qualification':
          if (this.state === 'playing' && this.phase === this.qualificationPhases) {
            this.loose()
          } else {
            this.finishPhase()
          }
          break
        case 'final':
          this.loose()
          break
        default: throw new Error(`Unknown game type: "${this.type}"`)
      }
    },
    skipHandler () {
      switch (this.type) {
        case 'qualification':
          this.steps[this.currentIndex].value = newWord()
          break
        case 'final':
          this.nextAvailableIndex()
          break
        default: throw new Error(`Unknown game type: "${this.type}"`)
      }
    },
    renewSteps () {
      const stepsCount = 5 + (this.type === 'final' ? (this.finalPhases - this.phase) : 0)

      this.steps = new Array(stepsCount).fill().map(
        () => ({
          state: 'available',
          value: newWord()
        })
      )
    },
    nextPhase () {
      this.state = 'ready'

      this.currentIndex = 0

      switch (this.type) {
        case 'qualification':
          if (this.phase === this.qualificationPhase) {
            this.type = 'final'
          }
        case 'final':
          this.phase += 1
          break
        default: throw new Error(`Unknown game type: "${this.type}"`)
      }
      this.renewSteps()
    },
    startHandler () {
      this.state = 'playing'
      this.$refs.timer.start()
    },
    init () {
      this.found = 0
      this.phase = 1
    },
    start (type) {
      this.state = 'pause'
      this.type = type || this.type
      this.phase = 0
      this.found = 0
      this.nextPhase()
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
    width:30px;
    height:30px;
    border-radius: 100%
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
