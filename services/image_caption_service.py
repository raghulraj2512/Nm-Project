from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch


class ImageCaptionService:
    """Service responsible for generating captions from images using BLIP."""

    def __init__(self, model_name: str = "Salesforce/blip-image-captioning-base") -> None:
        self.model_name = model_name
        self.processor = None
        self.model = None
        self._load_model()

    def _load_model(self):
        """Load the BLIP processor and model, caching resources."""
        self.processor = BlipProcessor.from_pretrained(self.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(self.model_name)
        if torch.cuda.is_available():
            self.model.to("cuda")

    def generate_caption(self, image: Image.Image) -> str:
        """Generate a visual description for a PIL image."""
        if self.processor is None or self.model is None:
            self._load_model()

        inputs = self.processor(images=image, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        output = self.model.generate(**inputs)
        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption
