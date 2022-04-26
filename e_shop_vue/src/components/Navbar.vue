<template>
    <header class="bg-dark">        
        <!--desktop menu-->
        <nav>
            <div class="max-w-7xl mx-auto">
                <div class="flex justify-between">
                    <!--menu-->
                    <div class="flex space-x-4">
                        <!--logo-->
                        <div class="navbar-logo flex items-center space-x-2 py-3 px-2">
                            <router-link to="/" class="logo text-white">
                                e-Kids <span>shop</span>
                            </router-link>     
                        </div>
                        <!--menu -->
                        <div class="menu items-center space-x-1" v-bind:class="{'hidden': !showMenu, 'flex': showMenu}">
                            <div class="flex flex-col lg:flex-row list-none ml-auto">    
                                <router-link to="/" class="py-5 px-5 text-white hover:text-green">home</router-link>
                                <router-link to="/clothes" class="py-3 px-3 text-white hover:text-green">baby clothes</router-link>                        
                                <router-link to="/nutrition" class="py-5 px-3 text-white hover:text-green">child nutrition</router-link>                        
                                <router-link to="/diapers" class="py-5 px-3 text-white hover:text-green">diapers</router-link>                        
                                <router-link to="/toys" class="py-5 px-3 text-white hover:text-green">toys</router-link>
                            </div>        
                        </div>
                    </div>
                    <!--login-->
                    <div class="hidden md:flex items-center space-x-1">
                        <light-btn to="/log-in">log in</light-btn>
                      <!--  <light-btn to="/account">account</light-btn>-->
                    </div>                    
                    <div class="hidden md:flex items-center space-x-1">
                        <light-btn to="/register">register</light-btn>
                    </div>
                    <div class="hidden md:flex items-center space-x-1">
                        <light-btn class="green" to="cart">
                            <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                            <span>Cart</span>
                        </light-btn>
                    </div> 
                    <div class="hidden md:flex items-center space-x-1">
                        <select class="text-white">
                            <option>Рус</option>
                            <option>Eng</option>
                        </select>
                    </div> 
                    <!--btn show mobile menu-->
                    <div class="flex md:hidden items-center" v-on:click="toggleNavbar()">
                        <button class="py-5 px-7">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-15" fill="none" viewBox="0 0 24 24" stroke="white" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h8m-8 6h16" />
                            </svg>
                        </button>
                        
                    </div>
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

export default {
  components: { GreenBtn, LightBtn },
    data() {
        return {
            showMenu: false,

        }
    },
    methods: {
        toggleNavbar: function(){
        this.showMenu = !this.showMenu;
        }
  }
}
</script>

<style scoped>
/*BURGER menu*/
.burger{
    cursor: pointer;
    display: none;
    position: absolute;
    right: 0;
}
.burger-menu, .burger-menu__item{
    display: block;
}
.burger-menu{
  border: 1px solid #42b883;
  border-radius: 3px;
  background: #fff;
  height: 45px;
  width: 62px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 10px;
}
.burger-menu__item{
    height: 3px;
    width: 100%;
    background: #42b883;
    transition: transform 300ms cubic-bezier(0.445, 0.05, 0.55, 0.95),
    opacity 300ms linear;
}
.burger--is-open .burger__item.burger__item--first{
        transform: translate(0, 20px) rotate(40deg);
}    
.burger--is-open .burger__item--second{
        opacity: 0;
}    
.burger--is-open .burger__item.burger__item--third{
        transform: translate(0, -20px) rotate(-40deg);
}

@media (max-width: 991px) {
    .burger{
        display: block;
    }    
}
/*end BURGER menu*/
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
