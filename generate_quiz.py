import requests
import json
import re
from database import insert_question, clear_questions

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_questions(topic):

    clear_questions()

    prompt = f"""
Generate 5 multiple choice questions about {topic}.

Return ONLY JSON array.

Example format:

[
{{"question":"...", "A":"...", "B":"...", "C":"...", "D":"...", "answer":"A"}},
{{"question":"...", "A":"...", "B":"...", "C":"...", "D":"...", "answer":"B"}}
]
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    print("AI RESPONSE:")
    print(result)

    try:

        # Extract JSON block
        start = result.find("[")
        end = result.rfind("]") + 1
        json_text = result[start:end]

        # Fix missing commas between objects
        json_text = re.sub(r"}\s*{", "},{", json_text)

        questions = json.loads(json_text)

        for q in questions:

            insert_question(
                q["question"],
                q["A"],
                q["B"],
                q["C"],
                q["D"],
                q["answer"]
            )

        print("Questions inserted successfully")

    except Exception as e:
        print("Error parsing AI response:", e)