<template>
  <div class="about">
    <b-row class="mt-3">
      <div class="user__avatar col-4 offset-1">
        <Avatar :img="user.img" :user-name="user.name" />
      </div>
      <div class="user__personal-data col-6 text-left">
        <h1><EditableTextOutput v-bind:value="user.name" v-on:input="user.name = $event" v-on:change="updateProfile()" /></h1>
        <b>Wohnort:</b> <EditableTextOutput :value="user.address" v-on:input="user.address = $event" v-on:change="updateProfile()" /><br>
        <b>Notfall-E-Mail:</b> <EditableTextOutput :value="user.emergencyContactEmail" v-on:input="user.emergencyContactEmail = $event" v-on:change="updateProfile()" />
      </div>
    </b-row>

    <b-row class="mt-5">
      <b-col cols="10" offset="1">
        <div class="user__experience">
          <h2>Erfahrungen / Präferenzen</h2>
          <p>
            <EditableTextOutput :type="'textarea'" :cols="100" :rows="10" :value="user.bio" v-on:input="user.bio = $event" v-on:change="updateProfile()" />
          </p>
        </div>
      </b-col>
    </b-row>

    <b-row class="mt-3">
      <b-col cols="10" offset="1">
        <div class="user__pets">
          <h2>Meine Tiere</h2>
          <b-row class="mt-3">
            <b-col
              cols="3"
              v-for="animal in user.animals"
              v-bind:key="animal.id"
            >
              <router-link :to="{ name: 'editPet', params: { id: animal.id } }"><Animal v-bind:animal="animal" /></router-link>
            </b-col>
          </b-row>
        </div>
      </b-col>
    </b-row>

    <b-row class="mt-3">
      <b-col cols="10">
        <router-link tag="button" to="/profil/haustier/add">Haustier hinzufügen</router-link>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Avatar from '../components/Avatar.vue'
import Animal from '../components/Animal.vue'
import EditableTextOutput from '../components/EditableTextOutput.vue'

export default {
  title: 'Quarantiere - Profil',
  name: 'profile-view',
  components: { Avatar, Animal, EditableTextOutput },
  data () {
    return {
      user: {
        name: 'Corinna Quarantina',
        img: 'Mensch3.jpg',
        address: 'Berlin',
        emergencyContactEmail: 'some-mail@somewhere.com',
        bio: 'Spicy jalapeno cow ribeye drumstick meatloaf. Meatball t-bone ham spare ribs, short ribs ball tip alcatra leberkas ham hock chislic landjaeger. Brisket bresaola venison, buffalo ball tip beef pastrami meatball shank flank. Pork chop leberkas frankfurter short loin chislic tenderloin drumstick pastrami kevin pork loin tail jowl pig.',
        animals: []
      }
    }
  },
  created () {
    this.loadProfile()
    this.loadAnimals()
  },
  methods: {
    loadProfile () {
      if (this.$store.state.profile.id === null) {
        this.$store.dispatch('getProfile')
      }
      console.log(this.$store.state.profile)
      const profile = this.$store.state.profile
      this.user.name = profile.name
      this.user.address = profile.address
      this.user.bio = profile.bio
      this.user.animals = profile.animals
      this.user.emergencyContactEmail = profile.emergencyContactEmail
    },
    loadAnimals () {
      this.$store.dispatch('getAnimals')
      console.log(this.$store.state.profile.animals)
      this.user.animals = this.$store.state.profile.animals
    },
    updateProfile () {
      this.$store.dispatch('updateProfile', {
        id: this.$store.state.profile.id,
        name: this.user.name,
        bio: this.user.bio,
        address: this.user.address,
        emergencyContactEmail: this.user.emergencyContactEmail
      })
    }
  }
}
</script>
