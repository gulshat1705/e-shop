<template>
    <header>
        <div class="container">
            <nav class="navbar">
                <div class="navbar-logo">
                    <router-link to="/" class="logo">
                        e-Kids <span>shop</span>
                    </router-link>  <!--LOGO-->

                    <a class="burger-menu" @click="showBurgerMenu = !showBurgerMenu">
                        <span class="burger-menu__item burger-menu__item--first"></span>
                        <span class="burger-menu__item burger-menu__item--second"></span>
                        <span class="burger-menu__item burger-menu__item--third"></span>
                    </a>    <!-- burger menu -->
                </div> 
<!--baby clothes, child nutrition, diapers, toys, -->
                <div class="navbar-menu" v-bind:class="{'is-active': showBurgerMenu}">
                    <ul class="menu">
                        <router-link to="/">home</router-link>
                        <router-link to="/clothes">baby clothes</router-link>                        
                        <router-link to="/nutrition">child nutrition</router-link>                        
                        <router-link to="/diapers">diapers</router-link>                        
                        <router-link to="/toys">toys</router-link>                        
                        <router-link to="/about">About</router-link>
                    </ul>

                </div>


            </nav>

        </div>        
    </header>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            showBurgerMenu: false,
        }
    }
}
</script>

