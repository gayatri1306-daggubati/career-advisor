<<<<<<< HEAD
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Suggest 3 careers for someone interested in coding and art.")
print(response.text)
=======
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Suggest 3 careers for someone interested in coding and art.")
print(response.text)
>>>>>>> db06363a0da4f63e1601dc714478633b7316e50e
