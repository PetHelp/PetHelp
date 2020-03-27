<template>
    <div class="avatar w-100 white d-flex justify-content-center align-items-center">
      <div class="avatar__img-wrapper">
        <img
            :src="require(`../assets/Images/${img}`)"
            :alt="userName"
            class="avatar__img img-fluid rounded-circle"
        />
      </div>
    </div>
</template>

<script>
export default {
  name: 'Avatar',
  props: ['img', 'userName']
}
</script>

<style scoped>
  .avatar__img-wrapper {
    position: relative;
    width: 100%;
    overflow: hidden;
    padding-bottom: 100%;
  }

  .avatar__img {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    object-fit: cover;
    width: 100%;
    height: 100%;
    border: 3px solid #eee;
  }
</style>
