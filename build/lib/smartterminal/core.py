import subprocess
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_command(natural_input: str) -> str:
    prompt = f"""You're a terminal assistant. Convert this natural language into a Linux terminal command.
Natural language: "{natural_input}"
Return ONLY the command string (no explanation).
"""

    response = model.generate_content(prompt)
    return response.text.strip()

def run_command(cmd: str):
    print(f"→ Running: {cmd}")
    result = subprocess.getoutput(cmd)
    return result
