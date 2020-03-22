<template>
  <div class="wrapper">
    <div class="wrapper">
      <div class="mb-3" style=" border-style: solid; border-width: 1px; border-color: #2c4e57;border-radius: 5px; padding: 1em;">
        <b style="font-size: 25px; text-decoration: underline black">Das Wichtigste zuerst:</b>
        <br/>Nach aktuellem Stand kann das Coronavirus <b>nicht</b> von Haustieren auf Menschen oder umgekehrt von Menschen auf Haustieren übertragen werden!
        <a
          href="https://www.bmel.de/DE/Ministerium/_Texte/corona-virus-faq-fragen-antworten.html#doc13796248bodyText6"
        >(Quelle zum BMEL)</a>
        <br />Diese Plattform und alle hier angebotenen Hilfen sind rein ehrenamtlich,
        <b>kommerzielle Angebote sind verboten!</b>
      </div>
    </div>

    <div class="accordion" id="accordionExample">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h2 class="mb-0">
            <button
              class="btn btn-link QuestionBox"
              type="button"
              data-toggle="collapse"
              data-target="#collapseOne"
              aria-expanded="true"
              aria-controls="collapseOne"
            >Was ist an hygienischen Maßnahmen zu beachten?</button>
          </h2>
        </div>
        <div
          id="collapseOne"
          class="collapse show"
          aria-labelledby="headingOne"
          data-parent="#accordionExample"
        >
          <div class="card-body">
            <ul>- Bestätigt infizierte Personen sollten den engen Kontakt zu ihren Haustieren, wie z. B. das Abschlecken des Gesichts durch die Tiere, vermeiden.</ul>
            <ul>- Im Idealfall sollte der direkte Kontakt zwischen Hilfe suchendem und helfenden vermieden werden. Die Übergabe von beispielsweise Hunden kann beispielsweise so erfolgen,
            dass der Hund aus dem Flur abgeholt wird (während der Halter sich in einem anderen Raum aufhält) oder der Hund im Treppenhaus angebunden und dann abgeholt wird. Außerdem gilt auch hier,
            Händewaschen nach Kontakt mit dem Tier, ggf. eigene Ausrüstung (beispielsweise Leine) mitbringen.</ul>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header" id="headingTwo">
          <h2 class="mb-0">
            <button
              class="btn btn-link collapsed QuestionBox"
              type="button"
              data-toggle="collapse"
              data-target="#collapseTwo"
              aria-expanded="false"
              aria-controls="collapseTwo"
            >Was ist bei der Pflege fremder Tiere zu beachten?</button>
          </h2>
        </div>
        <div
          id="collapseTwo"
          class="collapse"
          aria-labelledby="headingTwo"
          data-parent="#accordionExample"
        >
          <div class="card-body">
            <ul>- Es sollte im Vorfeld über mögliche Allergien und Krankheiten gesprochen werden. Ggf. muss über notwendige Medikamente gesprochen werden.</ul>
            <ul>- Bitte klären Sie im Vorfeld ab, was passiert wenn das Tier sich verletzt oder krank wird. Soll die Pflegestelle im Zweifelsfall direkt zum Tierarzt fahren und
            vom Tierarzt empfohlene Untersuchungen durchführen lassen? Oder regelt der Tierhalter in dem Fall alles Nötige?</ul>
            <ul>- Ein Futterwechsel sollte möglichst vermieden werden.</ul>
            <ul>- Besondere Eigenheiten des Tieres sollten geklärt werden. (Macht Dinge kaputt, Flieht gerne aus der Wohnung, mag keine Menschen mit Bart o.ä.)</ul>
            <ul>- Für den Notfall sollte mindestens eine weitere Kontaktperson angegeben werden. (Plötzlicher Krankenhausaufenthalt o.ä.)</ul>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header" id="headingThree">
          <h2 class="mb-0">
            <button
              class="btn btn-link collapsed QuestionBox"
              type="button"
              data-toggle="collapse"
              data-target="#collapseThree"
              aria-expanded="false"
              aria-controls="collapseThree"
            >Was ist bei Spaziergängen mit fremden Hunden zu beachten?</button>
          </h2>
        </div>
        <div
          id="collapseThree"
          class="collapse"
          aria-labelledby="headingThree"
          data-parent="#accordionExample"
        >
          <div class="card-body">
            <ul>- Die Hunde sollten nicht von der Leine gelassen werden, hier können Schleppleinen Abhilfe schaffen.</ul>
            <ul>- Kontakt mit anderen Hunden sollte wenn überhaupt nach Abfrage mit beiden Tierhaltern erfolgen (insbesondere dem Hilfesuchenden!).</ul>
            <ul>- Halten Sie sich an Absprachen! (Maulkorb o.ä.)</ul>
            <ul>- Zum Ausführen von Listenhunden müssen die Gassigeher in einigen Bundesländern Auflagen erfüllen. Ebenso gilt in einigen Bundesländern die 2040 Regel!</ul>
            <ul>- Für jeden Hund muss eine gültige Haftpflichtversicherung abgeschlossen sein, und der Hund sollte geimpft sein.</ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.wrapper {
  width: 1280px;
  margin: 0 auto;
}

.QuestionBox {
  background: #2c4e57;
  color: white;
}
</style>
