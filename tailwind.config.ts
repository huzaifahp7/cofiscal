import type { Config } from "tailwindcss";
const { nextui } = require("@nextui-org/react");

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      gridTemplateColumns: {
        "17": "repeat(17, minmax(0, 1fr))",
      },
    },
  },
  darkMode: "class",
  plugins: [nextui({
    themes: {
      light: {
        colors: {
          
        }
      }
    }
  }),
  require('tailwind-scrollbar')({ nocompatible: true }),
],
};
export default config;
