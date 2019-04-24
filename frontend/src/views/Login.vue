<template>
    <div>
        <el-row>
            <el-col :span="10"><div class="grid-content"></div></el-col>
            <el-col :span="4">
                <div class="bg-purple-dark">
                    <el-row>
                        <div>
                            <el-input size="medium" v-model="username" placeholder="Enter your name..."></el-input>
                        </div>
                    </el-row>
                    <el-row>
                        <div>
                            <el-input size="medium" v-model="password" type="password" placeholder="Enter your password..."></el-input>
                        </div>
                    </el-row>
                    <el-row>
                        <el-col :span="12">
                            <div>
                                <el-button @click=loginClick>登录</el-button>
                            </div>
                        </el-col>
                        <el-col :span="12">
                            <div>
                                <el-button @click=registerClick>注册</el-button>
                            </div>
                        </el-col>
                    </el-row>
                </div>
            </el-col>
            <el-col :span="10"><div class="grid-content"></div></el-col>
        </el-row>
    </div>
</template>


<script>
    export default {
        name: "Login",
        data(){
            return{
                username: "",
                password: ""

            }
        }
    }
</script>

<style scoped>
    .el-row {
        margin-bottom: 10px;
    }
    .el-col {
        border-radius: 4px;
    }
    .el-input {
        margin: 20px;
        width: 240px;
    }
    .el-button {
        margin: 20px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }

</style>