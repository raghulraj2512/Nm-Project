from PIL import Image


class ImageUtils:
    """Utility helpers for image processing."""

    @staticmethod
    def load_image(file) -> Image.Image:
        try:
            return Image.open(file).convert("RGB")
        except Exception:
            raise
