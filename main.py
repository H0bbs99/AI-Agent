import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


if len(sys.argv) > 1 :
     ai_prompt = sys.argv[1]
else:
     raise ValueError("Please provide a prompt as a command-line argument.")

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=ai_prompt)

# Output the response from the API
print(f"Response: {response.text}")

print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")