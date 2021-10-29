<template>
  <div>
    <div id="cartao" class="card text-white bg-danger overflow-auto">
      <menumodoro :appname="name" v-on:swapcolors="mudacores"></menumodoro>
      <clockmodoro :valor="valor" :status="liga"></clockmodoro>
      <botaomodoro v-on:clique="clicado" :label="botao"></botaomodoro>
    </div>
    <audio src="@/assets/alarm.wav" id="alarm" loop></audio>
  </div>
</template>

<script>
import Menumodoro from './Menumodoro.vue';
import Clockmodoro from './Clockmodoro.vue';
import Botaomodoro from './Botaomodoro.vue';

export default {
  name: 'Vuemodoro',
  components: {
    Menumodoro,
    Clockmodoro,
    Botaomodoro,
  },
  data() {
    return {
      name: 'Vuemodoro',
      liga: false,
      valor: 1500,
      pos: 0,
      botao: 'Iniciar',
      valorSeq: [1500, 300, 1500, 300, 1500, 1800],
      botaoSeq: ['Pausar', 'Continuar'],
      tema: 0,
    };
  },
  methods: {
    clicado() {
      this.botao = this.botaoSeq.at(this.liga);
      this.liga = !this.liga;

      const alarm = document.querySelector('#alarm');
      alarm.pause();
    },
    muda() {
      this.botao = this.botaoSeq.at(1);
      this.liga = false;

      const alarm = document.querySelector('#alarm');
      alarm.play();

      this.pos += 1;
      if (this.pos > this.valorSeq.length - 1) {
        this.pos = 0;
        this.botao = 'Iniciar';
      }
      this.valor = this.valorSeq.at(this.pos);
    },
    mudacores() {
      const temas = [
        { fg: 'text-white', bg: 'bg-danger' },
        { fg: 'text-dark', bg: 'bg-white' },
        { fg: 'text-success', bg: 'bg-white' },
        { fg: 'text-primary', bg: 'bg-white' },
        { fg: 'text-white', bg: 'bg-dark' },
        { fg: 'text-dark', bg: 'bg-warning' },
      ];

      const cartao = document.querySelector('#cartao');
      cartao.classList.remove(temas.at(this.tema).fg);
      cartao.classList.remove(temas.at(this.tema).bg);

      let pick = this.tema;
      do {
        pick = Math.floor(Math.random() * (temas.length));
      } while (pick === this.tema);
      this.tema = pick;

      cartao.classList.add(temas.at(this.tema).fg);
      cartao.classList.add(temas.at(this.tema).bg);
    },
  },
  mounted() {
    setInterval(() => {
      if (this.liga === true) {
        this.valor -= 1;
      }
      if (this.valor <= 0) {
        this.muda();
      }
    }, 1000);
  },
};
</script>

<style scoped>
div.card {
  height: calc(100vh - 59px);
}
</style>
