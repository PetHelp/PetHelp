<template>
  <div id="app" class="container-fluid">
    <div id="nav">
      <b-row align-h="center">
            <b-col align-self="center"><img src="http://via.placeholder.com/100x100"></b-col>
            <b-col align-self="center"><router-link to="/">Home</router-link></b-col>
            <b-col align-self="center"><router-link to="/hilfe-suchen">Hilfe suchen</router-link></b-col>
            <b-col align-self="center"><router-link to="/hilfe-anbieten">Hilfe anbieten</router-link></b-col>
            <b-col align-self="center"><router-link to="/guideline">Guideline</router-link></b-col>
            <b-col align-self="center"><router-link to="/faq">FAQ</router-link></b-col>
            <b-col align-self="center"><router-link to="/profil"><img style="width:50px" src="https://cdn2.iconfinder.com/data/icons/facebook-51/32/FACEBOOK_LINE-01-512.png"></router-link></b-col>
      </b-row>
    </div>
     <b-row>
        <router-view/>
    </b-row>

    <b-row>
      <b-col>
        Footer
      </b-col>
    </b-row>

  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  text-align: center;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
