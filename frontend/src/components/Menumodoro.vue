<template>
  <div>
      <div class="card-header">
        <div class="row justify-content-between">
          <div class="col-8">
            <h1><span class="fas fa-pepper-hot"></span> {{appname}}</h1>
          </div>
          <div class="col-2">
            <h2><span @click="colors" class="fas fa-palette"></span></h2>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Menumodoro',
  props: ['appname'],
  methods: {
    colors() {
      this.$emit('swapcolors');
    },
  },
};
</script>

<style scoped>
</style>
