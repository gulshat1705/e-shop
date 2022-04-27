<template>
    <header class="bg-dark">        
        <!--desktop menu-->
        <nav  class="header-wrap max-w-7xl mx-auto flex justify-between sm:px-5">
            <div class="navbar-logo flex items-center space-x-2 py-3 px-2">
                <Logo />
            </div>
            <div class="block lg:hidden flex items-center">                
                <button @click="toggle" class="flex items-center px-3 py-2">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-10" fill="none" viewBox="0 0 24 24" stroke="white" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>
            </div>
                                    <!--menu -->
            <div :class="open ? 'block': 'hidden'" class="menu items-center space-x-1 w-full flex-grow lg:flex" >
                <div class="md:flex-grow">    
                    <router-link to="/" class="py-5 px-5 text-white hover:text-green">Home</router-link>
                    <router-link to="/all-products" class="py-5 px-5 text-white hover:text-green">All Products</router-link>
                    <router-link to="/clothes" class="py-5 px-3 text-white hover:text-green">Clothes</router-link>                        
                    <router-link to="/nutrition" class="py-5 px-3 text-white hover:text-green">Nutrition</router-link>                        
                    <router-link to="/diapers" class="py-5 px-3 text-white hover:text-green">Diapers</router-link>                        
                    <router-link to="/toys" class="py-5 px-3 text-white hover:text-green">Toys</router-link>
                </div> 
                            
                <div class="left-items flex space-x-4">
                    <light-btn to="/log-in">log in</light-btn>
                <!--  <light-btn to="/account">account</light-btn>-->
                                        
                    <light-btn to="/register">register</light-btn>
                                        
                    <light-btn class="green" to="cart">
                        <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                        <span>Cart</span>
                    </light-btn>
                        
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

        }
    },
    methods: {
        toggle() {
        this.open = !this.open;
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
.green{
    background: #42b883;
    color: #fff;
}
.icon{
    margin-left: -5px;
    margin-right: 10px;
}
.fas.fa-shopping-cart{
    color: #fff;
}
</style>
