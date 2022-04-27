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
    }
  },
  actions: {
  },
  modules: {
  }
})
