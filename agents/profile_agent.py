import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_profile(name, context, search_results):

    prompt = f"""
You are an AI research assistant.

Using the publicly available information below, create a professional profile.

Person Name:
{name}

Context:
{context}

Search Results:
{search_results}

Generate the profile using these sections:

# Executive Summary

# Basic Details
- Full Name
- Nationality
- Current Role / Occupation
- Industry
- Current City and Country

# Biography

# Career Timeline

# Education

# Interests

# Estimated Net Worth

# Recent News or Public Activities

# References and Source Links

Rules:
- Use only publicly available information.
- Do not make up information.
- If information is unavailable, write "Not Publicly Available".
- Mention sources whenever possible.
- Format the output neatly using Markdown.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=2048
    )

    return response.choices[0].message.content