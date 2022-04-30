<template>
    <div>
        <green-title>checkout</green-title>
        <div class="">
            <table class="">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Totsl</th>
                    </tr>
                </thead>

                <tbody>
                    <tr
                     v-for="item in cart.items"
                     v-bind:key="item.product.id"                    
                    >
                        <td>{{ item.product.name }}</td>
                        <td>{{ item.product.price }}</td>
                        <td>{{ item.quantity }}</td>
                        <td>{{ getItemTotal(item).toFixed(2) }} som</td>
                    </tr>
                </tbody>

                <tfoot>
                    <tr>
                        <td colspan="2">Total</td>
                        <td>{{ cartTotalLength }}</td>
                        <td>{{ cartTotalPrice.toFixed(2) }} som</td>
                    </tr>
                </tfoot>
            </table>
        </div>

        <div>
            <green-title>shipping details</green-title>
            <p class="text-gray">*All fields are required</p>
        </div>

        <div>
            <div class="">
                <label>First name *</label>
                <input type="text" class="" v-model="first_name">
            </div>

            <div class="">
                <label>Last name *</label>
                <input type="text" class="" v-model="last_name">
            </div> 

            <div class="">
                <label>E-mail *</label>
                <input type="email" class="" v-model="email">
            </div>  

            <div class="">
                <label>Phone *</label>
                <input type="text" class="" v-model="phone">
            </div>  

            <div class="">
                <label>Address *</label>
                <input type="text" class="" v-model="address">
            </div>

            <div class="">
                <label>Zip code*</label>
                <input type="text" class="" v-model="zipcode">
            </div> 

            <div class="">
                <label>Place *</label>
                <input type="text" class="" v-model="place">
            </div>                                                                  
        </div>

        <div class="" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <hr>

        <div id="card-element"></div>

        <template v-if="cartTotalLength">
            <hr>

            <green-btn @click="submitForm">Pay with stripe</green-btn>
        </template>
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
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | e-Kids Shop'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('sk_test_51KqxPuGkcoqpICjCjjXcuKkUnW3iAOutwjpwdYIz1QqcMHiZb57FtS9PTczj0No42B7lQiRrMII4uL8R9zQdOoiq00cmCWxg92')
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

            if (this.last_name === '') {
                this.errors.push('The last name field is missing!')
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

            if (this.zipcode === '') {
                this.errors.push('The zip code field is missing!')
            }

            if (this.place === '') {
                this.errors.push('The place field is missing!')                
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
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
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
