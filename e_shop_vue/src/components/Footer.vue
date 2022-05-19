<template>
    <footer class="bg-dark">
        <div class="max-w-7xl mx-auto py-5 flex">
            <div class="w-1/4">
                <green-title class="text-center">Contacts</green-title>
                <div class="flex flex-wrap justify-center text-xl space-x-2 pl-6">
                    <i class="fa-solid fa-phone-volume text-white pt-1"></i>
                    <p class="text-lightGray">0771 67 67 51</p>
                </div>
                <div class="flex flex-wrap justify-center text-xl space-x-2">
                    <a href="https://whatsapp.com" class="flex flex-wrap justify-center text-xl space-x-2 cursor-pointer pl-6">
                        <i class="fa-brands fa-whatsapp text-white text-2xl"></i>
                        <i class="text-lightGray  hover:text-white">0771 67 67 51</i>
                    </a>                    
                </div> 

                <div class="flex flex-wrap justify-center text-xl space-x-2">
                    <a href="https://instagram.com" class="flex flex-wrap justify-center text-xl space-x-4 cursor-pointer">
                        <i class="fa-brands fa-instagram-square text-white text-2xl"></i>
                        <i class="text-lightGray  hover:text-white">instagram</i>
                    </a>
                </div> 

                <div class="flex flex-wrap justify-center text-xl space-x-2">
                    <a href="https://telegram.com" class="flex flex-wrap justify-center text-xl space-x-6 cursor-pointer">
                        <i class="fa-brands fa-telegram text-white text-2xl"></i>
                        <i class="text-lightGray  hover:text-white mx-0">telegram</i>
                    </a>
                </div> 
            </div>

            <div class="w-1/4">
                <green-title class="text-center">methods of payment</green-title>
                <div class="flex flex-wrap justify-center text-xl space-x-2 my-5">
                    <img height="40" src="https://shoplineimg.com/assets/footer/card_visa.png"/>
                    <img height="40" src="https://shoplineimg.com/assets/footer/card_master.png"/>
                    <img height="40" src="https://shoplineimg.com/assets/footer/card_paypal.png"/>
                </div>    
            </div>

            <div class="w-2/4 pl-10 pr-36 border-l-2 border-solid border-lightGray">
                <green-title class="text-left">newsletter subscriptions</green-title>
                <form>
                    <div class="w-full">
                        <input class="w-full my-2 py-2 px-3 rounded-md" type="text" placeholder="Name" name="name" required>
                        <input class="w-full my-2 py-2 px-3 rounded-md" type="text" placeholder="Email address" name="mail" required>

                    </div>

                    <green-btn type="submit" class="mt-2 rounded-md">subscribe</green-btn>
                </form>
            </div>
        </div>

        <p class="copyright">Copyright (c) 2022</p>
        
    </footer>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import GreenBtn from '@/components/UI/GreenBtn'

export default {
    components: { 
        GreenTitle,
        GreenBtn
    }
}


</script>

<style scoped>
.copyright{
    color: #615e5e;
    font-size: 14px;
    display: block;
    padding: 10px;
    background: #fff;
    text-align: center;

}
</style>