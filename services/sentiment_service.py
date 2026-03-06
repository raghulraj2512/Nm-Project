from transformers import pipeline


class SentimentService:
    """Service to detect mood or sentiment from text."""

    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english") -> None:
        self.model_name = model_name
        self.classifier = None
        self._load_model()

    def _load_model(self) -> None:
        self.classifier = pipeline("sentiment-analysis", model=self.model_name)

    def detect_mood(self, text: str) -> str:
        """Detect mood and map to predefined categories."""
        if self.classifier is None:
            self._load_model()
        result = self.classifier(text[:512])[0]
        label = result["label"].lower()
        # simple mapping, may expand
        if "positive" in label:
            return "Cozy"
        elif "negative" in label:
            return "Playful"
        else:
            return "Professional"
