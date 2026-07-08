import requests
from .config import OLLAMA_URL, MODEL_NAME


class LLMClient:

    def ask(self, prompt: str):

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        response.raise_for_status()

        return response.json()["response"]