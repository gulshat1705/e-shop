<template>
    <div>
        <green-title>thank you</green-title>
    </div>
</template>

<script>
import GreenTitle from '@/components/UI/GreenTitle'

export default {
    name: 'success',
    components: {
        GreenTitle
    },
    mounted() {
        document.title = 'Success | e-Kids Shop'
    }
}
</script>
