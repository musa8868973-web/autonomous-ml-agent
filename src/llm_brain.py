import os 
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("[Error] GROQ_API_KEY is missing. Please check your .env file.")

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

def generate_ml_script(prompt):
    print("[LLM Brain] Thinking and writing Python code...")
    
    # System prompt forces the AI to act as a strict code generator
    system_prompt = (
        "You are an expert ML-Ops AI. You write clean, executable Python code for Machine Learning pipelines. "
        "Return ONLY the raw python code. Do NOT include markdown formatting (like ```python) or any explanations."
    )
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant", # Using Llama-3 8B for fast inference
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# API Error: {str(e)}"
