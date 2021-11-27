<template>
  <div>
      <input type="text" id="nome"><br>
      <input type="password" id="senha"><br>
      <button @click="cadastrar">Cadastrar</button>
  </div>
</template>

<script>
export default {
    name: 'Cadastro',
    methods: {
        async cadastrar() {
            const nome = document.querySelector('#nome').value;
            const senha = document.querySelector('#senha').value;

            const payload = new FormData();
            payload.append('nome', nome);
            payload.append('senha', senha);

            await this.$axios.post("http://localhost:8000/auth/register", payload)
            .then(response => (console.log(response.data.status)))
            .catch(error => (console.log(error)))
        },
    }
}
</script>

<style>

</style>