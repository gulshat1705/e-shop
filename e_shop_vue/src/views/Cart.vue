<template>
    <div>
        <dark-title>cart</dark-title>
        <div>
            <table class="w-full" v-if="cartTotalLength">
                <thead>
                    <tr class="font-bold border border-solid border-lightGray">
                        <th  class="w-1/4 py-3">Product</th>
                        <th  class="w-1/4 py-3">Price</th>
                        <th  class="w-1/4 py-3">Quantity</th>
                        <th  class="w-1/4 py-3">Total</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody class="text-center py-3">
                    <CartItem class=" "
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        v-bind:initialItem="item"    
                        v-on:removeFromCart="removeFromCart"       
                    />
                </tbody>
            </table>
            <p v-else class="text-dark">You don't have any products in your cart ...</p>
        </div>

        <div class="w-full">
            <green-title class="font-bold">Summary</green-title>
            <div class="w-full text-center py-3 bg-green">
                <strong  class="py-5 text-dark">{{cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
            </div>
            <hr>
            <router-link class="block text-center" to="/cart/checkout"><green-btn class="my-3 text-center">Procceed to checkout</green-btn></router-link>
        </div>
    </div>
</template>

<script>
import DarkTitle from '@/components/UI/DarkTitle'
import GreenTitle from '@/components/UI/GreenTitle'
import DarkBtn from '@/components/UI/DarkBtn'
import GreenBtn from '@/components/UI/GreenBtn'
import CartItem from '@/components/CartItem'
import axios from 'axios'

export default {
    name: 'cart',
    components: {
        DarkTitle,
        GreenTitle,
        DarkBtn,
        GreenBtn,
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        }
    }


}
</script>