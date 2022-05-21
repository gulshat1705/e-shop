<template>
  <div class="carousel">
      <slot :currentSlide="currentSlide" />
    <!--Navigation -->
      <div v-if="navEnabled" class="navigate px-10 h-full w-full absolute flex justify-center items-center">
            <div class="toggle-page-left justify-start"> PREV
                <i @click="prevSlide" class="fa-solid fa-circle-chevron-left text-green cursor-pointer"></i>
            </div>

            <div class="toggle-page-right justify-end">NEXT
                <i @click="nextSlide" class="fa-solid fa-circle-chevron-right text-green cursor-pointer"></i>
            </div>            
      </div>
      <!--Pagination-->
      <div v-if="paginationEnabled" class="pagination absolute bottom-5 w-full flex justify-center items-center gap-6">
          <span @click="goToSlide()" class="cursor-pointer bg-red w-10 h-10"
            v-for="(slide, index) in getSlideCount"
           :key="index"
           :class="{active : index + 1 === currentSlide}"
           >
            {{ slide }}
          </span>

      </div>

  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
    props: ["startAutoPlay", "timeout", "navigation", "pagination"],
    setup(props) {
        const currentSlide = ref(1);
        const getSlideCount = ref(null);
        const autoPlayEnabled =  ref(props.startAutoPlay === undefined ? true : props.startAutoPlay);;
        const timeoutDuration = ref(props.timeout === undefined ? 5000 : props.timeout);
        const paginationEnabled = ref(props.pagination === undefined ? true : props.pagination);
        const navEnabled = ref(props.navigation === undefined ? true : props.navigation);

        const nextSlide = () => {
            if (currentSlide.value === getSlideCount.value) {
                currentSlide.value = 4
                return
            }
            currentSlide.value += 1
        };
            
        const prevSlide = () => {
            if(currentSlide.value === 1) {
                currentSlide.value = 1;
                return;
            }
            currentSlide.value -=1;
        };   
        const goToSlide = (index) => {
            currentSlide.value = index + 1
        };
        // autoplay
        const autoPlay = () => {
            setInterval(() => {
                nextSlide()
            }, timeoutDuration.value);
        };
        if (autoPlayEnabled.value) {
            autoPlay();
        }
        onMounted(() => {
            getSlideCount.value = document.querySelectorAll('.slide').length
        });

        return { currentSlide, nextSlide, prevSlide, getSlideCount, goToSlide, paginationEnabled, navEnabled}
    }

}
</script>

<style>
.active{
background-color: aqua;
}
</style>