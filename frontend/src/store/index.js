import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_name: '',
    access_token: '',
  },
  mutations: {
    update_token (state, nt) {
      state.access_token = nt
    },
    update_name (state, nn) {
      state.user_name = nn
    }
  },
  actions: {
  },
  modules: {
  }
})
