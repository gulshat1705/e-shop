<template>
    <header>
        <div class="container">
            <nav class="navbar">
                <div class="navbar-logo">
                    <router-link to="/" class="logo">
                        e-Kids <span>shop</span>
                    </router-link>       <!--LOGO-->

                    <a class="burger-menu" @click="showBurgerMenu = !showBurgerMenu">
                        <span class="burger-menu__item burger-menu__item--first"></span>
                        <span class="burger-menu__item burger-menu__item--second"></span>
                        <span class="burger-menu__item burger-menu__item--third"></span>
                    </a>                 <!-- burger menu -->
                </div> 
<!--baby clothes, child nutrition, diapers, toys, -->
                <div class="navbar-menu" v-bind:class="{'is-active': showBurgerMenu}">
                    <ul class="menu">
                        <router-link to="/">home</router-link>
                        <router-link to="/clothes" class="link">baby clothes</router-link>                        
                        <router-link to="/nutrition">child nutrition</router-link>                        
                        <router-link to="/diapers">diapers</router-link>                        
                        <router-link to="/toys">toys</router-link>                        
                    </ul>
                </div>

                <div class="navbar-items">
                    <div>
                        <light-btn to="/account">account</light-btn>
                    </div>
                    
                    <div>
                        <light-btn to="/olog-in">log in</light-btn>
                    </div>                   
                </div>
                <div class="navbar-items">
                    <light-btn class="green" to="cart">
                        <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                        <span>Cart</span>
                    </light-btn>
                </div>
                <div class="lang-items">
                    <select class="language">
                        <option>Рус</option>
                        <option>Eng</option>
                    </select>
                </div>


            </nav>

        </div>        
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
            showBurgerMenu: false,

        }
    }
}
</script>

<style scoped>
.green{
    background: #42b883;
    color: #fff;
}
.icon{
    margin-left: -5px;
    margin-right: 10px;
}
.lang-items{
    margin: 15px 0 0 20px;
}
.language{
    margin-top: 10px;
    color: #fff;
    font-size: 18px; 
    position: absolute;
    right: 0;    
}
.fas.fa-shopping-cart{
    color: #fff;
}
</style>
