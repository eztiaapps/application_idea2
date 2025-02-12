import requests
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_URL = "https://api.groq.com/v1/completions"

def rewrite_cv(cv_text, api_key):
    """
    Sends CV text to Groq's Llama API and returns a FAANG-optimized version.
    """
    if not cv_text.strip():
        return "Error: Empty CV content provided."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"Rewrite the following CV in a FAANG and ATS-friendly format:\n\n{cv_text}"

    data = {
        "model": "llama-3-8b",  # Update based on Groq's supported models
        "prompt": prompt,
        "max_tokens": 1000
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("text", "").strip()
    else:
        return f"Error: {response.text}"
