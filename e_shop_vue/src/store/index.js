import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,


//    accessToken: null,
  //  refreshToken: null,
    access: '',
    refresh: '',
  //  token: '',
    isLoading: false
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }

      if (localStorage.getItem('access')) {
        state.access = localStorage.getItem('access')
        state.refresh = localStorage.getItem('refresh')
        state.isAuthenticated = true
      } else {
        state.access = ''
        state.refresh = ''
        state.isAuthenticated = false
      }
      

    //  if (localStorage.getItem('token')) {
    //    state.token = localStorage.getItem('token')
    //    state.isAuthenticated = true
    //} else {
    //    state.token = ''
    //    state.isAuthenticated = false
    //  }      
    },

    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    setIsLoading(state, status) {
      state.isLoading = status
    },

    setAccess(state, access) {
      state.access = access
    

  //  setToken(state, token) {
    //  state.accessToken = null
    //  state.refreshToken = null
      
    //  state.token = token
      state.isAuthenticated = true
    },
    setRefresh(state, refresh) {
      state.refresh = refresh
    },
    
    removeToken(state) {
      state.access = ''
      state.isAuthenticated = false
    },
    clearCart(state) {
      state.cart = { items: []}
      localStorage.setItem('cart', JSON.stringify(state.cart))  // после заполнения номер карт и тд очистились
    },
  },
  actions: {
  },
  modules: {
  }
})
