export default {
    namespaced: true,
    state: {
        funcionando: false,
        liga: false,
        valor: 1500,
        pos: 0,
        botao: 'Iniciar',
        tema: 0,
    },
    mutations: {
        LIGA_DESLIGA: state => {
            state.liga = !state.liga
        },
        BOTAO: (state, texto) => {
            state.botao = texto
        },
        VALOR_DEC: state => {
            state.valor--
        },
        VALOR_SET: (state, val) => {
            state.valor = val
        },
        JA_FUNCIONA: (state) => {
            state.funcionando = true
        },
        TEMA: (state, num) => {
            state.tema = num
        },
        POS_INC: (state) => {
            state.pos++
        },
        POS_INI: (state) => {
            state.pos = 0
        }
    },
    actions: {
        iniciar(context, obj) {
            if (!context.state.funcionando) {
                setInterval(() => {
                    if (context.state.liga == true) {
                        if (context.state.valor > 0) {
                            context.commit('VALOR_DEC')
                        }
                    }
                    if (context.state.valor <= 0) {
                        obj.muda()
                    }
                }, 1000);
            }
        },
        clique(context, payload) {
            context.commit('LIGA_DESLIGA')
            context.commit('BOTAO', payload)
            context.commit('JA_FUNCIONA')
        },
        diminui(context) {
            if (context.state.valor > 0) {
                context.commit('VALOR_DEC')
            }
        },
        muda_tema(context, pos) {
            context.commit('TEMA', pos)
        },
        fim_contagem(context, length) {
            context.commit('POS_INC')
            if (context.state.pos > length - 1) {
                context.commit('POS_INI');
                context.commit('BOTAO', "INICIAR");
            }
        },
        set_valor(context, val) {
            context.commit('VALOR_SET', val);
        }
    }
}