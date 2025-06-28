"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import CocktailGenerator from "@/components/CocktailGenerator";
import CocktailCard from "@/components/CocktailCard";
import ThemeToggle from "@/components/ThemeToggle";

interface Cocktail {
  name: string;
  slug: string;
  description: string;
  longDescription: string;
  image: string;
  ingredients: string[];
  instructions: string;
}

export default function Home() {
  const [cocktails, setCocktails] = useState<Cocktail[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/cocktails`)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return res.json();
      })
      .then((data) => {
        setCocktails(data);
        setError(null);
      })
      .catch((err) => {
        console.error("Failed to fetch cocktails:", err);
        setError("Failed to load cocktails. Please refresh the page.");
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  if (error) return <div className="min-h-screen flex items-center justify-center text-red-500">{error}</div>;

  return (
    <main className="min-h-screen py-12 px-6 transition-colors duration-300 bg-night text-cream dark:bg-night dark:text-cream light:bg-white light:text-black">
      <ThemeToggle />

      <section className="relative text-center mb-16">
        <div className="absolute inset-0 h-[200px] bg-gradient-to-b from-gold/10 to-transparent blur-2xl pointer-events-none" />
        <h1 className="text-6xl md:text-7xl font-display tracking-wide z-10 relative">
          Nightcap<span className="text-gold">.</span>
        </h1>
        <p className="text-white/60 dark:text-white/60 light:text-black/60 text-sm md:text-base mt-2 z-10 relative italic">
          Curated classics & modern pours.
        </p>
      </section>

      <CocktailGenerator />

      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        transition={{ staggerChildren: 0.15 }}
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto mt-12"
      >
        {cocktails.map((cocktail, index) => (
          <motion.div
            key={cocktail.slug}
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: index * 0.1 }}
          >
            <CocktailCard {...cocktail} />
          </motion.div>
        ))}
      </motion.div>
    </main>
  );
}