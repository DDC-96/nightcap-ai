"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { motion, useScroll, useMotionValueEvent } from "framer-motion";

export default function Header() {
  const [scrollDirection, setScrollDirection] = useState<"up" | "down">("up");

  const { scrollY } = useScroll();

  useMotionValueEvent(scrollY, "change", (latest) => {
    const previous = scrollY.getPrevious() ?? 0;
    if (latest > previous && latest > 10) {
      setScrollDirection("down");
    } else if (latest < previous) {
      setScrollDirection("up");
    }
  });

  const isVisible = scrollDirection === "up";

  return (
    <motion.header
      initial={{ y: 0, opacity: 1 }}
      animate={{
        y: isVisible ? 0 : -80,
        opacity: isVisible ? 1 : 0,
      }}
      transition={{ duration: 0.3, ease: "easeInOut" }}
      className="w-full px-6 sticky top-0 z-50 transition-all duration-300 backdrop-blur-sm border-b border-neutral-800 bg-neutral-900/70 py-3"
    >
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: isVisible ? 1 : 0, scale: isVisible ? 1 : 0.95 }}
        transition={{ duration: 0.3, ease: "easeInOut" }}
        className="max-w-7xl mx-auto flex items-center justify-between"
      >
        <Link
          href="/"
          className="text-xl font-display font-bold text-white transition lg:-ml-4"
        >
          Nightcap<span className="text-gold">.</span>
        </Link>

        <nav className="flex items-center space-x-6 text-sm">
          <Link href="/" className="text-neutral-300 hover:text-white transition">
            Home
          </Link>
          <Link
            href="/ai-generator"
            className="text-neutral-300 hover:text-white transition"
          >
            Cocktail AI Generator
          </Link>
        </nav>
      </motion.div>
    </motion.header>
  );
}
