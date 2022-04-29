<template>
  <button class="dark-btn">
      <slot></slot>
  </button>
</template>

<script>
export default {
    name: 'dark-btn'
}
</script>
<style scoped>
.dark-btn{
  font-family: 'Helvetica', sans-serif;
  text-transform: uppercase;
  color: #fff;
  background: #35495e;
  padding: 10px 30px;
  text-align: center;
  border: #fff;
}  
</style>