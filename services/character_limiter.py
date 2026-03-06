from typing import Tuple


class CharacterLimiter:
    """Enforces platform-specific character limits on caption and hashtags."""

    LIMITS = {
        "twitter": 280,
        "instagram": 2200,
        "facebook": 63206,
    }

    def __init__(self, platform: str = "twitter") -> None:
        self.platform = platform.lower()

    def enforce(self, caption: str, hashtags: str) -> Tuple[str, str]:
        """Return possibly truncated caption and hashtags respecting limits.

        Caption is always preserved; hashtags trimmed first. Words not cut.
        """
        limit = self.LIMITS.get(self.platform, 280)
        total = len(caption) + (1 if hashtags else 0) + len(hashtags)
        if total <= limit:
            return caption, hashtags

        # trim hashtags word by word
        words = hashtags.split()
        trimmed = []
        curr = len(caption)
        for w in words:
            if curr + 1 + len(w) <= limit:
                trimmed.append(w)
                curr += 1 + len(w)
            else:
                break
        return caption, " ".join(trimmed)
