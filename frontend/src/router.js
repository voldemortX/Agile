import Vue from 'vue'
import Router from 'vue-router'
import login from './views/Login.vue'
import mainPage from './views/MainPage.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/mainPage',
      name: 'mainPage',
      component: mainPage
    }
  ]
})
