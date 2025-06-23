from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_bio(resume_text):
    prompt = f"""Act like a professional career coach. Based on the following resume content, write a LinkedIn bio (first-person) within 250 words:

{resume_text}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
