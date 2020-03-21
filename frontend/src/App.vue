<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/hilfe-suchen">Hilfe suchen</router-link> |
      <router-link to="/hilfe-anbieten">Hilfe anbieten</router-link> |
      <router-link to="/guideline">Guideline</router-link> |
      <router-link to="/faq">FAQ</router-link> |
      <router-link to="/profil">Profil</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
