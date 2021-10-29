<template>
  <div class="card-footer d-grid gap-2">
      <div class="btn btn-warning btn-lg" @click="clique"><h2>{{label}}</h2></div>
  </div>
</template>

<script>
export default {
  name: 'Botaomodoro',
  props: ['label'],
  methods: {
    clique() {
      this.$emit('clique');
    },
  },
};
</script>

<style scoped>
</style>
