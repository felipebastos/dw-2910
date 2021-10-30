<template>
  <div>
      <input type="text" id="nome"><br>
      <input type="password" id="senha"><br>
      <button @click="logar">Logar</button>
  </div>
</template>

<script>
export default {
    name: 'Login',
    methods: {
        async logar() {
            const nome = document.querySelector('#nome').value;
            const senha = document.querySelector('#senha').value;

            const payload = new FormData();
            payload.append('nome', nome);
            payload.append('senha', senha);

            const res = await this.$axios.post("http://localhost:5000/auth/login", payload)
            .then(response => {return response.data})
            .catch(error => (console.log(error)))
            
            this.$store.commit('update_token',res.access_token);
            this.$store.commit('update_name', nome);
        },
    }
}
</script>

<style>

</style>