<template>
  <div id="app">
    <navBar/>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
  import navBar from './components/navBar'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {
      components: {navBar}
  }

</script>