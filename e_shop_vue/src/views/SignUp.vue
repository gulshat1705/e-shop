<template>
    <div class="w-3/4 text-center mx-auto my-5">
        <dark-title>sign up</dark-title>
        <form @submit.prevent="submitForm">
            <div class="text-center w-1/2 mx-auto">
                <div class="my-5">
                    <input type="text" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="email" placeholder="Email">
                </div>
                <div class="my-5">
                    <input type="text" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="username" placeholder="Username">
                </div>                
                <div class="my-5">
                    <input type="password" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="password" placeholder="Password">
                </div>

                <div class="my-5">
                    <input type="password" class="w-full border-b border-solid border-dark py-1 px-3 ml-5" v-model="password2" placeholder="Repeat Password">
                </div>
            </div>    

            <div class="" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div> 

            <div class="my-5">
                <dark-btn>sign up</dark-btn>
            </div> 
            <hr>
            <p class="py-5">Or 
                <router-link to="/log-in" class="text-green">click here</router-link>
                to log in!
            </p>       
        </form>
    </div>
    
</template>

<script>
import DarkTitle from '@/components/UI/DarkTitle'
import DarkBtn from '@/components/UI/DarkBtn'
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'sign-up',
    components: {
        DarkTitle,
        DarkBtn,
    },
    data() {
        return {
            email: '',
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Sign up | e-Kids-shop'
    },
    methods: {
        submitForm() {
            this.errors = []
            if (this.email === '') {
                this.errors.push('The email is missing')
            }

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The password doesn\'t match')
            }

            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    username: this.username,
                    password: this.password,
                    re_password: this.password2
                }

                axios
                    .post('api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in by email!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-center'
                        })

                        this.$router.push('/log-in')        // After registration, it goes straight to the log-in page
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })           
            }

        }
    }
 
}

</script>
