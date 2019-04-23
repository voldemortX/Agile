<template>
    <div>
        <ul>
            <li>
                <el-input v-model="username" placeholder="Enter your name..."></el-input>
            </li>
        </ul>
        <ul>
            <li>
                <el-input v-model="password" type="password" placeholder="Enter your password..."></el-input>
            </li>
        </ul>
        <ul>
            <li>
                <el-button @click=loginClick>登录</el-button>
            </li>

        </ul>
        <ul>
            <li>
                <el-button @click=registerClick>注册此帐号</el-button>
            </li>
        </ul>

    </div>
</template>



<script>
    export default {
        name: "Login",
        data(){
            return{
                username: "",
                password: "",

            }
        }
    }
</script>

<style scoped>

</style>