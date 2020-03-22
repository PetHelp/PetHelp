<template>
    <div class="avatar w-100 white d-flex justify-content-center align-items-center">
        <img
            :src="img"
            :alt="userName"
            class="img-fluid rounded-circle"
        />
    </div>
</template>

<script>
export default {
  name: 'Avatar',
  props: ['img', 'userName']
}
</script>
