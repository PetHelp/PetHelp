<template>
<div class="wrapper">
  <div class="accordion" id="accordionExample">

    <div class="card">
      <div class="card-header" id="headingOne">
        <h2 class="mb-0">
          <button class="btn btn-link QuestionBox" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Ist die Plattform kostenlos nutzbar?
          </button>
        </h2>
      </div>
      <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">
        <div class="card-body">
          Ja die Plattform ist für jeden kostenfrei nutzbar.
          Sie soll in der aktuell schwierigen Lage eine Möglichkeit bieten, seine tierlichen Gefährten im Ernstfall schnell an eine geeignete Pflegestelle vermitteln zu können.
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-header" id="headingTwo">
        <h2 class="mb-0 ">
          <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Welche Daten erhebt ihr? (Datenschutz)
          </button>
        </h2>
      </div>
      <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
        <div class="card-body">
          Alle Daten, welche ihr bei uns, zum Beispiel in eurem Nutzer*in Profil hinterlegt, werden nicht an Dritte weitergegeben.
          Es besteht aber für euch die Möglichkeit, eure Informationen, bei einem bestätigten Hilfegesuch/-angebot an den/die Vertragspartner*in freizugeben.
        </div>
      </div>
    </div>

    <div class="card">
      <div class="card-header" id="headingThree">
        <h2 class="mb-0">
          <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            Wie ist der allgemeine Ablauf?
          </button>
        </h2>
      </div>
      <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
        <div class="card-body">
          Dafür haben wie im Bereich “Guidelines” bereits einige Dinge für euch vorbereitet. Natürlich kann man den Ablauf aber nicht verallgemeinern, da jede Situation
          unterschiedlich ist. Dabei kommt es dann darauf, dass man sich möglichst genau mit dem anderen Menschen austauscht.
        </div>
      </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingFour">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
              Welche Tiere können hier vermittelt werden?
            </button>
          </h2>
        </div>
      <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordionExample">
        <div class="card-body">
          Prinzipiell kann jede Spezies auf dieser Plattform vermittelt werden. Natürlich geht das Ganze aber nur, wenn auch genügend Menschen diese Plattform nutzen.
          Es will nämlich nicht jeder eine Spinne bei sich aufnehmen. Solltest deine gesucht Spezies nicht gelistet sein, wende dich bitter per E-Mail an den Support, dann wird diese hinzugefügt.
        </div>
      </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingFive">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
              In meiner Nähe gibt es keine Hilfegesuche, was tun?
            </button>
          </h2>
        </div>
        <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordionExample">
          <div class="card-body">
            Dies liegt daran, dass in deiner Nähe zu wenig Menschen diese Plattform nutzen. Wenn du die Möglichkeit besitzt, kannst du natürlich auch Tiere von einer größeren Distanz abholen.
            Was in diesem Fall natürlich auch Hilft, ist es für diese Plattform in deinem Umfeld Werbung für uns zu machen.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingSix">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseSix" aria-expanded="false" aria-controls="collapseSix">
              Wie sicher ist die Tiervermittlung?
            </button>
          </h2>
        </div>
        <div id="collapseSix" class="collapse" aria-labelledby="headingSix" data-parent="#accordionExample">
          <div class="card-body">
            Darüber kann man keine allgemeine Aussage treffen. Wir sind lediglich eine Plattform um Menschen zusammen zu bringen. Alles andere muss von den Beteiligten geklärt werden.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingSeven">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseSeven" aria-expanded="false" aria-controls="collapseSeven">
              Wer haftet im Schadensfall?
            </button>
          </h2>
        </div>
        <div id="collapseSeven" class="collapse" aria-labelledby="headingSeven" data-parent="#accordionExample">
          <div class="card-body">
            Wir übernehmen keine Haftung für Schadensfälle, welche durch die Tiervermittlung entstehen.
            Wir sind lediglich eine Plattform, die die Menschen zusammenbringt. Alles was danach passiert, liegt in den Händen der Beteiligten.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingEigth">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseEight" aria-expanded="false" aria-controls="collapseEigth">
              Wie finanziert ihr euch?
            </button>
          </h2>
        </div>
        <div id="collapseEight" class="collapse" aria-labelledby="headingEigth" data-parent="#accordionExample">
          <div class="card-body">
            Wir sind über den Hackathon “WirVsVirus” der Bundesregierung entstanden und haben dadurch noch Ressourcen zur Verfügung.
            Sobald dieses aufgebraucht sind, wird die Webseite hoffentlich durch Spenden finanziert.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingNine">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseNine" aria-expanded="false" aria-controls="collapseNine">
              Was tun, wenn es Probleme bei der Vermittlung gibt?
            </button>
          </h2>
        </div>
        <div id="collapseNine" class="collapse" aria-labelledby="headingNine" data-parent="#accordionExample">
          <div class="card-body">
            Bei Problemen während der Vermittlung solltest du auf jeden fall auf Nummer sicher gehen, denn es geht ja im Zweifelsfall um dein liebsten Begleiter.
            Bei Problemen kannst du auch zunächst uns kontaktieren und um Hilfe bitten. Solltest du aber kriminelle Absichten vermuten, dann kontaktiere bitte die Örtliche Polizeidienststelle!
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingTen">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseTen" aria-expanded="false" aria-controls="collapseTen">
              Muss ich zwingend über die Plattform Kontakt aufbauen?
            </button>
          </h2>
        </div>
        <div id="collapseTen" class="collapse" aria-labelledby="headingTen" data-parent="#accordionExample">
          <div class="card-body">
            Nein musst du nicht. Du kannst auch direkt mit der Person telefonieren, oder die Person in einem anderen Messenger kontaktieren.
            Es besteht aber auch die Möglichkeit, dies über unsere Seite zu tun. Bitte markiere dein Hilfegesuch trotzdem als erfolgreich, wenn die Kontaktaufnahme geklappt hat.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingEleven">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseEleven" aria-expanded="false" aria-controls="collapseEleven">
              Was mache ich, wenn ich selbst auch Krank werde?
            </button>
          </h2>
        </div>
        <div id="collapseEleven" class="collapse" aria-labelledby="headingEleven" data-parent="#accordionExample">
          <div class="card-body">
            Dafür solltest du eine weitere Person angeben, welche sich im Ernstfall um das weitere Vorgehen für dich kümmern kann.
          </div>
        </div>
    </div>

    <div class="card">
        <div class="card-header" id="headingTwelve">
          <h2 class="mb-0">
            <button class="btn btn-link collapsed QuestionBox" type="button" data-toggle="collapse" data-target="#collapseTwelve" aria-expanded="false" aria-controls="collapseTwelve">
              Wie kann ich euch unterstützen?
            </button>
          </h2>
        </div>
        <div id="collapseTwelve" class="collapse" aria-labelledby="headingTwelve" data-parent="#accordionExample">
          <div class="card-body">
            Man kann uns mit freiwilliger Werbung (im legalen Rahmen) unterstützen. Solltest du Webdesigner*in sein und dich mit Vue.js und/oder Django auskennen,
            kannst du uns auch per E-Mail kontaktieren und uns bei der (Weiter-) Entwicklung der Webseite behilflich sein.
          </div>
        </div>
    </div>

  </div> <!--Accordion Ende !-->

</div>
</template>

<script>
export default {
  title: 'Quarantiere - FAQ'
}
</script>

<style scoped>
  .wrapper{
    width: 1280px;
    margin: 0 auto;
  }

  .QuestionBox{
    background: #2c4e57;
    color: white;
  }
</style>
