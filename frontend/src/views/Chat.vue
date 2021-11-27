<template>
  <div>
    <label for="rem">Seu nome:</label>
    <input type="text" name="" id="rem" :value="nome" required readonly />
    <label for="mensagem">Mensagem</label>
    <input type="text" name="" id="mensagem" required />
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
import { mapState } from "vuex";

export default {
  name: "Chat",
  data() {
    return {
      mensagens: [],
    };
  },
  computed: mapState({
    nome: state => state.chat.user_name,
    token: state => state.chat.access_token,
  }),
  methods: {
    async enviar() {
      const msg = document.querySelector("#mensagem").value;
      const rem = document.querySelector("#rem").value;

      const payload = new FormData();

      payload.append("rem", rem);
      payload.append("n_message", msg);

      const config = {
        headers: { Authorization: `Bearer ${this.token}` },
      };

      await this.$axios
        .post("http://localhost:8000/api_v2/post", payload, config)
        .then((response) => console.log(response.data.status))
        .catch((error) => console.log(error));

      this.atualizar();
    },
    async atualizar() {
      const config = {
        headers: { Authorization: `Bearer ${this.token}` },
      };
      await this.$axios
        .get("http://localhost:8000/api_v2/", config)
        .then((response) => (this.mensagens = response.data.mensagens))
        .catch((error) => console.log(error));
    },
  },
  mounted() {
    this.nome = this.$store.state.user_name;
    this.atualizar();

    setInterval(this.atualizar, 5000);
  },
};
</script>

<style>
</style>