<template>
    <div class="top-align">
        <h1>风险评估系统</h1>
        <el-row>
            <el-col :span="10"><div class="grid-content"></div></el-col>
            <el-col :span="4">
                <div class="bg-light">
                    <el-row><div class="grid-content bg-dark"></div></el-row>
                    <el-form :label-position="labelPosition">
                        <el-form-item>
                            <el-input prefix-icon="el-icon-arrow-right" size="medium" v-model="username" placeholder="用户名"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-input prefix-icon="el-icon-arrow-right" size="medium" v-model="password" type="password" placeholder="密码"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="success" round @click=login_click>登录</el-button>
                            <el-button round plain @click=register_click>注册</el-button>
                        </el-form-item>
                    </el-form>
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
                labelPosition: "right",
                username: "",
                password: ""

            }
        },

        methods:{
            dump: function() {
                // self-explaintary
                this.username = "";
                this.password = "";
            },
            login_click: function() {
                // post name: str; pwd: str; memo: str(true or false)
                // 0->success; 1->doesn't match; 2->cookie doesn't exist or expired
                this.$http({
                    method: 'POST',
                    url: 'http://134.175.225.180:3000/mock/43/auth/login',
                    params: {
                        username: this.username,
                        password: this.password
                    }
                }).then(
                    (response) => {
                        // success
                        if (response.body.status === 0) {
                            this.$router.push({path: '/mainPage'});
                        } else {
                            alert(response.body.error);
                        }
                    },
                    (error) => {
                        // error
                        this.dump();
                        alert(error);
                    }
                );

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
        width: 200px;
    }
    .el-button {
        margin: 20px;
    }
    .bg-dark {
        background: #1976d2;
    }
    .bg-light {
        background: #2196F3;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    .top-align {
        margin-top: 10%;
    }

</style>