<template>
	<div class="container-fluide">
		<md-toolbar class="md-accent" md-elevation="1" style="background-color: #ef4343; color: white;">
      <h3 class="md-title" style="flex: 1">Title</h3>
      <md-button style="color: white;">Refresh</md-button>
      <md-button class="md-primary" style="color: white;">Create</md-button>
    </md-toolbar>
	</div>
</template>

<script>
	export default{
		data: () => ({

		})
	}
</script>

<style lang="scss" scoped>
	.md-toolbar + .md-toolbar {
    margin-top: 16px;
  }
</style>