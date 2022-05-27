<template>
    <header class="bg-dark">        
        <!--desktop menu-->
        <nav  class="header-wrap max-w-7xl mx-auto flex justify-between lg:block">
            <div class="navbar-logo flex items-center space-x-2 py-3 px-2 xl:pl-5 sm:pl-5">
                <Logo />
            </div>
            <div class="hidden lg:block flex items-center absolute right-10 top-5">                
                <button @click="toggle" class="flex items-center px-3 py-2">
                   <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-10" fill="none" viewBox="0 0 24 24" stroke="white" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
                    </svg>
                </button>
            </div>
                                    <!--menu -->
            <div :class="open ? 'hidden': 'block'" class="items-center space-x-1 flex-grow lg:w-full lg:text-center lg:bg-dark500">
                <div class="pt-8 w-1/2 lg:w-full">    
                    <router-link to="/" class="py-5 px-5 text-white hover:text-green lg:block lg:py-1">Home</router-link>
                    <router-link to="/all-products" class="py-5 px-5 text-white hover:text-green lg:block lg:py-1">All Products</router-link>
                    <router-link to="/clothes" class="py-5 px-3 text-white hover:text-green lg:block lg:py-1">Clothes</router-link>                        
                    <router-link to="/nutrition" class="py-5 px-3 text-white hover:text-green lg:block lg:py-1">Nutrition</router-link>                        
                    <router-link to="/diapers" class="py-5 px-3 text-white hover:text-green lg:block lg:py-1">Diapers</router-link>                        
                    <router-link to="/toys" class="py-5 px-3 text-white hover:text-green lg:block lg:py-1">Toys</router-link>
                </div> 
                            
                <div class="absolute right-0 top-2 flex space-x-4 lg:block lg:static lg:w-full">
                    
                    <div class="py-5 px-10 lg:py-0">
                        <i class="fa-solid fa-phone text-2xl text-white"><span class="text-green text-lg pl-3 lg:text-white lg:text-base">0771 67 67 51</span></i>
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

        const access = this.$store.state.access

        if (access) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }
    },  
    mounted() {
        this.cart = this.$store.state.cart
    //    setInterval(() => {
    //        this.getAccess()
    //    }, 5000)
    },    
    methods: {
        toggle() {
            this.open = !this.open;
        },
    //    getAccess(e) {
    //        const accessData = {
    //            refresh: this.$store.state.refresh
    //        }
    //        axios
    //            .post('/api/v1/jwt/refresh/', accessData)
    //            .then(response => {
    //                const access = response.data.access

    //                console.log(access)

    //                localStorage.setItem('access', access)
    //                this.$store.commit('setAccess', access)
    //            })
    //            .catch(error => {
    //                console.log(error)
    //            })
    //    }
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
