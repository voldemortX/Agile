import Vue from 'vue'
import Router from 'vue-router'
import login from './views/Login.vue'
import mainPage from './views/MainPage.vue'
import _new from './views/New.vue'

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
    },
    {
      path: '/new',
      name: 'new',
      component: _new
    }
  ]
})
