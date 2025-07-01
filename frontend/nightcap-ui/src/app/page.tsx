"use client";

// import CocktailGenerator from "@/components/CocktailGenerator";
import { useEffect, useState, useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import CocktailCard from "@/components/CocktailCard";
import Header from "@/components/Header";

interface Cocktail {
  name: string;
  slug: string;
  description: string;
  longDescription: string;
  image: string;
  ingredients: string[];
  instructions: string;
  dateAdded?: string; // Fetching dateAdded API 
}


export default function Home() {
  const [cocktails, setCocktails] = useState<Cocktail[]>([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/cocktails`)
      .then((res) => res.json())
      .then((data) => setCocktails(data))
      .catch((err) => console.error("Failed to fetch cocktails:", err));
  }, []);

  // Scroll-linked animation setup
  const heroRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: heroRef,
    offset: ["start start", "150px start"], // fade begins ~150px down
  });

  const opacity = useTransform(scrollYProgress, [0, 1], [1, 0]);
  const y = useTransform(scrollYProgress, [0, 1], [0, -30]);

  return (
    <>
      <Header />

      <main className="min-h-screen px-6 pt-12 transition-colors duration-300 bg-night text-cream">
        {/* Hero Section */}
        <section ref={heroRef} className="relative text-center mb-16 pt-28">
          {/* Flicker Background Glow */}
          <div className="absolute inset-0 h-[200px] bg-gradient-to-b from-gold/10 to-transparent blur-2xl pointer-events-none" />

          <motion.h1
            style={{ opacity, y }}
            className="text-6xl md:text-7xl font-display tracking-wide z-10 relative"
          >
            Nightcap<span className="text-gold">.</span>
          </motion.h1>

          <motion.p
            style={{ opacity, y }}
            className="text-white/60 text-sm md:text-base mt-2 z-10 relative italic"
          >
            Curated classics & modern pours.
          </motion.p>
        </section>
{/* 
        Cocktail Generator
        <CocktailGenerator /> */}

        {/* Cocktail Grid */}
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
    </>
  );
}
