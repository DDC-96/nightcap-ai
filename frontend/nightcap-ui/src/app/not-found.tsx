// src/app/not-found.tsx
import Link from "next/link";

export default function NotFound() {
  return (
    <main className="min-h-screen bg-night text-cream flex flex-col items-center justify-center p-8 text-center">
      <h1 className="text-5xl font-display mb-4">404 — Not Found</h1>
      <p className="text-white/80 mb-6">
        This page doesn’t exist. Please check your internet activity.
      </p>
      <Link
        href="/"
        className="text-gold border border-gold px-4 py-2 rounded hover:bg-gold hover:text-night transition"
      >
        Back to Home
      </Link>
    </main>
  );
}
