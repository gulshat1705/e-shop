<template>
    <div class="">
        <div class="">
            <figure class="">
                <img v-bind:src="product.get_thumbnail">
            </figure>

            <h3>{{ product.name }}</h3>
            <p>{{ product.price }} som</p>

            <router-link v-bind:to="product.get_absolute_url" class="">View details</router-link>
        </div>
    </div>
  
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }

}
</script>

<style>

</style>