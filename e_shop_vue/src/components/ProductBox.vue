<template>
    <div class="relative text-center border border-solid border-lightGray w-72 h-96 pt-3 pb-5 py-5">
        <figure class="pl-9 pb-2">
            <img v-bind:src="product.get_thumbnail">
        </figure>
    
        <h3>{{ product.name }}</h3>
        <p class="text-gray" v-if="product.sale!=0" v-bind:class="{ 'line-through': isActive }">{{ product.price }} som</p>
        <p class="text-gray" v-else>{{ product.price }} som</p>
        <p v-if="product.sale!=0" class="text-red">sale: -{{ product.sale }} %</p>
        <p v-if="product.get_sale_price !=null" class="text-gray">discounted price:<i class="text-green">{{ product.get_sale_price }} </i></p>
        <p class="text-gray text-sm">{{ product.view_count }} <i class="fa-solid fa-eye text-dark"></i></p>       

        <router-link v-bind:to="product.get_absolute_url"><green-btn class="w-full absolute left-0 bottom-0">View details</green-btn></router-link>
    </div>     
</template>

<script>
import GreenBtn from '@/components/UI/GreenBtn.vue'

export default {
    name: 'ProductBox',
    components: { GreenBtn },
    props: {
        product: Object
    },
    data() {
        return {
            isActive: true
        }
    }
   
}


</script>
