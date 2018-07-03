<template>
	<div class="container-fluide text-center backgroundcolor" style="color: white !important; width: 100%; background-color: #EF4343">
			<footer style="margin-top: 30px; margin-bottom: 50px;">
				<p style="color: white !important; font-size: 15px; margin-top: 105px;">Développement du site et du jeu réalisé par
				<v-tooltip top>
					
      <a
      	id="cvcv"
        slot="activator"
        href="http://www.b3j0f.org/cv/all"
        target="_blank"
      >
        Jonathan Labejof 
      </a>
      <span>Curriculum Vitae</span>
    </v-tooltip>
    et
          <v-tooltip bottom>
      <a
      	id="cvcv"
        slot="activator"
        href="http://www.d-lecoin.rf.gd"
        target="_blank"
      >
        David Lecoin 
      </a>
      <span>Curriculum Vitae</span>
    </v-tooltip>
      </v-card-text>
      <v-card-text class="white--text">
        &copy;2018 — <strong>KeyWord</strong>
        </v-card-text>
    </v-card>
</p>

  </footer>
	</div>
</template>

<script>
export default {
	data(){
		return{
			
		}
	}
}
</script>

<style scoped>
#cvcv{
	color: black;
	font-size: 21px;
}
</style>