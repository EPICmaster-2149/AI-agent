import os
import json
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

with open("people.json", "r") as f:
    knowledge_base = json.load(f)


def query_gemini_with_document(user_query):
    prompt = f"""
You are an assistant that helps match a query to the best expert from a team.

Query: {user_query}

Team Members:
"""

    for person in knowledge_base:
        prompt += f"\nName: {person['name']}\nExpertise: {person['expertise']}\nSummary: {person['summary']}\n"

    prompt += "\nReturn the best matching person's name with a reason."

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(prompt)

    return response.text
