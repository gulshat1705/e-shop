<template>
    <div>
        <dark-title>cart</dark-title>
        <div>
            <table class="w-full" v-if="cartTotalLength">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>
                    <CartItem 
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        v-bind:initialItem="item"    
                        v-on:removeFromCart="removeFromCart"       
                    />
                </tbody>
            </table>
            <p v-else>You don't have any products in your cart ...</p>
        </div>

        <div class="">
            <green-title>Summary</green-title>
            <strong>{{cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
            <hr>
            <router-link to="/cart/checkout"><dark-btn>Procceed to checkout</dark-btn></router-link>
        </div>
    </div>
</template>

<script>
import DarkTitle from '@/components/UI/DarkTitle'
import GreenTitle from '@/components/UI/GreenTitle'
import DarkBtn from '@/components/UI/DarkBtn'
import CartItem from '@/components/CartItem'
import axios from 'axios'

export default {
    name: 'cart',
    components: {
        DarkTitle,
        GreenTitle,
        DarkBtn,
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
