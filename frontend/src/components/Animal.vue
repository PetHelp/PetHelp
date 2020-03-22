<template>
    <div>
        <Avatar :img="animal.img" />
        <h3 class="h5 text-center mt-3">{{animal.name}} ({{ animal.age }})</h3>
        <p v-if="animal.hometown" class="text-center">{{animal.hometown}}</p>
    </div>
</template>

<script>
import Avatar from '../components/Avatar.vue'

export default {
  name: 'Animal',
  props: ['animal'],
  components: { Avatar }
}
</script>
