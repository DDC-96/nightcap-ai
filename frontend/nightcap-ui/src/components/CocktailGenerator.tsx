// src/components/CocktailGenerator.tsx
"use client";

import { useState } from "react";
import axios from "axios";
import { Sparkles } from "lucide-react";

type CocktailResponse = {
  cocktail: string;
};

export default function CocktailGenerator() {
  const [loading, setLoading] = useState(false);
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");

  const handleGenerate = async () => {
    if (!prompt) return;
    setLoading(true);
    try {
      const res = await axios.post<CocktailResponse>(
        "/api/generate-cocktail", // Uses proxy
        { prompt }
      );
      setResult(res.data.cocktail);
    } catch (err) {
      console.error("Error generating cocktail:", err);
      setResult("Something went wrong. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white dark:bg-night text-black dark:text-cream p-6 rounded-xl shadow-xl max-w-2xl mx-auto space-y-4">
      <h2 className="text-2xl font-display flex items-center gap-2">
        <Sparkles className="text-gold" /> Let's Build Your Cocktail!
      </h2>

      <input
        type="text"
        placeholder="What's your vibe? (e.g. A Mezcal Sour Variation)"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        className="w-full px-4 py-2 rounded-md border border-white/20 bg-white/10 backdrop-blur text-inherit focus:outline-none"
      />

      <button
        onClick={handleGenerate}
        disabled={loading}
        className="bg-gold text-night px-4 py-2 rounded-md font-medium hover:brightness-110 transition"
      >
        {loading ? "Mixing..." : "Generate Cocktail"}
      </button>

      {result && (
        <pre className="bg-black/5 dark:bg-white/5 p-4 rounded-md whitespace-pre-wrap border border-white/10">
          {result}
        </pre>
      )}
    </div>
  );
}
