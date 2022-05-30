<template>
    <div class="w-3/4 text-center mx-auto my-5">
        <green-title>log in</green-title>
        <form @submit.prevent="submitForm">
            <div class="text-center w-1/2 mx-auto">
                <div class="my-5">
                    <input type="text" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="username" placeholder="Username">
                </div>

                <div class="my-5">
                    <input type="password" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="password" placeholder="Password">
                </div>
            </div>    

            <div class="" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div> 
            <div class="my-2">
                <green-btn>log in</green-btn>
                <p class="m-0">
                    <router-link to="/forgot-passw" class="text-green text-sm">Forgot password?</router-link>
                </p>
            </div> 

            <hr>
            <p class="py-5">Or 
                <router-link to="/sign-up" class="text-green">click here</router-link>
                to sign up!
            </p>       
        </form>
    </div>
    
</template>

<script>
import GreenBtn from '@/components/UI/GreenBtn'
import GreenTitle from '@/components/UI/GreenTitle'
import axios from 'axios'

export default {
    name: 'log-in',
    components: {
        GreenBtn,
        GreenTitle,
    },
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log in | e-kids Shop'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('access')

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/jwt/create/', formData)
                .then(response => {
                    const access = response.data.access
                    const refresh = response.data.refresh

                    this.$store.commit('setAccess', access)
                    this.$store.commit('setRefresh', refresh)

                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + access

                    localStorage.setItem('access', access)
                    localStorage.setItem('refresh', refresh) 

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again!')

                        console.log(JSON.stringify(error))
                    }
                })
        }
    }


}
</script>
