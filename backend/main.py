# main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("Missing OpenAI API key in environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Define app
app = FastAPI()

# Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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
        
        print("OpenAI response recieved.")
        return {"cocktail": response.choices[0].message.content.strip()}
    except Exception as e:
        print("Error Calling OpenAPI:", str(e))
        raise HTTPException(status_code=500, detail=str(e))


# Static cocktail data
cocktails = [
    {
        "name": "Manhattan",
        "slug": "manhattan",
        "description": "Bold and bitter with Rye Whiskey, Sweet Vermouth, and Angostura Bitters.",
        "longDescription": "The Manhattan is a true classic—bold, spirit-forward, and timeless for any pallete. Originally served in a coupe glass garnished with a delicious marchnino cherry. It's always a fan favorite. ",
        "image": "/images/manhattan.jpeg",
        "ingredients": [
            "2 oz Rye Whiskey",
            "1 oz Sweet Vermouth",
            "2 Dashes Angostura Bitters"
        ],
        "instructions": "Stir all ingredients with ice, strain into a chilled coupe, garnish with a cherry."
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
        "instructions": "Stir all ingredients with ice for approx 30seconds, strain into a chilled Nick & Nora Coupe, and garnish with a twist of Lemon."
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
        "longDescription": "The Final Ward is arguably the best known riff on the classic, Last Word. It is still compromised of equal parts Rye Whiskey replacing the Gin and Lemon Juice in place of the lime. The Last Word is a Gin based prohibition Cocktail which was rediscovered roughly in 04' and becoming a cult hit in the Seattle area.  ",
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
        "description": "This cocktail resembles the Americano (minus the soda and replaced with gin)...",
        "longDescription": "The Negroni is an iconic Italian aperitif — equal parts bitter campari or bordiga, Sweet Vertmouth - Antica, and any choice of Gin. It packs a punch and is a go to classic. If you're looking to change things up, order a Negroni with Mezcal instead of with Gin. It's smoky, elegant, and bold in flavor that compliments the citrus and bitter notes from the Campari.",
        "image": "/images/negroni.jpeg",
        "ingredients": [
            "1 oz Gin",
            "1 oz Campari",
            "1 oz Sweet Vermouth"
        ],
        "instructions": "Stir with ice in a mixing tin, strain into a rocks glass over a large cube or rocks ice and zest an orange peel or orange wedge."
    },
    {
        "name": "Whiskey Sour",
        "slug": "whiskey-sour",
        "description": "Neal's recipe is my personal favorite. Using an Over Proof Rye Whisky.",
        "longDescription": "The Whiskey Sour is a beloved balance of bright citrus and rich whiskey with Bourban or Rye. Take it up a notch and sub the Whiskey for Mezcal.",
        "image": "/images/whiskey-sour.jpeg",
        "ingredients": [
            "2 oz Bourban or Rye Whiskey",
            "3/4 oz Lemon Juice",
            "3/4 oz Simple Syrup or Demarara Syrup",
            "1/2 oz Egg White"
        ],
        "instructions": "Shake all ingredients with ice then (Dry Shake) then strain into a chilled coupe glass or a rocks glass with a big rock, upon request."
    },
    {
        "name": "Honey Bee",
        "slug": "honey-bee",
        "description": "A simple, citrusy rum cocktail sweetened with golden honey.",
        "longDescription": "The Honey Bee is a warm weather favorite that pairs dark Jamaican rum with floral honey and hits of fruity-ness from the pineapple. It can be tricky at times to come across a bar that carries Pineapple liqeuor, but if they don't they'll most likely sub it for Pineapple juice. It could be a bit sweeter depending if it's packaged (from a Distributor) vs juiced in house. Regardless, pineapple add's that hint of sweetness that pairs well with Dark Rum.",
        "image": "/images/honey-bee.jpeg",
        "ingredients": [
            "2 oz Dark Jamaican Rum",
            "3/4 oz Honey Syrup",
            "1/2 oz Lemon Juice",
            "1/2 oz Pineapple Liqeuor or Juice"
        ],
        "instructions": "Shake all ingredients with ice and strain into a chilled coupe..."
    },
    {
        "name": "Naked and Famous",
        "slug": "naked-and-famous",
        "description": "The Naked and Famous is the smoky, citrusy cousin of the Paper Plane.",
        "longDescription": "A balanced mix of Mezcal, Aperol, Yellow Chartreuse, and Lime Juice, created at Death & Co...",
        "image": "/images/naked-and-famous.jpeg",
        "ingredients": [
            "3/4 oz Mezcal",
            "3/4 oz Aperol",
            "3/4 oz Yellow Chartreuse",
            "3/4 oz Lime Juice"
        ],
        "instructions": "Shake with ice and strain into a coupe. No garnish needed."
    },
    {
        "name": "Too Soon",
        "slug": "too-soon",
        "description": "Order this at a bar, and impress your friends or your date!",
        "longDescription": "A contemporary cocktail created by Sam Ross of Attaboy, NY...",
        "image": "/images/too-soon.jpeg",
        "ingredients": [
            "1 oz Bourbon or Rye",
            "1 oz Campari",
            "1 oz Sweet Vermouth"
        ],
        "instructions": "Stir with ice and strain into a rocks glass or coupe. Garnish with an orange twist."
    }
]

# GET all cocktails
@app.get("/api/cocktails")
def get_all_cocktails():
    return cocktails

# GET cocktail by slug
@app.get("/api/cocktails/{slug}")
def get_cocktail_by_slug(slug: str):
    for cocktail in cocktails:
        if cocktail["slug"] == slug:
            return cocktail
    raise HTTPException(status_code=404, detail="Cocktail not found")
