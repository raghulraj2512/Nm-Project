import os
import requests


class GeminiService:
    """Optional integration with Google Gemini API for caption enhancement."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.endpoint = "https://api.gemini.google.com/v1/generate"  # placeholder

    def enhance_caption(self, prompt: str) -> str:
        """Send prompt to Gemini and return enhanced text if available."""
        if not self.api_key:
            return prompt
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"input": prompt}
        try:
            resp = requests.post(self.endpoint, json=data, headers=headers, timeout=5)
            resp.raise_for_status()
            result = resp.json()
            return result.get("output", prompt)
        except Exception:
            return prompt
