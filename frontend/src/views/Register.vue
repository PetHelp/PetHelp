<template>
  <div class="register container pt-5 my-5 z-depth-1">
    <b-row align-h="center">
      <b-col xs="12" sm="10" md="6" lg="6" xl="4">
        <h1 class="text-center">Account erstellen</h1>
        <b-form @submit.prevent="onSubmit">

        <b-form-group id="input-group-1" label="Name" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.name"
              size="lg"
              placeholder="Gib deinen Namen ein"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="E-Mail-Adresse" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.email"
              type="email"
              required
              size="lg"
              placeholder="Gib deine E-Mail-Adresse ein"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Passwort" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.password"
              required
              size="lg"
              placeholder="Gib dein Passwort ein"
              type="password"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4" label="Passwort Bestätigung" label-for="input-4">
            <b-form-input
              id="input-4"
              v-model="form.confirmPassword"
              required
              size="lg"
              placeholder="Gib dein Passwort erneut ein"
              type="password"
            ></b-form-input>
          </b-form-group>

          <p class="text-center"><b-button size="lg" type="submit" :disabled=!formIsValid variant="primary">Account erstellen</b-button></p>
        </b-form>
        <p class="text-center">Du hast bereits einen Account?<br><router-link to="/login">Dann gehts hier zur Anmeldung!</router-link></p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  title: 'Quarantiere - Registrierung',
  data () {
    return {
      form: {
        email: '',
        name: '',
        password: '',
        confirmPassword: null
      }
    }
  },
  methods: {
    onSubmit () {
      this.$store.dispatch('register', this.form)
    }
  },
  computed: {
    formIsValid () {
      return this.form.email && this.form.password && (this.form.password === this.form.confirmPassword)
    }
  }
}
</script>
