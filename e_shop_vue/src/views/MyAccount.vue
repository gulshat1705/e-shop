<template>
    <div>
        <dark-title>my account</dark-title>
        <dark-btn @click="logout()">log out</dark-btn>
    </div>
    <hr>
    <div>
        <green-title>my orders</green-title>

        <OrderSummary
            v-for="order in orders"
            v-bind:key="order.id"
            v-bind:order="order"
        />
        
    </div>

    
</template>

<script>
import axios from 'axios'
import DarkBtn from '@/components/UI/DarkBtn.vue'
import GreenTitle from '@/components/UI/GreenTitle.vue'
import DarkTitle from '@/components/UI/DarkTitle'
import OrderSummary from '@/components/OrderSummary'


export default {
    name: 'my-account',
    components: {
      DarkBtn,
      GreenTitle,
      DarkTitle,
      OrderSummary
    },    
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | e-Shop Kids'

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)    
        }
    }
}
</script>
