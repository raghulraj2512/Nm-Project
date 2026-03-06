# Social Mood Matcher

## Project Overview

Social Mood Matcher is a production-ready Streamlit application that helps users generate engaging social media captions and hashtags from images. It leverages state-of-the-art transformer models for image captioning and sentiment analysis, coupled with a rule-based system for caption styling and hashtag suggestions. The app applies platform-specific character limits and supports optional enhancement via the Google Gemini API.

## Architecture

```
social-mood-matcher/
│
├── app.py                 # Streamlit entrypoint
├── requirements.txt       # Python dependencies
├── services/              # Core ML and business logic
│   ├── image_caption_service.py
│   ├── sentiment_service.py
│   ├── caption_generator.py
│   ├── hashtag_engine.py
│   ├── character_limiter.py
│   └── gemini_service.py  # optional
├── utils/                 # Helper utilities
│   ├── image_utils.py
│   └── text_utils.py
├── data/
│   └── hashtags.json
└── README.md
```

### Key Components

- **ImageCaptionService** – Generates textual descriptions from uploaded images using BLIP.
- **SentimentService** – Detects mood categories using a DistilBERT sentiment model.
- **CaptionGenerator** – Produces styled caption variants based on description and mood.
- **HashtagEngine** – Suggests mood/category-specific trending hashtags.
- **CharacterLimiter** – Enforces platform length restrictions and truncates intelligently.
- **GeminiService** – Optional text enhancement via Google Gemini API.

## Setup Instructions

1. Clone the repository and navigate into the project directory:
   ```bash
   git clone <repo-url>
   cd social-mood-matcher
   ```
2. Create and activate a Python 3.10 virtual environment:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # on Windows use `venv\\Scripts\\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Create a `.env` file in the project root to hold environment variables:
   ```bash
   echo "GEMINI_API_KEY=your_key" > .env
   ```
   The app reads `GEMINI_API_KEY` from the environment automatically. Use
   [`python-dotenv`](https://pypi.org/project/python-dotenv/) if you want to
   load `.env` automatically (not included in requirements by default).

## Running the App

There are two simple ways to start the application:

- Use Streamlit directly:
  ```bash
  streamlit run app.py
  ```

- Or use the helper script (Unix-like systems):
  ```bash
  ./run.sh
  ```

The web UI should open automatically in your default browser. If it does not,
visit `http://localhost:8501`.


## Running the App

Execute the Streamlit application:

```bash
streamlit run app.py
```

The UI will open in your browser; upload an image and configure options via the sidebar.

## Screenshots

<!-- Add screenshots of the UI here -->

## Future Enhancements

- Add caching for generated captions and hashtags.
- Improve mood mapping using a custom classifier.
- Integrate with additional social platforms (LinkedIn, TikTok).
- Support bulk image uploads.
- Add multilingual caption support.

---

Feel free to customize and extend the project to fit your needs.