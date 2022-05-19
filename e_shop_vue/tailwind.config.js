module.exports = {
  //content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {

    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      white: 'white',
      green: '#42b883',
      red: '#ff2800',
      dark: '#35495e',
      dark500: 'rgb(75 85 99)',
      gray: '#615e5e',
      lightGray: 'rgb(203 213 225)'
    },   

    screens: {
      '2xl': {'max': '1535px'},
      // => @media (max-width: 1535px) { ... }

      'xl': {'max': '1279px'},
      // => @media (max-width: 1279px) { ... }

      'lg': {'max': '1090px'},
      // => @media (max-width: 1023px) { ... }

      'md': {'max': '767px'},
      // => @media (max-width: 767px) { ... }

      'sm': {'max': '639px'},
      // => @media (max-width: 639px) { ... }
    }
  },
  plugins: [],
}
