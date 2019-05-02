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
                            <el-input name="username" prefix-icon="el-icon-arrow-right" size="medium" v-model="username" placeholder="用户名"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-input name="password" prefix-icon="el-icon-arrow-right" size="medium" v-model="password" type="password" placeholder="密码"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button name="login" type="success" round @click.native=login_click>登录</el-button>
                            <el-button name="register" round plain @click.native=register_click>注册</el-button>
                            <p class="error">{{errorMessage}}</p>
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
        name: 'login',
        data(){
            return{
                labelPosition: 'right',
                username: '',
                password: '',
                errorMessage: ''

            }
        },

        methods:{
            dump: function() {
                // self-explainable
                this.username = '';
                this.password = '';
            },

            register_click: function() {
                this.$http({
                    method: 'POST',
                    url: 'http://localhost:7777/auth/register',
                    params: {
                        username: this.username,
                        password: this.password
                    }
                }).then(
                    (response) => {
                        // success
                        if (response.ok && response.body.status === 0) {
                            this.errorMessage = '注册成功！';
                        } else {
                            this.errorMessage = response.body.error;
                        }
                    },
                    (error) => {
                        // error?
                        this.errorMessage = error.body.error;
                    }
                );
            },

            login_click: function() {
                this.$http({
                    method: 'POST',
                    url: 'http://localhost:7777/auth/login',
                    params: {
                        username: this.username,
                        password: this.password
                    }
                }).then(
                    (response) => {
                        // success
                        if (response.ok && response.body.status === 0) {
                            this.$router.push({path: '/mainPage'});
                        } else {
                            this.errorMessage = response.body.error;
                        }
                    },
                    (error) => {
                        // error?
                        this.errorMessage = error.body.error;
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
    .error {
        color: red;
    }

</style>