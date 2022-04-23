<template>
  <button class="green-btn">
      <slot></slot>
  </button>
</template>

<script>
export default {
    name: 'green-btn'
}
</script>
<style scoped>
.green-btn{
  font-family: 'Helvetica', sans-serif;
  color: #35495e;
  background: #42b883;
  padding: 7px;
  font-size: 18px;
  text-align: center;
  border: #fff;
  border-radius: 5px;
}  
</style>