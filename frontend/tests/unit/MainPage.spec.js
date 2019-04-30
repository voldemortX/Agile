import Vue from 'vue'
import mainPage from '@/views/MainPage.vue'
import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import '../../src/plugins/element.js'
import VueResource  from 'vue-resource'

describe('MainPage.vue', () => {

    it('succeed in new system',done =>{
        const $route = {
          path:'/new',
          name:'_new'
        };
        const constructor = shallowMount(mainPage,{
          mocks:{
            $route
          }
        });
        const buttons = constructor.findAll('el-button-stub');
        const newbutton = buttons.at(0);
        newbutton.trigger('click');
        setTimeout(function () {
            expect(constructor.vm.$route.name).to.equal('_new');
            done();
        }, 2000);
    }
  )
})
