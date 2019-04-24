import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
import MainPage from './views/MainPage.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/main',
      name: 'mainPage',
      component: MainPage
    }
  ]
})
