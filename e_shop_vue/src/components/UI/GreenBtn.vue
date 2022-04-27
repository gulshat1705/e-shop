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
  text-transform: capitalize;
  color: #fff;
  background: #42b883;
  padding: 9px 7px;
  text-align: center;
  border: #fff;
}  
</style>