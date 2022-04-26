<template>
    <router-link to="/" class="logo text-white">
        e-Kids <span>shop</span>
    </router-link> 
</template>

<script>
export default {
    name: 'Logo'
}
</script>

<style scoped>
.logo{    
    font-weight: 300;
    font-size: 36px;
    line-height: 2.0rem;
    font-family: 'Lato', sans-serif;
    text-decoration: none;
}
.logo span{
    font-size: 32px;
    font-weight: 900;
    font-family: 'Bebas Neue', cursive;
    letter-spacing: 4px;
    padding-left: 15px;
    color: #42b883;
}
</style>