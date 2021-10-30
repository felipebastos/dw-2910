import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TesteAPI from '../views/TesteAPI.vue'
import Upload from '../views/Upload.vue'
import Chat from '../views/Chat.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/mensagem',
    name: 'Mensagem',
    component: TesteAPI
  },
  {
    path: '/upload',
    name: 'Upload',
    component: Upload
  },
  {
    path: '/chat',
    name: 'Chat',
    component: Chat
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
