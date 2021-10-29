<template>
  <div>
    <div class="card-body time">
      {{ display() }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Clockmodoro',
  props: {
    valor: Number,
    status: Boolean,
  },
  methods: {
    display() {
      const min = Math.floor(Number(this.valor / 60)).toString().padStart(2, '0');
      const sec = Number(this.valor % 60).toString().padStart(2, '0');
      return `${min}:${sec}`;
    },
  },
};
</script>

<style scoped>
div.time {
  font-size: 5em;
  text-align: center;
}
</style>
