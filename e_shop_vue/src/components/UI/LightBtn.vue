<template>
  <router-link class="light-btn">
      <slot></slot>
  </router-link>
</template>

<script>
export default {
    name: 'light-btn'
}
</script>
<style scoped>
.light-btn{
  display: block;
  text-transform: capitalize;
  font-family: 'Helvetica', sans-serif;
  color: #35495e;
  background: #fff;
  padding: 7px 25px;
  text-align: center;
  border: 1px solid #42b883;
  border-radius: 5px;
} 
.light-btn:hover,
.light-btn:active{
    background: #42b883;
    border-color: #fff;    
}

</style>