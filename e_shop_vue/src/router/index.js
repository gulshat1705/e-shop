import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AllProducts from '@/views/AllProducts'
import Search from '@/views/Search'
import Category from '@/views/Category'
import Product from '@/views/Product'
import SignUp from '@/views/SignUp'
import Cart from '@/views/Cart'
import Checkout from '@/views/Checkout'
import LogIn from '@/views/LogIn'
import MyAccount from '@/views/MyAccount'
import store from '@/store'
 
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
    path: '/log-in',
    name: 'log-in',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'my-account',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
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
  {
    path: '/cart/checkout',
    name: 'checkout',
    component: Checkout,

  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'log-in', query: { to: to.path } });
  } else {
    next()
  }
})


export default router
