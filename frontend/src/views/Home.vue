<template>
  <div>
    <image-component />
    <p>Bereits 20.189 gefundene Pfleegestellen!</p>
    <b-row align-h="center">
      <b-col></b-col>
      <b-col><b-button>Ich brauche Hilfe</b-button></b-col>
      <b-col><b-button>Ich möchte helfen</b-button></b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import ImageComponent from '@/components/landing/Image.vue'

export default {
  name: 'Home',
  components: {
    ImageComponent
  }
}
</script>
