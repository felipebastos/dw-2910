<template>
  <div>
    <div id="cartao" class="card overflow-auto">
      <menumodoro :appname="name" v-on:swapcolors="mudacores"></menumodoro>
      <clockmodoro :valor="valor" :status="liga"></clockmodoro>
      <botaomodoro v-on:clique="clicado" :label="botao"></botaomodoro>
    </div>
    <audio src="@/assets/alarm.wav" id="alarm" loop></audio>
  </div>
</template>

<script>
import Menumodoro from "./Menumodoro.vue";
import Clockmodoro from "./Clockmodoro.vue";
import Botaomodoro from "./Botaomodoro.vue";

import { mapState, mapActions } from "vuex";

export default {
  name: "Vuemodoro",
  components: {
    Menumodoro,
    Clockmodoro,
    Botaomodoro,
  },
  data() {
    return {
      name: "Vuemodoro",
      valorSeq: [1500, 300, 1500, 1500, 300, 1800],
      botaoSeq: ["Pausar", "Continuar"],
    };
  },
  methods: {
    ...mapActions([
      "clock/clique",
      "clock/diminui",
      "clock/muda_tema",
      "clock/fim_contagem",
      "clock/set_valor",
      "clock/iniciar",
    ]),
    clicado() {
      this["clock/clique"](this.botaoSeq.at(this.liga));

      const alarm = document.querySelector("#alarm");
      alarm.pause();
    },
    muda() {
      this["clock/clique"](this.botaoSeq.at(1));

      const alarm = document.querySelector("#alarm");
      alarm.play();

      this["clock/fim_contagem"](this.valorSeq.length);
      this["clock/set_valor"](this.valorSeq.at(this.pos));
    },
    mudacores() {
      const temas = [
        { fg: "text-white", bg: "bg-danger" },
        { fg: "text-dark", bg: "bg-white" },
        { fg: "text-success", bg: "bg-white" },
        { fg: "text-primary", bg: "bg-white" },
        { fg: "text-white", bg: "bg-dark" },
        { fg: "text-dark", bg: "bg-warning" },
      ];

      const cartao = document.querySelector("#cartao");
      cartao.classList.remove(temas.at(this.tema).fg);
      cartao.classList.remove(temas.at(this.tema).bg);

      let pick = this.tema;
      do {
        pick = Math.floor(Math.random() * temas.length);
      } while (pick === this.tema);
      this["clock/muda_tema"](pick);

      cartao.classList.add(temas.at(this.tema).fg);
      cartao.classList.add(temas.at(this.tema).bg);
    },
  },
  mounted() {
    const temas = [
      { fg: "text-white", bg: "bg-danger" },
      { fg: "text-dark", bg: "bg-white" },
      { fg: "text-success", bg: "bg-white" },
      { fg: "text-primary", bg: "bg-white" },
      { fg: "text-white", bg: "bg-dark" },
      { fg: "text-dark", bg: "bg-warning" },
    ];

    const cartao = document.querySelector("#cartao");
    cartao.classList.add(temas.at(this.tema).fg);
    cartao.classList.add(temas.at(this.tema).bg);

    if (!this.funcionando) {
      this["clock/iniciar"](this);
    }
  },
  computed: mapState({
    liga: (state) => state.clock.liga,
    valor: (state) => state.clock.valor,
    pos: (state) => state.clock.pos,
    botao: (state) => state.clock.botao,
    tema: (state) => state.clock.tema,
    funcionando: (state) => state.clock.funcionando,
  }),
};
</script>

<style scoped>
div.card {
  height: calc(100vh - 59px);
}
</style>
