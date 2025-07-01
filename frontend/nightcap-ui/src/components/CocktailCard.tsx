"use client";

import Image from "next/image";
import Link from "next/link";
import { motion } from "framer-motion";
import { formatDistanceToNow, parseISO, differenceInDays } from "date-fns";

interface CocktailCardProps {
  name: string;
  description: string;
  image: string;
  slug: string;
  dateAdded?: string;
}

export default function CocktailCard({
  name,
  description,
  image,
  slug,
  dateAdded,
}: CocktailCardProps) {
  const now = new Date();
  const addedDate = dateAdded ? parseISO(dateAdded) : null;
  const isNew = addedDate && differenceInDays(now, addedDate) <= 10;
  const daysAgo = addedDate ? formatDistanceToNow(addedDate, { addSuffix: false }) : null;

  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      transition={{ type: "tween", duration: 0.3 }}
      className="card-glass relative group overflow-hidden bg-white/5 backdrop-blur-md p-4 rounded-2xl shadow-lg border border-white/10"
    >
      {/* Image */}
      <div className="relative w-full h-64 mb-4 overflow-hidden rounded-xl">
        <Image
          src={image}
          alt={name}
          fill
          className="object-cover group-hover:scale-105 transition-transform duration-500 ease-in-out"
        />

        {/* Subtle glass overlay */}
        <div className="absolute inset-0 bg-black/30 backdrop-blur-[1.5px] opacity-60 group-hover:opacity-0 group-hover:backdrop-blur-none pointer-events-none transition-all duration-700 ease-out z-0" />
      </div>

      {/* Text content */}
      <div className="relative z-10 group-hover:opacity-100 opacity-60 transition duration-500 ease-in-out">
        <h2 className="text-xl font-display text-gold mb-1">{name}</h2>
        <p className="text-sm text-white/70 mb-4 line-clamp-3">{description}</p>

        <div className="flex items-center justify-start space-x-2 mt-2">
          <Link
            href={`/recipe/${slug}`}
            className="inline-block px-4 py-2 border border-gold text-gold rounded-full text-sm font-medium transition hover:bg-gold hover:text-night"
          >
            Recipe
          </Link>

          {isNew && (
            <span className="text-[10px] text-green-400 border border-green-400 px-2 py-0.5 rounded-full bg-black/30 backdrop-blur-sm">
              NEW · Uploaded {daysAgo} ago
            </span>
          )}
        </div>
      </div>
    </motion.div>
  );
}
