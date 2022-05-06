<template>
    <div>
        <dark-title>order #{{ order.id}}</dark-title>

        <green-title>products</green-title>

        <table>
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="item in order.items"
                    v-bind:key="item.product.id"
                >
                    <td>{{ item.product.name }}</td>
                    <td>{{ item.product.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ getItemTotal(item).toFixed(2) }}</td> 
                </tr>
            </tbody>
        </table>

    </div>
    <hr>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'
import DarkTitle from '@/components/UI/DarkTitle'

export default {
    name: 'OrderSummary',
    components: {
        GreenTitle,
        DarkTitle,        
    },
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        orderTotalLength(order) {
            return order.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}

</script>
