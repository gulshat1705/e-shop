<template>
    <div class="py-5">
        <green-title>Search results...</green-title>
        <h3 class="text-center text-lg">Search term: "{{query }}"</h3>
    </div>

    <div class="flex items-center space-x-2 my-2">
        <ProductBox 
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"
        />
    </div>    
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import ProductBox from '@/components/ProductBox'
import axios from 'axios'

export default {
    name: 'search',
    components: {
        GreenTitle,
        ProductBox,
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | e-Kids Shop'

        let url = window.location.search.substring(1)
        let params = new URLSearchParams(url)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/products/search/', {'query': this.query})
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
