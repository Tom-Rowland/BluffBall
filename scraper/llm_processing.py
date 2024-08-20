from dataclasses import dataclass
import dotenv
import json
import os
import requests
from scraper import webscraping

dotenv.load_dotenv()


@dataclass
class Match:
    home_side: str
    away_side: str
    home_score: int
    away_score: int
    competition: str
    discussion: list[dict]


def openai_completion(prompt: str, input: str) -> str:
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


def generate_bluffball_matches(reports: str) -> list[Match]:
    with open("scraper/prompts/process_report.md") as file:
        prompt = file.read()

    matches = []
    for report in reports:
        match = Match(
            **json.loads(
                openai_completion(prompt, report).replace("```", "").replace("json", "")
            )
        )
        matches.append(match)

    return matches
