import type { Config } from 'tailwindcss';

const config: Config = {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'], // Ensure it scans all files
  theme: { extend: {} },
  plugins: [],
};

export default config;
