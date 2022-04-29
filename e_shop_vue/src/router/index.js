import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AllProducts from '@/views/AllProducts'
import Search from '@/views/Search'
import Category from '@/views/Category'
import Product from '@/views/Product'
import SignUp from '@/views/SignUp'
import Cart from '@/views/Cart'
 
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/all-products',
    name: 'all-products',
    component: AllProducts
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUp
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart
  },

  {
    path: '/:category_slug/:product_slug',
    name: 'product',
    component: Product
  },
  {
    path: '/:category_slug',
    name: 'category',
    component: Category
  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})



export default router
