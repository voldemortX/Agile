import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import '../../src/plugins/element.js'
import Vue from 'vue'
import VueResource  from 'vue-resource'
import login from '@/views/Login.vue'

Vue.use(VueResource);


describe('Login.vue', () => {
    it('Can register', done => {
        const wrapper = shallowMount(login);
        wrapper.setData({username: 'test', password: 'test'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(1);
        buttonLogin.trigger('click');
        setTimeout(function () {
            expect(wrapper.html()).to.contains('注册成功');
            done();
        }, 2000);
    });

    it('Can handle existed username when registering', done => {
        const wrapper = shallowMount(login);
        wrapper.setData({username: 'wrong1', password: 'test'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(1);
        buttonLogin.trigger('click');
        setTimeout(function () {
            expect(wrapper.html()).to.contains('用户名已被注册');
            done();
        }, 2000);
    });

    it('Can handle unknown error when registering', done => {
        const wrapper = shallowMount(login);
        wrapper.setData({username: 'wrong2', password: 'test'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(1);
        buttonLogin.trigger('click');
        setTimeout(function () {
            expect(wrapper.html()).to.contains('数据库未知错误');
            done();
        }, 2000);
    });

    it('Can handle nonexistent username', done => {
        const wrapper = shallowMount(login);
        wrapper.setData({username: 'wrong', password: 'test'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(0);
        buttonLogin.trigger('click');
        setTimeout(function () {
                expect(wrapper.html()).to.contains('用户名不存在');
                done();
            }, 2000);
    });

    it('Can handle wrong password', done => {
        const wrapper = shallowMount(login);
        wrapper.setData({username: 'test', password: 'wrong'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(0);
        buttonLogin.trigger('click');
        setTimeout(function () {
            expect(wrapper.html()).to.contains('用户名或密码输入错误');
            done();
        }, 2000);
    });

    it('Can login', done => {
        const $route = {
            path: '/mainPage',
            name: 'mainPage'
        };
        const wrapper = shallowMount(login,{
            mocks: {
                $route
            }
        });
        wrapper.setData({username: 'test', password: 'test'});
        const buttons = wrapper.findAll('el-button-stub');
        const buttonLogin = buttons.at(0);
        buttonLogin.trigger('click');
        setTimeout(function () {
            expect(wrapper.vm.$route.name).to.equal('mainPage');
            done();
        }, 2000);
    });
});