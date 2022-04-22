<template>
  <navbar></navbar>
  <div class="app">
    <router-view/>
  </div>  
</template>

<script>
import navbar from '@/components/Navbar'

export default {
  components: {
    Navbar
  }
}
</script>


