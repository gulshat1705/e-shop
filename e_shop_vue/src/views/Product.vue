<template>
    <div class="flex py-8">
        <div class="w-2/4">
            <figure class="px-10 py-10">
                <img v-bind:src="product.get_image">
            </figure>
        </div>

        <div class="pl-10 w-2/4 text-justify">
            <green-title>{{ product.name }}</green-title>
            <p>Price: {{ product.price }} som</p>
            <p class="text-gray py-5">{{ product.description }}</p>

            <div class="mx-auto">
                <input type="number" class="w-20 border rounded border-solid border-green py-1 px-3 my-3" min="1" v-model="quantity">
            </div>
            <div class="">
                <green-btn @click="addToCart" class="w-full">Add to Cart</green-btn>
            </div>

        </div>
    </div>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import GreenBtn from '@/components/UI/GreenBtn'
import axios from 'axios'


export default {
    name: 'product',
    components: {
        GreenTitle,
        GreenBtn,
    },
    data() {
        return {
            product: {},
            quantity: 1
            
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | e-Kids Shop'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            console.log('addToCart')
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)
        }

    }

}
</script>
