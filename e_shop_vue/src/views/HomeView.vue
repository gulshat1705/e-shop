<template>
  <div class="py-5 mx-auto w-full">
    <h1 class="text-2xl text-center">Welcom to
       <span class="text-dark underline decoration-green">e-Kids<i class="text-green font-bold"> SHOP</i></span>, online shop with delivery
    </h1>
  </div>

  <div class="py-5 mx-auto w-full">
    <dark-title>Latest products</dark-title>   

    <swiper class="mySwiper flex flex-wrap justify-between items-center my-2 pb-10"
      :slidesPerView="4"  
      :spaceBetween="30"    
      :slidesPerGroup="4"
      :autoplay="{
        delay: 2500,
        disableOnInteraction: false
      }"
      :loop="true"
      :loopFillGroupWithBlank="true"
      :pagination="{
        clickable:true,
        }"
      :navigation="true"
      :modules="modules"   
    > 
      <swiper-slide v-for="product in latestProducts">          
          <ProductBox 
            v-bind:key="product.id"
            v-bind:product="product"
          />         
      </swiper-slide>  
    </swiper>  
  </div>

  <div class="py-5 mx-auto w-full">
    <dark-title>Popular products</dark-title>
    
      <swiper class="mySwiper flex flex-wrap justify-between items-center space-x-2 my-2 pb-10"
        :slidesPerView="4"  
        :spaceBetween="30"    
        :slidesPerGroup="4"
        :autoplay="{
          delay: 2500,
          disableOnInteraction: false
        }"
        :loop="true"
        :loopFillGroupWithBlank="true"
        :pagination="{
          clickable:true,
          }"
        :navigation="true"
        :modules="modules"   
      > 
        <swiper-slide v-for="product in popularProducts">          
            <ProductBox 
              v-bind:key="product.id"
              v-bind:product="product"
            />         
        </swiper-slide>  
      </swiper>  

    
  </div>  

  <div class="py-5 mx-auto w-full">
    <dark-title>Promotions, Sale</dark-title>
    <div class="flex flex-wrap justify-between items-center space-x-2 my-2">
      
      <swiper class="mySwiper flex flex-wrap justify-between items-center my-2 pb-10"
        :slidesPerView="4"  
        :spaceBetween="30"    
        :slidesPerGroup="4"
        :loop="true"
        :loopFillGroupWithBlank="true"
        :pagination="{
          clickable:true,
          }"
        :navigation="true"
        :modules="modules"   
      > 
        <swiper-slide v-for="product in salesProducts">          
            <ProductBox 
              v-bind:key="product.id"
              v-bind:product="product"
            />         
        </swiper-slide>  
      </swiper>  

    </div>
  </div>  
</template>

<script>
// @ is an alias to /src
import Logo from '@/components/UI/Logo'
import DarkTitle from '@/components/UI/DarkTitle'
import ProductBox from '@/components/ProductBox.vue'
import axios from 'axios'

import Carousel from '@/components/Carousel.vue'
import Slide from '@/components/Slide.vue'

import { Swiper, SwiperSlide } from "swiper/vue";

import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";



// import required modules
import {Autoplay, Pagination, Navigation } from "swiper";

export default {
  name: 'home',
  components: {     
    Logo,
    DarkTitle,
    ProductBox, 
    Carousel,
    Slide,
    
    Swiper,
    SwiperSlide,

  },
  data() {
    return {
      latestProducts: [],
      popularProducts: [],
      salesProducts: [],            
    }
  },
  mounted() {
    this.getLatestProducts(),
    this.getPopularProducts(),
    this.getSalesProducts(),

    document.title = 'Home | e-Kids Shop'
  },
  setup() {
    return {
      modules: [Autoplay, Pagination, Navigation],
    };
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    },

    async getPopularProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/popular-products/')
        .then(response => {
          this.popularProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)  
    },

    async getSalesProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/sale-products/')
        .then(response => {
          this.salesProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
      
      this.$store.commit('setIsLoading', false)
    },    
  }
}
</script>

<style>
.swiper-button-next:after, .swiper-button-prev:after {
  font-size: 18px;
  font-weight: bold;
}
.swiper-button-next, .swiper-button-prev {
  padding-left: -10px;
  margin-left: 0;
  width: 50px;
  height: 50px;
  color:  #35495e;
}
.swiper-horizontal>.swiper-pagination-bullets, .swiper-pagination-bullets.swiper-pagination-horizontal, .swiper-pagination-custom, .swiper-pagination-fraction{
  bottom:0px;
}
.swiper-pagination-bullet.swiper-pagination-bullet-active{
  background-color: #42b883;
  border: 1px solid #35495e;

}

</style>


