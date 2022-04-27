<template>
  <div class="py-5">
    <dark-title>All Products</dark-title>
    <div class="flex items-center space-x-2 my-2">
      <ProductBox
        v-for="product in allProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import DarkTitle from '@/components/UI/DarkTitle.vue'
import ProductBox from '@/components/ProductBox.vue'
import axios from 'axios'

export default {
  name: 'all-products',
  components: { 
    DarkTitle,
    ProductBox,
  },
  data() {
    return {
      allProducts: []
    }
  },
  mounted() {
    this.getAllProducts()
    document.title = 'All Products | e_Kids Shop'
  },
  methods: {
    async getAllProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/all-products/')
        .then(response => {
          this.allProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
        
      this.$store.commit('setIsLoading', false)
    }
  }

}
</script>

<style>

</style>