from typing import List


class CaptionGenerator:
    """Generates caption variants based on image description, mood, and style."""

    STYLES = ["casual", "aesthetic", "professional", "playful"]

    TEMPLATES = {
        "casual": "{desc} {emoji}",
        "aesthetic": "{desc} ✨",
        "professional": "{desc}",
        "playful": "{desc} 😂",
    }

    EMOJIS = {
        "casual": "🙂",
        "aesthetic": "🎨",
        "professional": "",
        "playful": "😜",
    }

    def __init__(self):
        pass

    def generate(self, description: str, mood: str, style: str) -> str:
        """Return a caption based on the given inputs."""
        style = style if style in self.STYLES else "casual"
        template = self.TEMPLATES.get(style, "{desc}")
        emoji = self.EMOJIS.get(style, "")
        caption = template.format(desc=description, emoji=emoji)
        return caption

    def generate_variants(self, description: str, mood: str) -> List[str]:
        """Return all style variants for a given description and mood."""
        variants = []
        for style in self.STYLES:
            variants.append(self.generate(description, mood, style))
        return variants
