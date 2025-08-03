import os
import certifi
import logging
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)

# Make sure Gemini uses correct cert file
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = certifi.where()




import subprocess
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_command(natural_input: str) -> str:
    prompt = f"""You are a Linux expert in terminal-based commands. Convert this natural language to a Linux terminal command. Only return the command, nothing else.
"{natural_input}"
"""

    t0 = time.time()

    response = model.generate_content(prompt, stream=True)

    command = ""
    for chunk in response:
        command += chunk.text

    t1 = time.time()
    taken_ms = (t1 - t0) * 1000
    print(f"⚡ responded in {taken_ms:.2f} ms")

    return command.strip().strip("`")


def run_command(cmd: str):
    print(f"→ Running: {cmd}")
    result = subprocess.getoutput(cmd)
    return result
