import _new from '@/views/New.vue'
import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import '../../src/plugins/element.js'
import Vue from 'vue'
import VueResource  from 'vue-resource'

Vue.use(VueResource);


describe('New.vue', () => {
    // Only test core algorithms
    it('Can do multiply', () => {
        const $route = {
            query: {
                sysname: 'test'
            }
        };
        const wrapper = shallowMount(_new,{
            mocks: {
                $route
            }
        });
        wrapper.setData({
            tableAsset: [
                {asset: '测试资产5', confidentiality: '很高', integrity: '中', availability: '很低', rank: '很高', details: 'blabla'},
                {asset: '测试资产4', confidentiality: '高', integrity: '中', availability: '很低', rank: '高', details: 'blabla'}
            ],
            tableVul: [
                {vulnerability: '测试脆弱性5', rank: '很高', vaString: '测试资产5,测试资产4', va: ['测试资产5', '测试资产4'], details: 'bla'},
                {vulnerability: '测试脆弱性3', rank: '中', vaString: '测试资产5', va: ['测试资产5'], details: 'bla'}
            ],
            tableThreat: [
                {threat: '测试威胁3', rank: '中', tvString: '测试脆弱性5,测试脆弱性3', tv: ['测试脆弱性5', '测试脆弱性3'], details: 'bla'},
                {threat: '测试威胁1', rank: '很低', tvString: '测试脆弱性5', tv: ['测试脆弱性5'], details: 'bla'}
            ],
            systemname: 'test1',
            method: 0
        });
        const buttonCalc = wrapper.findAll('el-button-stub').at(0);
        buttonCalc.trigger('click');
        expect(wrapper.vm.$data.resultDialogVisible).to.equal(true);
        expect(JSON.stringify(wrapper.vm.$data.tva_results)).to.equal(JSON.stringify([
            {"asset":"测试资产5","vulnerability":"测试脆弱性5","threat":"测试威胁3","level":4},
            {"asset":"测试资产4","vulnerability":"测试脆弱性5","threat":"测试威胁3","level":4},
            {"asset":"测试资产5","vulnerability":"测试脆弱性5","threat":"测试威胁1","level":3},
            {"asset":"测试资产4","vulnerability":"测试脆弱性5","threat":"测试威胁1","level":2},
            {"asset":"测试资产5","vulnerability":"测试脆弱性3","threat":"测试威胁3","level":3}
            ]));
    });

    it('Can do matrix', () => {
        const $route = {
            query: {
                sysname: 'test'
            }
        };
        const wrapper = shallowMount(_new,{
            mocks: {
                $route
            }
        });
        wrapper.setData({
            tableAsset: [
                {asset: '测试资产5', confidentiality: '很高', integrity: '中', availability: '很低', rank: '很高', details: 'blabla'},
                {asset: '测试资产4', confidentiality: '高', integrity: '中', availability: '很低', rank: '高', details: 'blabla'}
            ],
            tableVul: [
                {vulnerability: '测试脆弱性5', rank: '很高', vaString: '测试资产5,测试资产4', va: ['测试资产5', '测试资产4'], details: 'bla'},
                {vulnerability: '测试脆弱性3', rank: '中', vaString: '测试资产5', va: ['测试资产5'], details: 'bla'}
            ],
            tableThreat: [
                {threat: '测试威胁3', rank: '中', tvString: '测试脆弱性5,测试脆弱性3', tv: ['测试脆弱性5', '测试脆弱性3'], details: 'bla'},
                {threat: '测试威胁1', rank: '很低', tvString: '测试脆弱性5', tv: ['测试脆弱性5'], details: 'bla'}
            ],
            systemname: 'test1',
            method: 1
        });
        const buttonCalc = wrapper.findAll('el-button-stub').at(0);
        buttonCalc.trigger('click');
        expect(wrapper.vm.$data.resultDialogVisible).to.equal(true);
        expect(JSON.stringify(wrapper.vm.$data.tva_results)).to.equal(JSON.stringify([
            {"asset":"测试资产5","vulnerability":"测试脆弱性5","threat":"测试威胁3","level":4},
            {"asset":"测试资产4","vulnerability":"测试脆弱性5","threat":"测试威胁3","level":4},
            {"asset":"测试资产5","vulnerability":"测试脆弱性5","threat":"测试威胁1","level":4},
            {"asset":"测试资产4","vulnerability":"测试脆弱性5","threat":"测试威胁1","level":4},
            {"asset":"测试资产5","vulnerability":"测试脆弱性3","threat":"测试威胁3","level":3}
        ]));
    });
});
