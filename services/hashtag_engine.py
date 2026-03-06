import json
from typing import List


class HashtagEngine:
    """Generate hashtags based on content category and mood using a local dataset."""

    def __init__(self, data_path: str = "data/hashtags.json") -> None:
        self.data_path = data_path
        self.hashtags = self._load_data()

    def _load_data(self) -> dict:
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def get_hashtags(self, category: str, mood: str, limit: int = 15) -> List[str]:
        cat = self.hashtags.get(category, {})
        tags = cat.get(mood.lower(), [])
        # truncate preserving order
        return tags[:limit]
