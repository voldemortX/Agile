<template>
  <div id="app" class="bg-global">

    <router-view/>
  </div>
</template>

<style>
  #app {
    font-family: "PingFang SC", "Microsoft YaHei", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  .bg-global {
      background-size: 100% 100%;
      width: 100%;
      height: 100%;
      position: fixed;
      background-color: #ffffff;
  }
  body{
    margin:0;
    padding:0;
  }
</style>
