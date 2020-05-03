<template>
  <div class="register container pt-5 my-5 z-depth-1">
    <b-row align-h="center">
      <b-col xs="12" sm="10" md="6" lg="6" xl="4">
        <h1 class="text-center">Haustier anpassen</h1>
        <b-form @submit.prevent="onSubmit">

          <b-form-group id="input-group-1" label="Name" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.name"
              type="text"
              required
              size="lg"
              placeholder="Gib den Namen deines Haustiers ein"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Beschreibung" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.description"
              required
              size="lg"
              placeholder="Gib eine Beschreibung zu deinem Haustier ein"
              type="text"
            ></b-form-input>
          </b-form-group>

          <p class="text-center"><b-button size="lg" type="submit" :disabled=!formIsValid variant="primary">Speichern</b-button></p>
          <p class="text-center"><b-button size="lg" type="button" v-on:click="deleteAnimal" variant="danger">Löschen</b-button></p>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  title: 'Quarantiere - Haustier anpassen',
  data () {
    return {
      id: this.$route.params.id,
      form: {
        name: '',
        description: ''
      },
      animal: null
    }
  },
  methods: {
    onSubmit () {
      this.animal.name = this.form.name
      this.animal.description = this.form.description
      this.$store.dispatch('updateAnimal', this.animal)
    },
    deleteAnimal () {
      this.$store.dispatch('deleteAnimal', this.animal.id)
    }
  },
  computed: {
    formIsValid () {
      return true
    }
  },
  created () {
    this.animal = this.$store.getters.getAnimalById(this.id)

    if (this.animal) {
      this.form.name = this.animal.name
      this.form.description = this.animal.description
    }
  }
}
</script>
