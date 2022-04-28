import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    }
  },
  getters: {
  },
  mutations: {
    setIsLoading(state, status) {
      state.IsLoading = status
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.id === item.product.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      } else {
        state.cart.items.push(item)
      }
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }

  },
  actions: {
  },
  modules: {
  }
})
