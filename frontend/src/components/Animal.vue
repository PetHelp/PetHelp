<template>
    <div>
        <!--<Avatar :img="animal.img" />-->
        <h3 class="h5 text-center mt-3">{{animal.name}}</h3>
    </div>
</template>

<script>
// import Avatar from '../components/Avatar.vue'

export default {
  name: 'Animal',
  props: ['animal'] // ,
//  components: { Avatar }
}
</script>
