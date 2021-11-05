
export default {
    namespaced: true,
    state: {
      user_name: '',
      access_token: '',
    },
    mutations: {
      UPDATE_TOKEN (state, nt) {
        state.access_token = nt
      },
      UPDATE_NAME (state, nn) {
        state.user_name = nn
      }
    },
    actions: {
      update_token(context, payload){
        context.commit('UPDATE_TOKEN', payload);
      },
      update_name({commit}, payload){
        payload = `USUÁRIO ${payload}`;
        commit('UPDATE_NAME', payload);
      }
    },
  }