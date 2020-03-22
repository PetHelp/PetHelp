<template>
  <div class="page">
    <div class="container-fluid my-5 px-0 z-depth-1">
      <div class="hero">
        <img class="hero__image" src="../assets/Images/pethelp-header.png" alt="" />
        <div class="hero__text">
          <h2>Bereits 20.189 gefundene Pfleegestellen!</h2>
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
          class="mt-5"
        >
          <Animal v-bind:animal="animal"></Animal>
        </b-col>
      </b-row>
      <button type="button" class="btn btn-outline px-4 py-2 mt-5">Mehr anzeigen</button>
  </section>
</div>

<div class="container pt-5 my-5 z-depth-1">
  <section class="p-md-3 mx-md-5 text-center text-lg-left">
    <h2 class="text-center mx-auto font-weight-bold mb-4 pb-2">Wir helfen Tierbesitzer*innen in Quarantäne</h2>
    <div class="row">
      <div class="col-lg-3 col-md-4 col-sm-6 mb-4  Bereich">
        <div class="p-4">
          <div
            class="avatar w-100 white d-flex justify-content-center align-items-center"
          >
            <img
              src="https://mdbootstrap.com/img/Photos/Avatars/img%20(9).jpg"
              class="img-fluid rounded-circle z-depth-1"
            />
          </div>
          <div class="text-center mt-3">
            <h6 class="font-weight-bold pt-2">Alan Turing</h6>
            <p class="text-muted">
              <small
                ><i
                  >27 Jahre, Student</i
                ></small
              >
            </p>
            <button type="button" class="btn btn-primary ContactButton">Helfer*in kontaktieren</button>
          </div>
        </div>
      </div>

      <div class="col-lg-3 col-md-4 col-sm-6 mb-4  Bereich">
        <div class="p-4">
          <div
            class="avatar w-100 white d-flex justify-content-center align-items-center"
          >
            <img
              src="https://mdbootstrap.com/img/Photos/Avatars/img%20(2).jpg"
              class="img-fluid rounded-circle z-depth-1"
            />
          </div>
          <div class="text-center mt-3">
            <h6 class="font-weight-bold pt-2">Nathalie Fry</h6>
            <p class="text-muted">
              <small
                ><i
                  >29 Jahre, Bloggerin</i
                ></small
              >
            </p>
            <button type="button" class="btn btn-primary ContactButton">Helfer*in kontaktieren</button>
          </div>
        </div>
      </div>

      <div class="col-lg-3 col-md-4 col-sm-6 mb-4  Bereich">
        <div class="p-4">
          <div
            class="avatar w-100 white d-flex justify-content-center align-items-center"
          >
            <img
              src="https://mdbootstrap.com/img/Photos/Avatars/img%20(8).jpg"
              class="img-fluid rounded-circle z-depth-1"
            />
          </div>
          <div class="text-center mt-3">
            <h6 class="font-weight-bold pt-2">Billy Turner</h6>
            <p class="text-muted">
              <small
                ><i
                  >32 Jahre, Jurist</i
                ></small
              >
            </p>
            <button type="button" class="btn btn-primary ContactButton">Helfer*in kontaktieren</button>
          </div>
        </div>
      </div>
      <div class="col-lg-3 col-md-4 col-sm-6 mb-4  Bereich">
        <div class="p-4">
          <div
            class="avatar w-100 white d-flex justify-content-center align-items-center"
          >
            <img
              src="https://mdbootstrap.com/img/Photos/Avatars/img%20(4).jpg"
              class="img-fluid rounded-circle z-depth-1"
            />
          </div>
          <div class="text-center mt-3">
            <h6 class="font-weight-bold pt-2">Veronica Smith</h6>
            <p class="text-muted">
              <small
                ><i
                  >22 Jahre, Studentin</i
                ></small
              >
            </p>
            <button type="button" class="btn btn-primary ContactButton">Helfer*in kontaktieren</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

 <button type="button" class="btn btn-primary">Mehr anzeigen...</button>

  </div>
</template>

<script>
import Animal from '../components/Animal.vue'

export default {
  components: { Animal },
  data: function () {
    return {
      animals: [
        { id: 1, name: 'Nico', age: 10, img: 'Hund1.png', hometown: 'Bonn' },
        { id: 2, name: 'Sumo', age: 2, img: 'Hund2.png', hometown: 'Berlin' },
        { id: 3, name: 'T-Rex', age: 5, img: 'Hund3.jpg', hometown: 'Heinsberg' },
        { id: 4, name: 'Hope', age: 3, img: 'Hund4.jpg', hometown: 'Würzburg' },
        { id: 5, name: 'Rufus', age: 1, img: 'Hund5.jpg', hometown: 'Hannover' },
        { id: 6, name: 'Terence', age: 8, img: 'Hund6.jpg', hometown: 'München' },
        { id: 7, name: 'Bud', age: 13, img: 'Hund7.jpg', hometown: 'Heinsberg' },
        { id: 8, name: 'Lily', age: 13, img: 'Hund8.jpg', hometown: 'Heinsberg' }
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
