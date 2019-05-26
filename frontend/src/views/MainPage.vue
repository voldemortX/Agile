<template>
    <div>
        <el-container>
            <el-header style="text-align: center; vertical-align:middle;font-size: 40px;height:100px">
                <el-row></el-row>
                <span>风险评估系统</span>
            </el-header>
            <el-main style="text-align: center; background-color:#000000">
                <el-button type="primary" @click="dialogFormVisible = true">新建 +</el-button>
            </el-main>
        </el-container>
        <el-container>
            <el-header style="text-align: center; font-size: 24px;background-color:#DCDCDC;color:#000000;height:70px">
                <span>已评估系统</span>
            </el-header>
            <el-main>
                <el-table :data="tableSys" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                    <el-table-column prop="systemname" label="SystemID" width="250">
                    </el-table-column>
                    <el-table-column prop="method" label="Method" width="140">
                    </el-table-column>
                    <el-table-column prop="results" label="Result" width="100">
                        <template slot-scope="scope">
                            <el-button type="text" @click.native="result(scope.$index)" size="small" style="font-size:14px;width:38px;height:20px">查看详情</el-button>
                        </template>
                    </el-table-column>
                    <el-table-column prop="createtime" label="CreateTime" width="200">
                    </el-table-column>
                    <el-table-column prop="description" label="Description" >
                    </el-table-column>
                    <el-table-column fixed="right" label="操作" width="180">
                        <template slot-scope="scope">
                            <el-button @click.native="ModifyClick(scope.row)" type="text" size="small" style="font-size:16px;width:38px;height:20px">修改</el-button>
                            <el-button @click.native="DelClick(scope.$index,scope.row)" type="text" size="small" style="font-size:16px;width:38px;height:20px">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
        <el-dialog title="评估结果" :visible.sync="resultDialogVisible" :modal-append-to-body="false">
            <el-table :data="assessresults" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                <el-table-column prop="asset" label="资产名称" width="140"></el-table-column>
                <el-table-column prop="threat" label="威胁名称" width="140"></el-table-column>
                <el-table-column prop="vulnerability" label="脆弱性名称" width="140"></el-table-column>
                <el-table-column prop="level" label="风险等级" width="140"></el-table-column>
            </el-table>
        </el-dialog>

        <el-dialog title="输入系统名称" :visible.sync="dialogFormVisible" :modal-append-to-body="false">
            <el-form :model="newsys">
                <el-form-item label="系统名称" :label-width="formLabelWidth">
                    <el-input v-model="newsys.name" auto-complete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false" style="font-size:16px;width:75px;height:40px">取 消</el-button>
                <el-button type="primary" @click.native="getnew()" style="font-size:16px;width:75px;height:40px">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: 'mainPage',
        methods: {
            ModifyClick(row) {//进入该系统的编辑页
                this.$router.push({name:'new',query:{sysname:row.systemname}})
            },
            DelClick(index,row){//删除系统
                this.$http.delete('http://134.175.225.180:3000/mock/43/sys/delete' /*'/sys/delete'*/,{
                    emulateJSON: true,
                    body: JSON.stringify({systemname:row.sysname})
                }).then(
                    (response) => {
                        if(response.ok && response.body.status === 0)
                        {
                            this.tableSys.splice(index, 1);
                        }
                        else{
                            this.errorMessage = response.body.error;
                        }
                    },
                    (error) => {
                        this.errorMessage = error.body.error;
                    }
                );
            },
            result(index){//弹出结果
                this.assessresults.forEach((i)=>{
                    this.assessresults.splice(i,this.assessresults.length);
                });
                for(let i=0;i<this.tempresults[index].length;i++){
                    this.assessresults.push(this.tempresults[index][i]);
                }

                this.resultDialogVisible = true;
            },
            getnew(){//进入新建系统页
                //dialogFormVisible = false,
                this.$router.push({name:'new',query:{sysname:this.newsys.name}});
            }
        },
        data(){
            return{
                tableSys: [/*{
    systemname:'system1',
    method:'矩阵法',
    results:'5',
    createtime:'2019/04/25 10:20:00',
    description:'blablablabla'}*/],
                resultDialogVisible: false,
                dialogFormVisible : false,
                newsys:{
                    name:''
                },
                assessresults:[/*{
        asset:'a',
        threat:'t',
        vulnerability:'v',
        level:'1'
    }*/],
                tempresults: []
                //tempresults:this.GLOBAL.tempresults
            }
        },

        mounted:function()
        {//显示数据
            this.$http.get('http://134.175.225.180:3000/mock/43/sys/fetch_all' /*'/sys/fetch_all'*/)
                .then(
                    (response) => {
                        if(response.ok && response.body.status === 0)
                        {
                            //this.tableSys = response.body.systems;
                            for(let i = 0; i < response.body.systems.length;i++ )
                            {
                                let temp = {};
                                temp.systemname = response.body.systems[i].systemname;
                                temp.method = response.body.systems[i].method;
                                temp.createtime = response.body.systems[i].createtime;
                                temp.description = response.body.systems[i].description.replace('&&&', '; ').replace('&&&', '; ').replace('&&&', '');
                                this.tableSys.push(temp);
                                //console.log(response.body.systems[i].results);
                            }
                            for(let i = 0; i < response.body.systems.length;i++ )
                            {
                                this.tempresults.push(response.body.systems[i].results.tva_results);
                            }
                        }
                        else{
                            this.errorMessage = response.body.error;
                        }
                    },
                    (error) => {
                        this.errorMessage = error.body.error;
                    }
                );
        }
    }
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
