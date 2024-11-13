/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6', // Tailwind's default blue, but can adjust for branding
        secondary: '#64748b',
        sky: '#0ea5e9', // custom colors if needed
        lavender: '#7e5bef',
        rose: '#f43f5e',
      },
    },
  },
  plugins: [],
}

