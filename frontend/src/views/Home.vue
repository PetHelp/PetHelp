<template>
  <div class="page">
    <div class="container-fluid px-0">
      <div class="hero">
        <img class="hero__image" src="../assets/Images/pethelp-header.png" alt="" />
        <div class="hero__text">
          <h2>Bereits 20.189 gefundene Pflegestellen!</h2>
          <p class="mt-4">Hast du ein Tier, dass schnellst möglich durch Eintritt einer Krankheit oder Quarantäne in gute Hände zur Pflege gegeben werden muss oder du brauchst jemand der sich
            stationär um deine Tiere kümmert?</p>
          <p> Dann bist du bei UNS genau richtig!</p>

          <div class="here__actions mt-5">
            <button type="button" class="btn btn-primary btn-lg btn-light mr-4 px-4 py-2"><b>Ich suche Hilfe</b></button>
            <button type="button" class="btn btn-primary btn-lg btn-light px-4 py-2"><b>Ich biete Hilfe</b></button>
          </div>
        </div>
      </div>
    </div>

    <!-- PETS -->
    <div class="container pt-5 my-5 z-depth-1 ">
      <section class="p-md-3 mx-md-5 text-center">
        <h2 class="text-center mx-auto font-weight-bold mb-4 pb-2">7.651 Tiere brauchen deine Hilfe</h2>
        <b-row class="mt-3">
          <b-col
            cols="3"
            v-for="animal in animals"
            v-bind:key="animal.id"
            class="mt-4"
          >
            <Animal v-bind:animal="animal"></Animal>
          </b-col>
        </b-row>
        <button type="button" class="btn btn-outline px-4 py-2 mt-5">Mehr anzeigen</button>
      </section>
    </div>

    <!-- HELPERS -->
    <div class="container pt-5 my-5 z-depth-1">
      <section class="p-md-3 mx-md-5 text-center">
        <h2 class="text-center mx-auto font-weight-bold mb-4 pb-2">Wir helfen Tierbesitzer*innen in Quarantäne</h2>
        <b-row class="mt-3 text-left">
          <b-col
            cols="4"
            v-for="user in users"
            v-bind:key="user.id"
            class="mt-4"
          >
            <Card v-bind:user="user" />
          </b-col>
        </b-row>
        <button type="button" class="btn btn-outline px-4 py-2 mt-5">Mehr anzeigen</button>
      </section>
    </div>
  </div>
</template>

<script>
import Animal from '../components/Animal.vue'
import Card from '../components/Card.vue'

export default {
  components: { Animal, Card },
  data: function () {
    return {
      animals: [
        { id: 1, name: 'Nico', age: 10, img: 'Hund1.png', hometown: 'Bonn' },
        { id: 2, name: 'Sumo', age: 2, img: 'Hund2.png', hometown: 'Berlin' },
        { id: 3, name: 'T-Rex', age: 5, img: 'Hund3.jpg', hometown: 'Heinsberg' },
        { id: 4, name: 'Hope', age: 3, img: 'Hund4.jpg', hometown: 'Würzburg' },
        { id: 5, name: 'Rufus', age: 1, img: 'Hund5.jpg', hometown: 'Hannover' },
        { id: 6, name: 'Terence', age: 8, img: 'Hund6.jpg', hometown: 'Augsburg' },
        { id: 7, name: 'Bud', age: 13, img: 'Hund7.jpg', hometown: 'Heinsberg' },
        { id: 8, name: 'Lily', age: 13, img: 'Hund8.jpg', hometown: 'Heinsberg' }
      ],
      users: [
        {
          id: 1,
          name: 'Corinna Quarantina',
          givenName: 'Corinna',
          img: 'Mensch3.jpg',
          hometown: 'Berlin',
          phone: '(0179) 200 33 66',
          experience: 'Spicy jalapeno cow ribeye drumstick meatloaf. Meatball t-bone ham spare ribs, short ribs ball tip alcatra leberkas ham hock chislic landjaeger.',
          animals: [
            { id: 1, name: 'T-Rex', age: 6, img: 'Hund3.jpg' },
            { id: 2, name: 'Sumo', age: 2, img: 'Hund2.png' }
          ]
        },
        {
          id: 2,
          name: 'Isabella Isolationara',
          givenName: 'Isabella',
          img: 'Mensch2.jpg',
          hometown: 'Augsburg',
          phone: '(0172) 100 22 99',
          experience: 'Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato.',
          animals: [
            { id: 1, name: 'Terence', age: 8, img: 'Hund6.jpg', hometown: 'Augsburg' }
          ]
        },
        {
          id: 3,
          name: 'Peter Pan-Demie',
          givenName: 'Peter',
          img: 'Mensch1.jpg',
          hometown: 'Hannover',
          phone: '(0175) 500 55 44',
          experience: 'Celery quandong swiss chard chicory earthnut pea potato. Salsify taro catsear garlic gram celery bitterleaf wattle seed collard greens nori.',
          animals: [
            { id: 1, name: 'Rufus', age: 1, img: 'Hund5.jpg', hometown: 'Hannover' }
          ]
        }
      ]
    }
  }
}
</script>

<style scoped>
  img {
    max-width: 100%;
  }

  .hero {
    position: relative;
    color: white;
    background-color: #2c4e57;
  }

  .hero__image {
    margin-bottom: -7em;
  }

  .hero__text {
    position: absolute;
    top: 4em;
    left: 3em;
    width: 50%;
    line-height: 1.5;
    font-size: 1.15em;
  }

  .btn-outline {
    border: 2px solid #2c4e57;
    border-radius: 10px;
    font-weight: bold;
  }

  .page {
      background-color: #fefefe;
  }
</style>
