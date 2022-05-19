<template>
    <div>
        <green-title class="text-center">checkout</green-title>
        <div class="w-full py-5">
            <table class="w-full">
                <thead class="">
                    <tr class="font-bold border border-solid border-lightGray">
                        <th class="w-1/4 py-3">Product</th>
                        <th class="w-1/4 py-3">Price</th>
                        <th class="w-1/4 py-3">Quantity</th>
                        <th class="w-1/4 py-3">Total</th>
                    </tr>
                </thead>

                <tbody>
                    <tr
                     v-for="item in cart.items"
                     v-bind:key="item.product.id"                    
                    >
                        <td class="text-center py-3">{{ item.product.name }}</td>
                        <td class="text-center py-3">{{ item.product.price }}</td>
                        <td class="text-center py-3">{{ item.quantity }}</td>
                        <td class="text-center py-3">{{ getItemTotal(item).toFixed(2) }} som</td>
                    </tr>
                </tbody>

                <tfoot>
                    <tr class="border border-solid border-lightGray">
                        <td colspan="2" class="font-bold pl-16  py-3 text-red">Total</td>
                        <td class="font-bold text-center">{{ cartTotalLength }}</td>
                        <td class="font-bold text-center">{{ cartTotalPrice.toFixed(2) }} som</td>
                    </tr>
                </tfoot>
            </table>
        </div>

        <div class="contact-box w-full flex">
            <div class="w-3/6 h-full">
                <img src="../../public/Express-delivery.webp" alt="e_shop">
            </div>

            <div class="w-3/6 bg-dark px-10 py-2 items-center">
                <green-title class="form-title text-center font-bold">shipping details</green-title>
                <div class="">
                    <div class="field flex">
                        <label class="text-lightGray">Name *</label>
                        <input type="text" class="" v-model="first_name">
                    </div>

                    <div class="field flex">
                        <label class="text-lightGray">E-mail *</label>
                        <input type="email" class="" v-model="email">
                    </div>                  

                    <div class="field flex">
                        <label class="text-lightGray">Phone *</label>
                        <input type="text" class="" v-model="phone">
                    </div> 
                    
                    <div class="field flex">
                        <label class="text-lightGray">Address *</label>
                        <input type="text" class="" v-model="address">
                    </div>

                    <div class="field flex">
                        <label class="text-lightGray">Comments</label>
                        <input type="text" class="" v-model="comments" >
                    </div> 
                </div>

                <div class="" v-if="errors.length">
                    <p class="text-red" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div> 

                <hr>

                <div id="card-element"></div>
                
                <template v-if="cartTotalLength" class="">
                    <hr>
                    <green-btn class="mt-3" @click="submitForm">Pay with stripe</green-btn>
                </template>           

            </div>

        </div>       
    </div>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import GreenBtn from '@/components/UI/GreenBtn'
import axios from 'axios'

export default {
    name: 'checkout',
    components: {
        GreenTitle,
        GreenBtn
    },
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            email: '',
            phone: '',
            address: '',
            comments: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | e-Kids Shop'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51KqxPuGkcoqpICjCzTOPB6nFsmNyp6PVbgpSF3GgstKEkrpC24Jm9U4S4pqRnl35FqcPf9Sf8FYXxAF8p3jEMClU00EBf33nOf')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('The first name field is missing!')
            }

            if (this.email === '') {
                this.errors.push('The email field is missing!')
            }

            if (this.phone === '') {
                this.errors.push('The phone field is missing!')
            }

            if (this.address === '') {
                this.errors.push('The address field is missing!')
            }

            if (!this.errors.length) {  // empty or no error
                this.$store.commit('setIsLoading', true)

                this.stripe.createToken(this.card).then(result => {
                    if(result.error) {
                        this.$store.commit('setIsLoading', false)

                        this.errors.push('Something went wrong with Stripe. Please try again')

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                product: item.product.id,
                quantity: item.quantity,
                price: item.product.price * item.quantity
                } 
                items.push(obj)
            }   
            
            const data = {
                'first_name': this.first_name,
                'email': this.email,
                'address': this.address,
                'comments': this.comments,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id        // get from the backend
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')

                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>

<style scoped>
label:after { content: ": " }

.form-title{
    position: relative;
    padding-bottom: 10px;
    margin-bottom: 10px;
}
.form-title::after{
    content: '';
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
    height: 4px;
    width: 50px;
    border-radius: 3px;
    background-color: #42b883;
}

.field{
    width: 100%;    
}
.field label{
    color: #fff;
    width: 100px;
}
.field input{
    width: 80%;
    padding: 3px 10px;
    outline: none;
    border: 1px solid #42b883;
    margin-bottom: 5px;
    transition: .3s;
}

</style>
