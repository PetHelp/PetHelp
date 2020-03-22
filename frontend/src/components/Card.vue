<template>
  <div class="user__card p-3 pb-4">
    <div class="card__avatar mx-auto">
      <Avatar :img="user.img" />
    </div>
    <h3 class="h5 text-center mt-3">{{user.name}}</h3>
    <p v-if="user.hometown" class="text-center">
      {{user.hometown}}<span v-if="user.animals" class=" mt-3">, {{user.animals.length}} <span v-if="user.animals.length > 1">Tiere</span><span v-else>Tier</span></span>
    </p>
    <p v-if="user.experience" class=" mt-3">{{user.experience}}</p>
    <div class="text-center">
      <button class="btn btn-cta px-4 py-2 mt-2">{{user.givenName}} kontaktieren</button>
    </div>
  </div>
</template>

<style>
  .user__card {
    display: flex;
    flex-direction: column;
    border: 1px solid #ccc;
    border-radius: 10px;
  }

  .card__avatar {
    width: 80%;
    margin-top: -3em;
  }

  .btn.btn-cta {
    border-radius: 10px;
    background-color: #2c4e57;
    color: white;
    font-weight: bold;
  }

  .btn.btn-cta:hover,
  .btn.btn-cta:focus {
    background: #0f1b1f;
    color: white;
  }
</style>

<script>
import Avatar from '../components/Avatar.vue'

export default {
  name: 'Card',
  props: ['user'],
  components: { Avatar }
}
</script>
