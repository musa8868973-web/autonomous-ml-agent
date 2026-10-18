import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_ml_script(prompt):
    print("[LLM Brain] Thinking and writing Python code...")
    # Yahan Groq API call aayegi
    return "# AI Generated Python Code Will Be Here"