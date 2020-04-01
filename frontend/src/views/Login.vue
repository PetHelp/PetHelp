<template>
  <div class="register container pt-5 my-5 z-depth-1">
    <b-row align-h="center">
      <b-col xs="12" sm="10" md="6" lg="6" xl="4">
        <h1 class="text-center">Anmelden</h1>
        <b-form @submit.prevent="onSubmit">

          <b-form-group id="input-group-1" label="E-Mail-Adresse" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.email"
              type="email"
              required
              size="lg"
              placeholder="Gib deine E-Mail-Adresse ein"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Passwort" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.password"
              required
              size="lg"
              placeholder="Gib dein Passwort ein"
              type="password"
            ></b-form-input>
          </b-form-group>

          <p class="text-center"><b-button size="lg" type="submit" :disabled=!formIsValid variant="primary">Anmelden</b-button></p>
        </b-form>
        <p class="text-center">Du hast noch keinen Account?<br><router-link to="/register">Dann erstelle dir kostenlos einen!</router-link></p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit () {
      this.$store.dispatch('login', this.form)
    }
  },
  computed: {
    formIsValid () {
      return this.form.email && this.form.password
    }
  }
}
</script>
