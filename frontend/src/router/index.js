import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TesteAPI from '../views/TesteAPI.vue'
import Upload from '../views/Upload.vue'
import Chat from '../views/Chat.vue'
import Login from '../views/Login.vue'
import Cadastro from '../views/Cadastro.vue'

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
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/cadastro',
    name: 'Cadastro',
    component: Cadastro
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
