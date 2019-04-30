<template>
  <div>
    <el-container>
      <el-header style="text-align: center; vertical-align:middle;font-size: 40px;height:100px">
      <el-row></el-row>
        <span>风险评估系统</span>
      </el-header>
      <el-main style="text-align: center; background-color:#000000">
        <el-button type="primary" @click="getnew()">新建 +</el-button>
      </el-main>
  </el-container>
    <el-container>
      <el-header style="text-align: center; font-size: 24px;background-color:#DCDCDC;color:#000000;height:70px">
        <span>已评估系统</span>
      </el-header>
      <el-main>
        <el-table :data="tableData" border :header-cell-style="{background:'#FFFFFF'}":cell-style="{background:'#FFFFFF'}">
          <el-table-column prop="systemname" label="SystemID" width="250">
          </el-table-column>
          <el-table-column prop="method" label="Method" width="140">
          </el-table-column>
          <el-table-column prop="results" label="Result" width="100">
          </el-table-column>
          <el-table-column prop="createtime" label="CreateTime" width="200">
          </el-table-column>
          <el-table-column prop="description" label="Description" >
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="180">
            <template slot-scope="scope">
              <el-button @click="handleClick(scope.row)" type="text" size="small" style="font-size:16px;width:38px;height:20px">修改</el-button>
              <el-button type="text" size="small" style="font-size:16px;width:38px;height:20px">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>

  </div>
</template>

<script>
export default {
name: 'mainPage',
methods: {
handleClick(row) {//进入该系统的编辑页
    this.$http.get('/new?'+row.systemname)
  .then((response)=>{
      console.log(response)
  })
  .catch((error) => {
      console.log(error);
  })
},
getnew(){//进入新建系统页
  /*this.$http.get('/new')
      .then((response) => {
                        if (response.body.status === 0) {
                            this.$router.push({path: '/new'});
                        } else {
                            alert(response.body.error);
                        }
                    },
                    (error) => {
                        // error
                        this.dump();
                        alert(error);
                    });*/
  this.$router.push({path: '/new'});
  }
},
data(){
  return{
    tableData: [{
    systemname:'system1',
    method:'矩阵法',
    results:'5',
    createtime:'2019/04/25 10:20:00',
    description:'blablablabla'}]
  }
  }

};
</script>


<style scoped>
.el-button{
  width:150px;
  height:60px;
  font-size:24px;
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
.el-aside {
  color: #333;
}
.el-row
{
  height:23px;
}
</style>
