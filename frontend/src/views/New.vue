<template>
  <div>
  <el-container width="200px">
    <el-header style="text-align: center; vertical-align:middle;font-size: 40px;height:100px">
      <el-row></el-row>
      <span>风险评估</span>

    </el-header>
    <el-main style="text-align: center">
    <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="评估准备" name="first">
        <el-divider content-position="left">评估目标</el-divider>
        <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="aim"></el-input>
        <el-divider content-position="left">评估范围</el-divider>
        <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="range"></el-input>
        <el-divider content-position="left">组建团队成员</el-divider>
        <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="team"></el-input>
    </el-tab-pane>
    <el-tab-pane label="资产评估" name="second">
      <div style="float:left">
        <el-button type="add">添加</el-button>
        <el-button type="modify">修改</el-button>
        <el-button type="delete">删除</el-button>
      </div>
      <el-table :data="tableData" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
        <el-table-column prop="assets" label="资产名称" width="260">
        </el-table-column>
        <el-table-column prop="integrity" label="保密性" width="140">
        </el-table-column>
        <el-table-column prop="availability" label="可用性" width="140">
        </el-table-column>
        <el-table-column prop="confidentiality" label="完整性" width="140">
        </el-table-column>
        <el-table-column prop="assetvalue" label="资产价值" >
        </el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="脆弱性评估" name="third">
      <div style="float:left">
        <el-button type="add">添加</el-button>
        <el-button type="modify">修改</el-button>
        <el-button type="delete">删除</el-button>
      </div>
        <el-table :data="tableData" border :header-cell-style="{background:'#FFFFFF'}":cell-style="{background:'#FFFFFF'}">
          <el-table-column prop="vulnerability" label="脆弱性名称" width="260"></el-table-column>
          <el-table-column prop="vrank" label="脆弱性等级" width="140"></el-table-column>
          <el-table-column prop="va" label="资产关联" width="140"></el-table-column>
          <el-table-column prop="vdetails" label="描述"></el-table-column>
        </el-table>
    </el-tab-pane>
    <el-tab-pane label="威胁评估" name="fourth">
      <div style="float:left">
        <el-button type="add">添加</el-button>
        <el-button type="modify">修改</el-button>
        <el-button type="delete">删除</el-button>
      </div>
      <el-table :data="tableData" border :header-cell-style="{background:'#FFFFFF'}":cell-style="{background:'#FFFFFF'}">
        <el-table-column prop="threat" label="威胁名称" width="260"></el-table-column>
        <el-table-column prop="trank" label="威胁等级" width="140"></el-table-column>
        <el-table-column prop="tv" label="威胁的脆弱性关联" width="140"></el-table-column>
        <el-table-column prop="tdetails" label="描述"></el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
    </el-main>
</el-container>

</div>
</template>

<script>
export default {
  name: '_new',
  data() {
    return {
      aim: '',
      range: '',
      team: ''
    }
  },
  methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
};
</script>


<style scoped>
.el-button{
width:74px;
height:40px;
font-size:17px;
}
</style>
<style>
.el-header {
background-color: #000000;
color: #FFFFFF;
line-height: 70px;
}
.el-main {
background-color:#FFFFFF;
}
</style>
