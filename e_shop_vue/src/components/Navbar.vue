<template>
    <header class="bg-dark">        
        <!--desktop menu-->
        <nav  class="header-wrap max-w-7xl mx-auto flex justify-between sm:px-5">
            <div class="navbar-logo flex items-center space-x-2 py-3 px-2">
                <Logo />
            </div>
            <div class="block lg:hidden flex items-center absolute right-10 top-5">                
                <button @click="toggle" class="flex items-center px-3 py-2">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-10" fill="none" viewBox="0 0 24 24" stroke="white" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>
            </div>
                                    <!--menu -->
            <div :class="open ? 'block': 'hidden'" class="menu items-center space-x-1 flex-grow lg:flex" >
                <div class="md:flex-grow">    
                    <router-link to="/" class="py-5 px-5 text-white hover:text-green lg:block">Home</router-link>
                    <router-link to="/all-products" class="py-5 px-5 text-white hover:text-green ">All Products</router-link>
                    <router-link to="/clothes" class="py-5 px-3 text-white hover:text-green">Clothes</router-link>                        
                    <router-link to="/nutrition" class="py-5 px-3 text-white hover:text-green">Nutrition</router-link>                        
                    <router-link to="/diapers" class="py-5 px-3 text-white hover:text-green">Diapers</router-link>                        
                    <router-link to="/toys" class="py-5 px-3 text-white hover:text-green">Toys</router-link>
                </div> 
                            
                <div class="left-items flex space-x-4">
                    
                    <div class="py-5 px-10">
                        <i class="fa-solid fa-phone text-2xl text-white"><span class="text-green text-lg pl-3">0771 67 67 51</span></i>
                    </div>
                    <template v-if="$store.state.isAuthenticated">
                        <router-link to="/my-account">
                            <i class="fa-solid fa-user-check py-5 text-2xl text-white hover:text-green"></i>
                        </router-link>                        
                    </template>

                    <template v-else>
                         <router-link to="/log-in">
                            <i class="fa-solid fa-user-large py-5 text-2xl text-white hover:text-green"></i>
                        </router-link>
                    </template>         
                                       
                    <router-link to="/cart">
                        <i class="fa-solid fa-cart-shopping relative py-5 text-2xl text-white hover:text-green">
                            <span class="absolute top-3 text-sm text-green hover:text-white">{{ cartTotalLength }}</span>
                        </i>                        
                    </router-link>
                        
                    <select class="text-white">
                        <option>Рус</option>
                        <option>Eng</option>
                    </select>                         
                </div>                   
            </div>
                    <!-- mobile menu-->     
        </nav>

    </header>
</template>

<script>
import axios from 'axios'

import GreenBtn from './UI/GreenBtn.vue'
import LightBtn from './UI/LightBtn.vue'
import Logo from './UI/Logo.vue'

export default {
  components: { GreenBtn, LightBtn, Logo },
    data() {
        return {
            open: false,
            cart: {
                items: []
            }
        }
    },
    beforeCreated() {
        this.$store.commit('initializeStore')

        const token = this.$store.state.token

        if (token) {
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }
    },    
    methods: {
        toggle() {
        this.open = !this.open;
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0

            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }
            return totalLength
        }
    }
}
</script>

<style scoped>
.header-wrap{
    position: relative;
}
.left-items{
    position: absolute;
    right: 0;
}
</style>
