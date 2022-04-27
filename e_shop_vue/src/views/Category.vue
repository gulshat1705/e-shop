<template>
    <div class="">
        <green-title>{{ category.name }}</green-title>
         <div class="flex items-center space-x-2 my-2">
             <ProductBox
                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product"
             />

         </div>
    </div>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import ProductBox from '@/components/ProductBox'

import { toast } from 'bulma-toast'
import axios from 'axios'

export default {
    name: 'category',
    components: {
        GreenTitle,  
        ProductBox      
    },
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {            // switch by category
        $route(to, from) {
            if (to.name === 'category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | e-Kids Shop'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'

                    })                
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
