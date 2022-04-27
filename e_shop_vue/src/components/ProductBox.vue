<template>
    <div class="text-center border border-solid border-lightGray w-64 h-80 pt-3 pb-5 py-5">
        <figure class="pl-10 pb-5">
            <img v-bind:src="product.get_thumbnail">
        </figure>

        <h3>{{ product.name }}</h3>
        <p class="text-gray">{{ product.price }} som</p>

        <router-link v-bind:to="product.get_absolute_url"><green-btn class="w-full">View details</green-btn></router-link>
    </div>     
</template>

<script>
import GreenBtn from '@/components/UI/GreenBtn.vue'

export default {
    name: 'ProductBox',
    components: { GreenBtn },
    props: {
        product: Object
    }

}
</script>

<style>

</style>