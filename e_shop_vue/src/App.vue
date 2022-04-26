<template>
  <Navbar />

  <section class="container header-wrap max-w-7xl mx-auto py-8">

    <div class="search items-center relative mx-auto">
      <form method="get" action="/search">
        <div class="control ">
          <input type="text" class="border rounded-3xl border-dark py-3 pl-7 pr-16 text-dark" placeholder="What are you looking for" name="query">
        </div>

        <div class="control absolute flex items-center right-5 top-2">
          <button class="button is-success">
            <span class="icon">
            <i class="fas fa-search text-3xl text-green"></i>
            </span>
          </button>

        </div>

      </form>
    </div>
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

<style scoped>
.search{
  width: 80%;
  text-align: center;
}
.search input{
  width: 100%;
}
</style>


