import os

from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GOOGLE_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello! Tell me your name in one sentence."
)

print(response.text)