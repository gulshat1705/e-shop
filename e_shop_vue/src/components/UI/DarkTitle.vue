<template>
  <h2 class="dark-title">
      <slot></slot>
  </h2>
</template>

<script>
export default {
    name: 'dark-title'
}
</script>
<style scoped>
.dark-title{
  text-align: center;
  text-transform: capitalize;
  font-family: 'Helvetica', sans-serif;
  color: #35495e;
  padding: 7px;
  font-size: 26px;
} 
</style>