# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
import logging

# Loading Basic Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "*")

if not OPENAI_API_KEY:
    logger.error("Missing Open AI Key in environment variable.")
    raise RuntimeError("Missing OpenAI API key in environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Define app
app = FastAPI()

# Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for POST body
class Prompt(BaseModel):
    prompt: str

# AI Cocktail Generator Endpoint
@app.post("/api/generate-cocktail")
async def generate_cocktail(prompt: Prompt):
    try:
        print("Prompt Recieved:", prompt.prompt)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional mixologist. Return original cocktail recipes in an inviting tone, "
                        "in this format:\n\n"
                        "**Name**: Cocktail Name\n"
                        "**Type**: Classic or Modern Twist\n"
                        "**Description**: A short poetic sentence\n"
                        "**Ingredients**:\n- Ingredient 1\n- Ingredient 2\n"
                        "**Instructions**: One or two clear sentences"
                    ),
                },
                {"role": "user", "content": prompt.prompt},
            ],
            max_tokens=350,
        )
        
        logger.info("OpenAI response recieved.")
        return {"cocktail": response.choices[0].message.content.strip()}
    except Exception as e:
        logger.error("Error Calling OpenAPI:", str(e))
        raise HTTPException(status_code=500, detail=str(e))


# cocktail data
cocktails = [
    {
        "name": "Manhattan",
        "slug": "manhattan",
        "description": "Bold and bitter with Rye Whiskey, Sweet Vermouth, and Angostura Bitters.",
        "longDescription": "The Manhattan is a true classic—bold, spirit-forward, and timeless for any pallete. Originally served in a coupe glass garnished with a delicious marchnino cherry. ",
        "image": "/images/manhattan.jpeg",
        "ingredients": [
            "2 oz Rye Whiskey",
            "1 oz Sweet Vermouth",
            "2 Dashes Angostura Bitters"
        ],
        "instructions": "Stir all ingredients with ice, strain into a chilled coupe, garnish with a cherry.",
        "dateAdded": "2025-06-25T00:00:00Z" 
    },
    {
        "name": "Greenpoint",
        "slug": "greenpoint",
        "description": "Making a dark-moody-sexy drink is as easy as it gets with this Greenpoint cocktail.",
        "longDescription": "The Greenpoint Cocktail is named after a neighborhood in Brooklyn and was first created at the infamous NY cocktail bar, Milk & Honey. The Greenpoint is a variation on the Brooklyn which is also derived from the classic Manhattan. ",
        "image": "/images/greenpoint.jpeg",
        "ingredients": [
            "1/2 oz Sweet Vermouth",
            "1/2 oz Yellow Chartreuse",
            "2 oz Rye Whiskey",
            "1 Dash Orange Bitters",
            "1 Dash Angostura Bitters"
        ],
        "instructions": "Stir all ingredients with ice for approx 30 seconds, strain into a chilled Nick & Nora Coupe, and garnish with a twist of Lemon.",
        "dateAdded": "2025-09-25T00:00:00Z"
    },
    {
        "name": "The Bitter Sun",
        "slug": "the-bitter-sun",
        "description": "Where Mezcal's smoky-ness meets the bittersweet bite of Cynar. Fresh blood orange and citrus for a savory taste.",
        "longDescription": "I was inspired by a drink I had at a bar in LA, similar build, but contained Apricot and Lemon. I liked it, but as I sipped more on the drink, I wanted to put my own twist with Cynar. After messing around with spirits, I landed on something bittersweet and citrus forward with a smoky finish. Using Mezcal and Cynar together give it depth, while blood orange and lime kept it fresh and balanced especially now that oranges are in season. Nothing flashy, just a solid drink to try out in your arsenal if you’ve got Cynar and Blood Oranges on hand. Give it a shot.",
        "image": "/images/the-bitter-sun.jpeg",
        "ingredients": [
            "1 1/2 oz Cynar",
            "1 1/2 oz Juice squeezed from a Blood Orange",
            ".5 oz Lime Juice",
            "1 oz Mezcal",
            "1 Dash Angostura Bitters"
        ],
        "instructions": "Combine all the ingredients into a shaker with ice. Strain into a rocks glass with a big rock and garnish with a zest of a Blood Orange Peel.",
        "dateAdded": "2025-06-25T00:00:00Z"
    },        
    {
        "name": "Penicillin",
        "slug": "penicillin",
        "description": "A modern classic created by the man himself, Sam Ross.",
        "longDescription": "Sam has made many well known cocktails to this date, whilst spending his time behind the bar at infamous NY cocktail bars such as Milk & Honey, Pegu, and Attaboy. The Penicillin combines smoky flavours with sweet honey and spicy ginger to curate this punching bag. ",
        "image": "/images/penicillin.jpeg",
        "ingredients": [
            "1/4 oz Islay Whiskey",
            "2 oz Blended Scotch Whiskey",
            "1/4 oz Ginger Syrup",
            "1/4 oz Honey Syrup",
            "3/4 oz Lemon Juice"
        ],
        "instructions": "Combine all the ingredients into a shaker with ice. Strain into a rocks glass, float Islay Whiskey on top and garnish with ginger candy. I like to throw in zest of a lemon peel to tie it all together."
    },
    {
        "name": "El Jefe",
        "slug": "el-jefe",
        "description": "The Bold Boss of Espresso Martinis. A moody twist of agave and espresso, crafted for the coffee-obssesed.",
        "longDescription": "El Jefe is a bold, agave-forward twist on the classic Espresso Martini, swapping vodka for tequila to create a richer, more daring profile. The earthy warmth of tequila pairs beautifully with the deep roast of espresso and the bittersweet intensity of Mr Black coffee liqueur or sub for an Amaro (Montenegro!). It's smooth, complex, and just the right amount of bitterness for late nights or confident first sips. This one's for the boss in you. ",
        "image": "/images/el-jefe.jpeg",
        "ingredients": [
            "1 oz Tequilla Reposado",
            "2/3 oz Mr Black Coffee Liqueur or any Amaro",
            "1 oz Espresso",
            "1/3 oz Agave Syrup (cut 1:1)"
        ],
        "instructions": "Combine all the ingredients into a shaker with ice. Bonus points for a extra foamy head, dry shake it. Strain into a chilled coupe glass and garnish with espresso powder or beans."
    },
    {
        "name": "Devils Soul",
        "slug": "devils-soul",
        "description": "The advocate in question, with subtle smokiness and bitter notes. If omitted, farewell the soul of the 'Devil'. No Mezcal, no mischief!",
        "longDescription": "The Devil's Soul cocktail is a concoction that seems to have emerged from the speakeasy era, where strong flavors and stiff drinks were the order of the day. It's a drink that's not for the faint-hearted but rather for those who appreciate the complexity and boldness of spirits. ",
        "image": "/images/devils-soul.jpeg",
        "ingredients": [
            "1 oz Rye Whiskey",
            "Barspoon - Averna Amaro",
            "1 oz Mezcal",
            "1/4 oz Elderflower Liqueur",
            "1 Dash Angostura Bitters"
        ],
        "instructions": "Stir with ice in a mixing tin, strain into a rocks glass over a large cube or rocks ice and zest/garnish an Orange Peel."
    },
    {
        "name": "Final Ward",
        "slug": "final-ward",
        "description": "Last Word's cooler older brother.",
        "longDescription": "The Final Ward is arguably the best known riff on the classic, Last Word. It is still compromised of equal parts Rye Whiskey replacing the Gin and Lemon Juice in place of the lime. The Last Word is a Gin based prohibition Cocktail which was making it's way to the scene in recent years. I personally enjoy making these whenever I'm behind the bar and trying to wow someone.",
        "image": "/images/final-ward.jpeg",
        "ingredients": [
            "3/4 oz Green Chartreuse",
            "3/4 oz Maraschino Liqueur",
            "3/4 oz Rye Whiskey",
            "3/4 oz Lime Juice"
        ],
        "instructions": "Combine all the ingredients into a shaker with ice. Strain into a chilled coupe glass and garnish with a zest of a Lemon Peel."
    },
    {
        "name": "Negroni",
        "slug": "negroni",
        "description": "Bitter. Bold. Unapologetic. A ruby red glass of joy with equal parts spirts.",
        "longDescription": "The Negroni is a CLASSIC. Stirred cold, served straight over a giant rock glass or up if you're feeling fancy. The herbal bitterness, and the softness from vermouth add the right amount of complexity to the cocktail. Finish it with an orange twist for a final touch.",
        "image": "/images/negroni.jpeg",
        "ingredients": [
            "1 oz Gin",
            "1 oz Campari",
            "1 oz Sweet Vermouth"
        ],
        "instructions": "Stir with ice in a mixing tin, strain into a rocks glass over a large cube or rocks ice and zest an orange peel."
    },
    {
        "name": "Whiskey Sour",
        "slug": "whiskey-sour",
        "description": "A classic balance of bold, citrus, and sweet. Making it a refreshing yet spirit forward favorite.",
        "longDescription": "The Whiskey Sour is a timeless clash of bright citrus and deep, oaky whiskey-your choice of Bourban, Rye, or Mezcal (my favorite way to drink it.) These days, you'll find it made with egg white (hello, Boston Sour!) for that fire, foamy texture. Though some skip it and drink it without the Egg, which is fine as well. But why miss out on the foamy goodness. Sours are fun to drink and taste amazing when you're rotating spirts. Try it with Mezcal or Tequilla! Other fan favorites that you should try that include Egg White as well are the Ameretto Sour, New York Sour, Aperol Sour, and Pisco Sour.",
        "image": "/images/whiskey-sour.jpeg",
        "ingredients": [
            "2 oz Bourban or Rye Whiskey",
            "3/4 oz Lemon Juice",
            "3/4 oz Simple Syrup or Demarara Syrup",
            "1/2 oz Egg White"
        ],
        "instructions": "If using egg white, dry shake (shake without ice) all ingredients first to emulsify. Add ice and shake until chilled, strain into a rocks glass over a big rock, rocks ice, or in a chilled coupe glass if preffered."
    },
    {
        "name": "Honey Bee",
        "slug": "honey-bee",
        "description": "A simple, citrusy rum forward nightcap sweetened with honey.",
        "longDescription": "The Honey Bee is a warm weather favorite that pairs dark Jamaican rum with floral honey and hits of fruity-ness from the pineapple. It can be tricky at times to come across a bar that carries Pineapple liqeuor, but if they don't they'll most likely sub it for Pineapple juice. It could be a bit sweeter depending if it's packaged (from a Distributor) vs juiced in house. Regardless, pineapple add's that hint of sweetness that pairs well with Dark Rum.",
        "image": "/images/honey-bee.jpeg",
        "ingredients": [
            "2 oz Dark Jamaican Rum",
            "3/4 oz Honey Syrup",
            "1/2 oz Lemon Juice",
            "1/2 oz Pineapple Juice"
        ],
        "instructions": "Shake all ingredients with ice and strain into a chilled coupe..."
    },
    {
        "name": "The Naked and Famous",
        "slug": "naked-and-famous",
        "description": "The Naked and Famous is the smoky, citrusy cousin of the Paper Plane. A fire blend of smoky Mezcal, bitter Aperol, and lime.",
        "longDescription": "The Naked and Famous is a sleek, modern craft cocktail that plays a smoky, herbal, bitter, and sour harmony at it's first sip. Quick to make, and great introduction to craft cocktails to those wanting to try and order something new at a bar. Definitely worth adding to your rotation. Cheers!",
        "image": "/images/naked-and-famous.jpeg",
        "ingredients": [
            "3/4 oz Mezcal (preferbly Del Maguey Chichicapa)",
            "3/4 oz Aperol",
            "3/4 oz Yellow Chartreuse",
            "3/4 oz Lime Juice"
        ],
        "instructions": "Add all ingredients into a shaker filled with ice. Shake until chilled (15-20 seconds). Strain into a chilled coupe glass and garnish with a lime wheel or twist!"
    },
    {
        "name": "Too Soon",
        "slug": "too-soon",
        "description": "A dark, herbal, and citrusy punch of a drink that highlights Cynar Amaro very well.",
        "longDescription": "The Too Soon is a modern classic by NYC cocktail legend Sam Ross (creator of the Penicillin and Paper Plane). Vibrant citrus and herbal aromas lead into a complex, bittersweet, thanks to the magic of Cynar which shines brilliantly in this balance of fresh and bold.",
        "image": "/images/too-soon.jpeg",
        "ingredients": [
            "1 oz Cynar",
            "1 oz Gin",
            "3/4 oz Lemon Juice",
            "1/2 oz Simple Syrup"
        ],
        "instructions": "Stir with ice and strain into a rocks glass or coupe. Garnish with a bouqet of Mint."
    }
]

# GET all cocktails
@app.get("/api/cocktails")
def get_all_cocktails():
    logger.info("GET /api/cocktails called")
    return cocktails

# GET cocktail by slug
@app.get("/api/cocktails/{slug}")
def get_cocktail_by_slug(slug: str):
    logger.info(f"GET /api/cocktails/{slug} called")
    for cocktail in cocktails:
        if cocktail["slug"] == slug:
            return cocktail
    logger.warning(f"Cocktail not found: {slug}")
    raise HTTPException(status_code=404, detail="Cocktail not found")
