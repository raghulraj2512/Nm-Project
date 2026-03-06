from typing import Tuple


class TextUtils:
    """General text helper methods."""

    @staticmethod
    def smart_truncate(text: str, limit: int) -> str:
        if len(text) <= limit:
            return text
        words = text.split()
        truncated = ""
        for w in words:
            if len(truncated) + len(w) + (1 if truncated else 0) > limit:
                break
            truncated = f"{truncated} {w}" if truncated else w
        return truncated
