"use client";

import Header from "@/components/Header";
import CocktailGenerator from "@/components/CocktailGenerator";

export default function AIGeneratorPage() {
  return (
    <>
      <Header />
      <main className="min-h-screen px-6 pt-20 transition-colors duration-300 bg-night text-cream">
        <section className="max-w-4xl mx-auto text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-display text-gold mb-4">
            Cocktail AI Generator
          </h1>
          <p className="text-white/60 max-w-xl mx-auto text-sm">
            Craft your next drink with a little help from our custom-trained cocktail companion.
          </p>
        </section>

        <CocktailGenerator />
      </main>
    </>
  );
}
