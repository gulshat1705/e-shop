<template>
  <Navbar />

  <section class="container">
    <router-view/>
  </section>  

  <Footer />
  
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer' 

export default {
  components: {
    Navbar,
    Footer,
  }
}
</script>


