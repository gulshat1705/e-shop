<template>
    <div>
        <dark-title>my account</dark-title>
        <div class="text-right">
            <dark-btn @click="logout()">log out</dark-btn>
        </div>
        <div>
            <green-title class="font-bold">Personal details</green-title>
            <p class="text-red" >If you want update your personal information click the follow info!</p>
            <form @submit.prevent="handleSubmit(updateProfile)">                
                <div class="flex items-center justify-center flex-wrap w-full"> 
                    <div class="field flex">
                        <label class="text-dark font-bold">username: </label>
                        <input type="text" class="" v-model="userForm.username">
                    </div>    
                    <div class="field flex">
                        <label class="text-dark font-bold">email: </label>
                        <input type="email" class="" v-model="userForm.email">
                    </div>                                    
                    <div class="field flex">
                        <label class="text-dark font-bold">Name: </label>
                        <input type="text" class="" v-model="userForm.name">
                    </div>
                    <div class="field flex">
                        <label class="text-dark font-bold">Phone: </label>
                        <input type="text" class="" v-model="userForm.phone">
                    </div>
                    <div class="field flex address">
                        <label class="text-dark font-bold">Address: </label>
                        <input type="text" class="" v-model="userForm.address">
                    </div>                    
                </div>
                
                <button  type="submit" class="block uppercase text-white bg-green py-2 px-5 w-80 mx-auto my-2 rounded">save changes</button>
                <router-link to="/change-password" class="block pb-2 text-dark underline decoration-solid decoration-green font-bold text-center">Change password</router-link>
            </form>
            
        </div>
        
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
import GreenBtn from '@/components/UI/GreenBtn.vue'


export default {
    name: 'my-account',
    components: {
      DarkBtn,
      GreenBtn,
      GreenTitle,
      DarkTitle,
      OrderSummary

    },    
    data() {
        return {
            orders: [],
            userForm: {
                username: '',
                email: '',
                name: '',
                phone: '',
                address: ''
            }
            
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
        getUser() {
            axios
                .get('/api/v1/update_profile/')
                .then(response => {
                    this.userForm = response.data
                })
        },
        async created() {
            const response = await axios.get('user', {
            headers: {
                Authorization: 'Bearer ' + localStorage.getItem('access')
            }
            })
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
        },


    }
}
</script>

<style scoped>
.field{
    width: 50%; 
    padding: 5px 10px ;
}

.field label{
    width: 100px;
}
.field input{
    width: 100%;
    padding: 3px 10px;
    outline: none;
    background: rgb(203 213 225);
    border: 1px solid rgb(203 213 225);
    border-radius: 3px;
    margin-bottom: 5px;
    transition: .3s;
}
.address{
    width: 100%;
    padding-left: 0;
}
.field input:focus{
    border: 1px solid #35495e;

}
</style>
