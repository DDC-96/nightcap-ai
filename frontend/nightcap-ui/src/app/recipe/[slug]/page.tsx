// src/app/recipe/[slug]/page.tsx
import { notFound } from "next/navigation";
import Link from "next/link";
import Image from "next/image";
import { ArrowLeft } from "lucide-react";

type Cocktail = {
  name: string;
  slug: string;
  description: string;
  longDescription: string;
  image: string;
  ingredients: string[];
  instructions: string;
};

type Props = {
  params: { slug: string };
};

export default async function RecipePage({ params }: Props) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/cocktails/${params.slug}`, {
    cache: "no-store",
  });

  if (!res.ok) return notFound();

  const recipe: Cocktail = await res.json();

  return (
    <main className="min-h-screen bg-night text-cream px-6 py-12 max-w-2xl mx-auto">
      <Link
        href="/"
        className="flex items-center text-gold hover:text-gold/80 transition mb-6 font-medium"
      >
        <ArrowLeft className="mr-2 w-5 h-5" />
        Back
      </Link>

      <h1 className="text-4xl font-display mb-4">{recipe.name}</h1>

      <div className="mb-6">
        <Image
          src={`/images/${recipe.slug}.jpeg`}
          alt={recipe.name}
          width={800}
          height={400}
          className="w-full h-[300px] object-cover rounded-2xl shadow-lg"
        />
      </div>

      <p className="text-white/80 leading-relaxed mb-8 border-l-4 border-gold pl-4 italic">
        {recipe.longDescription}
      </p>

      <div className="mb-8">
        <h2 className="text-xl font-semibold text-gold tracking-wide uppercase mb-3 border-b border-white/10 pb-1">
          Ingredients
        </h2>
        <ul className="list-disc list-inside space-y-1">
          {recipe.ingredients.map((item, idx) => (
            <li key={idx} className="text-white/90">
              {item}
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h2 className="text-xl font-semibold text-gold tracking-wide uppercase mb-3 border-b border-white/10 pb-1">
          Instructions
        </h2>
        <p className="text-white/90 leading-relaxed">{recipe.instructions}</p>
      </div>
    </main>
  );
}
