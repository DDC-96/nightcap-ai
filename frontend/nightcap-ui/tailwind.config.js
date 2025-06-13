module.exports = {
  darkMode: "class",
  content: ["./src/**/*.{js,ts,jsx,tsx}"], // 🛠 Prevent performance issues
  theme: {
    extend: {
      colors: {
        night: "#0a0a0a",
        cream: "#f1efe7",
        gold: "#c8a96a",
      },
      fontFamily: {
        sans: "var(--font-sans)",
        display: "var(--font-display)",
      },
    },
  },
  plugins: [],
};
