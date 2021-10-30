<template>
  <div>
    <input type="file" name="arquivo" id="arquivo" /><br />

    <button @click="onClick">Enviar</button>

    <hr />
    <div class="flexcont">
      <img
        style="width: 10%; height: auto"
        v-for="(imagem, key) in imagens"
        :key="key"
        :src="`http://localhost:5000/upload/img/${imagem}`"
        alt=""
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "FormularioUpload",
  data() {
    return {
      imagens: [],
    };
  },
  methods: {
    async onClick() {
      const payload = new FormData();

      const arquivo = document.querySelector("#arquivo").files[0];

      payload.append("arquivo", arquivo);

      await this.$axios
        .post("http://localhost:5000/upload/save", payload)
        .then((response) => console.log(response.data.status))
        .catch((error) => console.log(error));
      this.atualiza();
    },
    async atualiza() {
      await this.$axios
        .get("http://localhost:5000/upload/")
        .then((response) => (this.imagens = response.data.imagens));
    },
  },
  mounted() {
      this.atualiza();
  },
};
</script>

<style>
div.flexcont {
  display: flex;
  flex-direction: row;
}
</style>