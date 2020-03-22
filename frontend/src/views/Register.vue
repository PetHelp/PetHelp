<template>
  <div class="register container pt-5 my-5 z-depth-1">
    <b-row align-h="center">
      <b-col xs="12" sm="10" md="6" lg="6" xl="4">
        <h1>Account erstellen</h1>
        <b-form @submit="onSubmit">

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
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4" label="Passwort Bestätigung" label-for="input-4">
            <b-form-input
              id="input-4"
              v-model="form.password2"
              required
              size="lg"
              placeholder="Gib dein Passwort erneut ein"
            ></b-form-input>
          </b-form-group>

          <b-button size="lg" type="submit" :disabled=!formIsValid variant="primary">Account erstellen</b-button>
        </b-form>
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
        password: '',
        password2: null
      }
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      // this.apiService.registerUser({name: this.form.name, email: this.form.email, password:this.form.password}).subscribe()
      // show error or login and redirect
    }
  },
  computed: {
    formIsValid: function () {
      return this.form.email && this.form.password && (this.form.password === this.form.password2)
    }
  }
}
</script>
