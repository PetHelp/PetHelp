<template>
  <div class="page col-12 pt-5">
    <div class="container">
      <b-row>
        <b-col cols="12">
          <h1>Biete deine Hilfe an!</h1>
        </b-col>
        <b-col cols="4" class="mt-4">
          <h2>Deine Suche</h2>
          <form>
            <div class="form-group">
              <label for="exampleFormControlInput1">Umkreis</label>
              <input type="email" class="form-control" id="exampleFormControlInput1" value="Heinsberg (10km)" placeholder="name@example.com">
            </div>
            <div class="form-group">
              <label for="exampleFormControlSelect1">Tierart</label>
              <select class="form-control" id="exampleFormControlSelect1">
                <option>Hund</option>
                <option>Katze</option>
                <option>Maus</option>
                <option>Kanarienvogel</option>
              </select>
            </div>
            <div class="form-group">
              <p class="mb-0">Verträglich mit Artgenossen</p>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1" checked>
                <label class="form-check-label" for="inlineRadio1">Ja</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2">
                <label class="form-check-label" for="inlineRadio2">Nein</label>
              </div>
            </div>
            <div class="form-group">
              <p class="mb-0">Sachkundenachweis nötig</p>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3">
                <label class="form-check-label" for="inlineRadio3">Ja</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio4" value="option4" checked>
                <label class="form-check-label" for="inlineRadio4">Nein</label>
              </div>
            </div>
          </form>
          <p class="mt-4"><a class="suche__link" href="#">Suche verfeinern</a></p>
        </b-col>
        <b-col cols="7" class="mt-4" offset="1">
          <h2>Diese Tiere suchen Hilfe in <b>Heinsberg</b></h2>
          <b-row class="mt-3">
            <b-col
              cols="4"
              v-for="animal in animals"
              v-bind:key="animal.id"
              class="mt-4"
            >
              <Animal v-bind:animal="animal"></Animal>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import Animal from '../components/Animal.vue'

export default {
  title: 'Quarantiere - Hilfe anbieten',
  components: { Animal },
  data: function () {
    return {
      animals: [
        { id: 3, name: 'T-Rex', age: 5, img: 'Hund3.jpg', hometown: 'Heinsberg' },
        { id: 7, name: 'Bud', age: 13, img: 'Hund7.jpg', hometown: 'Heinsberg' },
        { id: 8, name: 'Lily', age: 2, img: 'Hund8.jpg', hometown: 'Heinsberg' },
        { id: 9, name: 'Susi', age: 6, img: 'Hund4.jpg', hometown: 'Heinsberg' },
        { id: 10, name: 'Bella', age: 6, img: 'Hund2.png', hometown: 'Heinsberg' }
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

<style>
  .suche__link {
    color: #2c4e57;
    text-decoration: underline;
  }

  .page {
    border-top: 1px solid #2c4e57;
  }
</style>
