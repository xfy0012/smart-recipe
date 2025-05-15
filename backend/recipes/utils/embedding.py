import os
import voyageai
from dotenv import load_dotenv

load_dotenv()

client = voyagai.Client()

def build_embedding_input(doc):
    title = doc.get("title", "").strip()
    ingredients = [i.strip() for i in doc.get("ingredients", []) if i.strip()]
    instructions = doc.get("instructions", "").strip()
    
    return f"""Recipe title: {title}
Ingredients: {", ".join(ingredients)}
Instructions: {instructions}
"""

def generate_embedding(doc):
    text = build_embedding_input(doc)
    result = client.embed([text], model="voyage-3.5-lite", input_type="document")
    return result.embeddings[0]
    
