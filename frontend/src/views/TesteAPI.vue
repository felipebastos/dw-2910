<template>
  <div>
    <h1>A mensagem! Ah a mensagem!</h1>
    <br />
    <br />
    <span v-if="!chegou">Não temos mensagem ainda</span>
    <span v-else>{{ mensagem }}</span>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TesteAPI",
  data() {
    return {
      chegou: false,
      mensagem: "",
    };
  },
  async mounted () {
    await axios.get("http://localhost:5000/api_v1/")
      .then(response => (this.mensagem = response.data.mensagem))
      .catch(function(error){
          console.log(error);
      });
    this.chegou = true;
  },
};
</script>

<style>
</style>