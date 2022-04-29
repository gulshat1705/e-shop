<template>
    <div>
        <green-title>my account</green-title>
        <dark-btn @click="logout()">log out</dark-btn>
    </div>
    
</template>

<script>
import axios from 'axios'
import DarkBtn from '../components/UI/DarkBtn.vue'
import GreenTitle from '../components/UI/GreenTitle.vue'

export default {
  components: { DarkBtn, GreenTitle },
    name: 'my-account',
    methods: {
        logout() {
            axios.defaults.headers.common[Authorization] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}
</script>
