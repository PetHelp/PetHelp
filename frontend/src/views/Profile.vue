<template>
  <div class="about">
    <b-row class="mt-3">
      <div class="user__avatar col-4 offset-1">
        <Avatar :img="user.img" :user-name="user.name" />
      </div>
      <div class="user__personal-data col-6 text-left">
        <h1>{{ user.name }}</h1>
        <b>Wohnort:</b> {{ user.hometown }}<br>
        <b>Telefon:</b> {{ user.phone }}
      </div>
    </b-row>

    <b-row class="mt-5">
      <b-col cols="10" offset="1">
        <div class="user__experience">
          <h2>Erfahrungen / Präferenzen</h2>
          <p>
            {{ user.experience }}
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
              <Animal v-bind:animal="animal"></Animal>
            </b-col>
          </b-row>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import Avatar from '../components/Avatar.vue'
import Animal from '../components/Animal.vue'

export default {
  name: 'profile-view',
  components: { Avatar, Animal },
  data: function () {
    return {
      user: {
        name: 'Corinna Quarantina',
        img: 'Mensch3.jpg',
        hometown: 'Berlin',
        phone: '(0179) 200 33 66',
        experience: 'Spicy jalapeno cow ribeye drumstick meatloaf. Meatball t-bone ham spare ribs, short ribs ball tip alcatra leberkas ham hock chislic landjaeger. Brisket bresaola venison, buffalo ball tip beef pastrami meatball shank flank. Pork chop leberkas frankfurter short loin chislic tenderloin drumstick pastrami kevin pork loin tail jowl pig.',
        animals: [
          { id: 1, name: 'T-Rex', age: 6, img: 'Hund3.jpg' },
          { id: 2, name: 'Sumo', age: 2, img: 'Hund2.png' }
        ]
      }
    }
  },
  created: function () {
    if (this.$store.state.profile.id === null) {
      this.$store.dispatch('getProfile')
    }

    const profile = this.$store.state.profile
    this.user.name = profile.name
    this.user.hometown = profile.address
    this.user.experience = profile.bio
  }
}
</script>
