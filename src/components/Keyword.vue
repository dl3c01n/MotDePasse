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
      md-confirm-text="Compris" />
        <md-toolbar class="md-accent" md-elevation="1" style="background-color: #ef4343; color: white;">
      <h3 class="md-title" style="flex: 1">KeyWord</h3>
      <md-button style="color: white;" @click="Refresh">Rafraîchir</md-button>
      <md-button class="md-primary" style="color: white;" @click="second = true">Règles du jeu</md-button>
    </md-toolbar>
    <div class="container">
        <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12 text-center">
                <md-button class="col-lg-12 col-md-12 col-sm-12" style="color: white;" id="showshow" @click="allowContent">Jouer</md-button>
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
                             <md-button class="md-icon-button md-accent gamebuttons" @click="NextWord" disabled>✓</md-button>
                        </div>
                        <div class="col-sm-3 col-lg-1 col-md-3">
                             <md-button class="md-icon-button md-accent gamebuttons" @click="Failed" disabled>X</md-button>
                        </div>
                        <div class="col-sm-3 col-lg-1 col-md-3">
                            <md-button class="md-icon-button md-accent gamebuttons" @click="idk" disabled>>></md-button>
                        </div>
                        <div class="col-sm-3 col-lg-2 col-md-3 offset-lg-7">
                            <md-button class="md-raised md-accent" @click="startCountDown" id="startgame">Start</md-button>
                        </div>
                    </div>
                    <div class="row text-center" style="margin-top: 130px;">
                        <div class="col-sm-2 col-lg-2 offset-lg-1 col-md-2 offset-md-1 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-2 col-lg-2 col-md-2 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-2 col-lg-2 col-md-2 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-2 col-lg-2 col-md-2 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-2 col-lg-2 col-md-2 text-center">
                            <div class="point"></div>
                        </div>
                    </div>
                    <div class="row text-center" style=" margin-bottom: 50px;">
                        <div class="col-sm-12 col-lg-12 col-md-12">
                            <h3 style="margin-bottom: 30px;" id="keymdp">{{ Motsdepasses[0] }}</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data(){
        return{
            welcome: "Mot De Passe",
            Motsdepasses: ["Jour", "Repas", "Signature", "Nager", "Respirer", "Amour", "Orteil"],
            count: 30,
            second: false,
            showContent: false
        }
    },
    components:{

    },
    methods:{
        NextWord(){
            this.Motsdepasses.shift();
            document.getElementsByClassName("point")[0].style.backgroundColor = "green";
            const Mdp = document.getElementById("keymdp");
            if(Mdp.innerHTML === ""){
                this.Motsdepasses = ["Jour", "Repas", "Signature", "Nager", "Respirer", "Amour", "Orteil"]
            }
        },
        Failed(){
            this.Motsdepasses.shift();
        },
        idk(){
            this.Motsdepasses.shift();
        },
        countDown () {
            setTimeout(() => {
                this.count -= 1
                if (this.count > 0) {
                    //
                    this.countDown()
                } else {
                    document.getElementsByClassName("gamebuttons")[0].setAttribute("disabled", "");
                    document.getElementsByClassName("gamebuttons")[1].setAttribute("disabled", "");
                    document.getElementsByClassName("gamebuttons")[2].setAttribute("disabled", "");
                }
            }, 1000)
        },
        allowButtons(){
            document.getElementsByClassName("gamebuttons")[0].removeAttribute("disabled");
            document.getElementsByClassName("gamebuttons")[1].removeAttribute("disabled");
            document.getElementsByClassName("gamebuttons")[2].removeAttribute("disabled");
        },
        startCountDown () {
            this.allowButtons()
            this.count = 30
            this.countDown()
        },
        Refresh(){
            location.reload();
        },
         allowContent(){
              if(this.showContent === false){
                this.showContent = true
                document.getElementById('showshow').innerHTML = "Arrêter"
              }else{
                this.showContent = false
                document.getElementById('showshow').innerHTML = "Jouer"
              }
        }
    },
    components:{
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
