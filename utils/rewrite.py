import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

#API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}


def rewrite_caption(base_caption: str, platform: str, tone: str) -> str:
    prompt = (
        f"Rewrite the following image description into a short, stylish, and {tone.lower()} caption for {platform}:\n\n"
        f"'{base_caption}'\n\n"
        f"Only return the final caption. Do not include extra instructions, markdown, or explanations.\n\n"
        f"Caption:"
    )

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 150, "temperature": 0.8}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list):
            full_output = result[0]["generated_text"]

          
            if "Caption:" in full_output:
                cleaned = full_output.split("Caption:")[-1].strip()
            else:
                cleaned = full_output.strip()

            
            for end_char in ["\n", "Instrucción", "**", "```", "Now", "Diseña", "Plan", "markdown", "Instagram"]:
                if end_char in cleaned:
                    cleaned = cleaned.split(end_char)[0].strip()

          
            return cleaned.strip(' "\'')

        return "Unexpected response format from HF API."
    except Exception as e:
        return f"Hugging Face API error: {str(e)}"



    
   
"""
    base_caption = base_caption.strip().capitalize()  

    if tone == "Funny":
        tone_prefix = "😂 Here's a funny take: "
    elif tone == "Romantic":
        tone_prefix = "❤️ Feeling the love: "
    elif tone == "Deep":
        tone_prefix = "💭 Deep thoughts: "
    elif tone == "Savage":
        tone_prefix = "💀 Ruthless vibes: "
    else:
        tone_prefix = ""

   
    if platform == "Instagram":
        platform_suffix = " "
    elif platform == "Twitter":
        platform_suffix = " "
    elif platform == "WhatsApp":
        platform_suffix = " "
    else:
        platform_suffix = ""

    
    return f"{base_caption}"
"""