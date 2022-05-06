<template>
  <div class="py-5 mx-auto w-full">
    <h1 class="text-2xl text-center">Welcom to
       <span class="text-dark underline decoration-green">e-Kids<i class="text-green font-bold"> SHOP</i></span>, online shop with delivery
    </h1>
  </div>

  <div class="py-5 mx-auto w-full">
    <dark-title>Latest products</dark-title>
    <div class="flex flex-wrap justify-between items-center space-x-2 my-2">
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>  
  </div>


  <div class="py-5 mx-auto w-full">
    <h2 class="text-2xl text-center text-dark font-bold">Promotion</h2>
  </div>  

  <div class="py-5 mx-auto w-full">
    <h2 class="text-2xl text-center text-dark font-bold">Top Seller</h2>
  </div> 

  <div class="py-5 mx-auto w-full">
    <h2 class="text-2xl text-center text-dark font-bold">Sale</h2>
  </div>      
</template>

<script>
// @ is an alias to /src
import Logo from '@/components/UI/Logo'
import DarkTitle from '@/components/UI/DarkTitle'
import ProductBox from '@/components/ProductBox.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: { 
    Logo,
    DarkTitle,
    ProductBox,    
  },
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | e-Kids Shop'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>


