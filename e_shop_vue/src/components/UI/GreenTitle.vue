<template>
  <h3 class="green-title">
      <slot></slot>
  </h3>
</template>

<script>
export default {
    name: 'green-title'
}
</script>
<style scoped>
.green-title{
  text-align: center;
  text-transform: capitalize;
  font-family: 'Helvetica', sans-serif;
  color: #42b883;
  padding: 7px;
  font-size: 24px;
} 
</style>