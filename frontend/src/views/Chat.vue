<template>
  <div>
    <label for="rem">Seu nome:</label>
    <input type="text" name="" id="rem" value="Anônimo" required>
    <label for="mensagem">Mensagem</label>
    <input type="text" name="" id="mensagem" required>
    <button @click="enviar">Enviar</button>
    <hr />
    <ul>
      <li v-for="(mensagem, k) in mensagens" :key="k">
        {{ mensagem.remetente }} disse: {{ mensagem.texto }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Chat",
  data() {
    return {
      mensagens: [],
    };
  },
  methods: {
    async enviar() {
      const msg = document.querySelector("#mensagem").value;
      const rem = document.querySelector("#rem").value;

      const payload = new FormData();
      
      payload.append('rem', rem)
      payload.append("n_message", msg);

      await this.$axios
        .post("http://localhost:5000/api_v2/put", payload)
        .then((response) => console.log(response.data.status))
        .catch((error) => console.log(error));

      this.atualizar();
    },
    async atualizar() {
      await this.$axios
        .get("http://localhost:5000/api_v2/")
        .then((response) => (this.mensagens = response.data.mensagens))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
      this.atualizar();
  },
};
</script>

<style>
</style>