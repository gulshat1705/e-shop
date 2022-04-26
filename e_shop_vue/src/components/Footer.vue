<template>
    <footer>
        <div class="footer-wrap container">
            
            <div class="footer-item contacts">
                <green-title>contacts</green-title>                
                <div>
                    <i></i><p>phone number</p>
                </div>
                <div>
                    <i></i><a href="#">instagram</a>
                </div>
                <div>
                    <i></i><a href="#">telegram</a>
                </div> 
                <div>
                    <i></i><a href="#">whatsapp</a>
                </div>                
            </div>

            <div class="footer-item payment">
                <green-title>methods of payment</green-title>

            </div>

            <div class="footer-item mailing">
                <green-title>newsletter subscriptions</green-title>

            </div>
        </div>

        <p class="copyright">Copyright (c) 2022</p>
        
    </footer>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'

export default {
    components: { GreenTitle }
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