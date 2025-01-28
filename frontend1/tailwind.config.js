module.exports = {
  theme: {
    extend: {
      transitionProperty: {
        all: 'all',
      },
      transitionDuration: {
        300: '400ms',
      },
      transitionTimingFunction: {
        'ease-in-out': 'ease-in-out',
      },
    },
  },
  content: ['./public/index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
