import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def analyze_requirement(requirement: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai/docs",
        "X-Title": "business-to-tech-streamlit"
    }

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are an expert software architect.

Given the business requirement: "{requirement}", break it down into:
1. Functional modules (clear list)
2. Database schema (tables and fields)
3. Pseudocode for main functions (use Python-style pseudocode)
Structure your output neatly.
"""
            }
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        return f"❌ Request error: {http_err}\n\nDetails: {response.text}"
    except Exception as e:
        return f"❌ General error: {e}"
