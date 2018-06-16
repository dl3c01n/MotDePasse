<template>
    <div style="margin-top: 40px;">
        <div class="container" style="border: 10px solid red;">
            <div class="row">
                <div class="col-sm-12 col-lg-8 col-md-10 offset-lg-2 offset-md-1">
                    <div class="row  text-center">
                        <div class="col-sm-12 col-lg-12 col-md-10 text-center">
                            <h1 style="font-weight: bold; text-transform: uppercase; margin-top: -30px;">{{ welcome }}</h1>
                        </div>
                    </div>
                    <div class="row text-center">
                        <div class="col-sm-12 col-lg-3 col-md-10">
                            <p id="timetime">0:30</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12 col-lg-1 col-md-10">
                            <b-button variant="danger" @click="NextWord">✓</b-button>
                        </div>
                        <div class="col-sm-12 col-lg-1 col-md-10">
                            <b-button variant="danger" @click="Failed">X</b-button>
                        </div>
                        <div class="col-sm-12 col-lg-1 col-md-10">
                            <b-button variant="danger" @click="idk">>></b-button>
                        </div>
                    </div>
                    <div class="row text-center" style="margin-top: 130px;">
                        <div class="col-sm-12 col-lg-2 offset-lg-2 col-md-12 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-12 col-lg-2 col-md-10 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-12 col-lg-2 col-md-10 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-12 col-lg-2 col-md-10 text-center">
                            <div class="point"></div>
                        </div>
                        <div class="col-sm-12 col-lg-2 col-md-10 text-center">
                            <div class="point"></div>
                        </div>
                    </div>
                    <div class="row text-center">
                        <div class="col-sm-12 col-lg-11 col-md-10 offset-lg-1">
                            <h3 style="border: 1px solid black; margin-bottom: 30px;" id="keymdp">{{ Motsdepasses[0] }}</h3> 
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
        }
    },
    components:{

    },
    methods:{
        NextWord(){
            this.Motsdepasses.shift();
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
    border: 1px solid black;
    font-size: 50px;
    margin-right: -10px;
}
.point{
    background:black;
    border: 3px solid green;
    width:30%;
    height:350%;
    border:2px solid black; 
}
</style>
