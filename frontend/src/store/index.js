import Vue from 'vue'
import Vuex from 'vuex'

import chat from '@/store/modules/chat'
import vuemodoro from '@/store/modules/vuemodoro'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    chat: chat,
    clock: vuemodoro
  }
})
