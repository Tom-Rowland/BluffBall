from scraper.data_classes import Match
import dotenv
import json
import os
import requests

dotenv.load_dotenv()


def openai_completion(prompt, input: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY"),
    }

    body = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": input},
        ],
        "temperature": 0.5,
    }
    data = json.dumps(body)

    response = requests.post(url, headers=headers, data=data).json()
    output = response["choices"][0]["message"]["content"]

    return output
