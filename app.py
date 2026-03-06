import streamlit as st
from PIL import Image
import io
from services.image_caption_service import ImageCaptionService
from services.sentiment_service import SentimentService
from services.caption_generator import CaptionGenerator
from services.hashtag_engine import HashtagEngine
from services.character_limiter import CharacterLimiter


def add_custom_css():
    """Add modern glowing CSS styles"""
    st.markdown("""
    <style>
    /* Modern Dark Theme */
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }

    /* Glowing Title */
    .title-glow {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #ffeaa7);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 3s ease infinite;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #b8c5d6;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.8;
    }

    /* Glowing Cards */
    .glow-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        box-shadow:
            0 8px 32px rgba(0, 0, 0, 0.3),
            0 0 20px rgba(78, 205, 196, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }

    .glow-card:hover {
        box-shadow:
            0 12px 40px rgba(0, 0, 0, 0.4),
            0 0 30px rgba(78, 205, 196, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }

    /* Upload Area */
    .upload-zone {
        border: 2px dashed rgba(78, 205, 196, 0.5);
        border-radius: 15px;
        padding: 3rem;
        text-align: center;
        background: rgba(78, 205, 196, 0.05);
        transition: all 0.3s ease;
        margin: 1rem 0;
    }

    .upload-zone:hover {
        border-color: #4ecdc4;
        background: rgba(78, 205, 196, 0.1);
        box-shadow: 0 0 20px rgba(78, 205, 196, 0.3);
    }

    /* Glowing Button */
    .glow-button {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        border: none;
        border-radius: 50px;
        padding: 15px 30px;
        font-size: 1.1rem;
        font-weight: 600;
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .glow-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.6);
        background: linear-gradient(45deg, #ff5252, #26d0ce);
    }

    /* Progress Bar */
    .progress-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
        overflow: hidden;
    }

    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        border-radius: 10px;
        transition: width 0.5s ease;
        box-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }

    /* Result Cards */
    .result-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }

    .result-title {
        color: #4ecdc4;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: rgba(15, 15, 35, 0.95);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Text Areas */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        font-family: 'Courier New', monospace !important;
    }

    .stTextArea textarea:focus {
        border-color: #4ecdc4 !important;
        box-shadow: 0 0 10px rgba(78, 205, 196, 0.3) !important;
    }

    /* Select Boxes */
    .stSelectbox div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
    }

    .stSelectbox div[data-baseweb="select"]:hover {
        border-color: #4ecdc4 !important;
        box-shadow: 0 0 10px rgba(78, 205, 196, 0.2) !important;
    }

    /* Slider */
    .stSlider div[data-testid="stThumbValue"] {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
        box-shadow: 0 0 10px rgba(255, 107, 107, 0.5) !important;
    }

    /* Success Messages */
    .stSuccess {
        background: rgba(46, 204, 113, 0.1) !important;
        border: 1px solid rgba(46, 204, 113, 0.3) !important;
        border-radius: 10px !important;
        color: #2ecc71 !important;
    }

    /* Info Messages */
    .stInfo {
        background: rgba(52, 152, 219, 0.1) !important;
        border: 1px solid rgba(52, 152, 219, 0.3) !important;
        border-radius: 10px !important;
        color: #3498db !important;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #ff5252, #26d0ce);
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="✨ Social Mood Matcher",
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    add_custom_css()

    # Hero Section
    st.markdown('<h1 class="title-glow">✨ Social Mood Matcher</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform your images into captivating social media content with AI-powered magic</p>', unsafe_allow_html=True)

    # Sidebar Configuration
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #4ecdc4; text-shadow: 0 0 15px rgba(78, 205, 196, 0.5);">⚙️ Settings</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        platform = st.selectbox(
            "🎯 Target Platform",
            ["twitter", "instagram", "facebook"],
            help="Choose your social media platform for optimized content"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        caption_style = st.selectbox(
            "🎨 Caption Style",
            ["casual", "aesthetic", "professional", "playful"],
            help="Select the tone for your caption"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        num_hashtags = st.slider(
            "🔥 Hashtag Count",
            min_value=5,
            max_value=30,
            value=15,
            help="Number of hashtags to generate"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Main Content Layout
    col1, col2 = st.columns([1, 1], gap="large")

    # Left Column - Upload & Process
    with col1:
        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #4ecdc4; text-align: center; margin-bottom: 1rem;">📸 Upload Your Image</h3>', unsafe_allow_html=True)

        # Upload Zone
        st.markdown('<div class="upload-zone">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Drop your image here or click to browse",
            type=["jpg", "jpeg", "png", "gif", "bmp"],
            label_visibility="collapsed"
        )

        if uploaded_file is not None:
            # Display uploaded image with glow effect
            st.markdown('<div style="text-align: center; margin: 1rem 0;">', unsafe_allow_html=True)
            image = Image.open(uploaded_file)
            st.image(
                image,
                caption="✨ Your Image",
                use_column_width=True,
                output_format="PNG"
            )
            st.markdown('</div>', unsafe_allow_html=True)

            # Generate Button
            st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
            if st.button("🚀 Generate Magic Content", key="generate_btn", help="Click to transform your image into social media gold"):
                with st.spinner("✨ AI is working its magic..."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()

                    try:
                        # Step 1: Image Caption
                        status_text.text("🎨 Analyzing your image...")
                        progress_bar.progress(20)
                        caption_service = ImageCaptionService()
                        caption = caption_service.generate_caption(image)

                        # Step 2: Sentiment Analysis
                        status_text.text("😊 Detecting mood and vibe...")
                        progress_bar.progress(40)
                        sentiment_service = SentimentService()
                        mood = sentiment_service.detect_mood(caption)

                        # Step 3: Caption Variants
                        status_text.text("✍️ Crafting caption variants...")
                        progress_bar.progress(60)
                        caption_gen = CaptionGenerator()
                        variants = caption_gen.generate_variants(caption, mood)

                        # Step 4: Hashtags
                        status_text.text("🔥 Finding perfect hashtags...")
                        progress_bar.progress(80)
                        hashtag_engine = HashtagEngine()
                        hashtags = hashtag_engine.get_hashtags("general", mood, limit=num_hashtags)

                        # Step 5: Platform Optimization
                        status_text.text("📱 Optimizing for your platform...")
                        progress_bar.progress(100)
                        hashtags_str = " ".join(hashtags)
                        limiter = CharacterLimiter(platform)
                        final_caption, final_hashtags = limiter.enforce(caption, hashtags_str)

                        # Store results
                        st.session_state.caption = caption
                        st.session_state.mood = mood
                        st.session_state.variants = variants
                        st.session_state.hashtags = hashtags
                        st.session_state.final_caption = final_caption
                        st.session_state.final_hashtags = final_hashtags

                        status_text.empty()
                        progress_bar.empty()
                        st.success("🎉 Your content is ready! Check the results on the right! ✨")

                    except Exception as e:
                        st.error(f"❌ Oops! Something went wrong: {str(e)}")
                        progress_bar.empty()
                        status_text.empty()
        else:
            st.markdown('<p style="color: #b8c5d6; font-size: 1.1rem;">Choose an image to get started with AI-powered content creation</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # End upload zone
        st.markdown('</div>', unsafe_allow_html=True)  # End glow card

    # Right Column - Results
    with col2:
        st.markdown('<div class="glow-card">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #4ecdc4; text-align: center; margin-bottom: 1rem;">🎯 Your Results</h3>', unsafe_allow_html=True)

        if "caption" in st.session_state:
            # Original Caption
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">📝 AI Caption</div>', unsafe_allow_html=True)
            st.text_area(
                "Original Caption",
                st.session_state.caption,
                disabled=True,
                height=80,
                label_visibility="collapsed"
            )
            st.markdown('</div>', unsafe_allow_html=True)

            # Mood Detection
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">😊 Detected Mood</div>', unsafe_allow_html=True)
            mood_emoji = {
                "Cozy": "🏠",
                "Playful": "🎉",
                "Professional": "💼"
            }.get(st.session_state.mood, "🎨")
            st.markdown(f'<h4 style="color: #ffeaa7; text-align: center;">{mood_emoji} {st.session_state.mood}</h4>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Caption Variants
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">✨ Caption Styles</div>', unsafe_allow_html=True)
            for i, variant in enumerate(st.session_state.variants, 1):
                style_name = ["Casual", "Aesthetic", "Professional", "Playful"][i-1]
                st.markdown(f"**{style_name}:** {variant}")
            st.markdown('</div>', unsafe_allow_html=True)

            # Hashtags
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">🔥 Hashtags ({})</div>'.format(len(st.session_state.hashtags)), unsafe_allow_html=True)
            st.text_area(
                "Suggested Hashtags",
                " ".join(st.session_state.hashtags),
                disabled=True,
                height=100,
                label_visibility="collapsed"
            )
            st.markdown('</div>', unsafe_allow_html=True)

            # Platform Optimized
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown('<div class="result-title">📱 Ready for {}</div>'.format(platform.title()), unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown('<div style="margin-bottom: 0.5rem; color: #4ecdc4;">📝 Final Caption</div>', unsafe_allow_html=True)
                st.text_area(
                    "Final Caption",
                    st.session_state.final_caption,
                    disabled=True,
                    height=100,
                    label_visibility="collapsed",
                    key="final_caption_display"
                )
            with col_b:
                st.markdown('<div style="margin-bottom: 0.5rem; color: #4ecdc4;">#️⃣ Final Hashtags</div>', unsafe_allow_html=True)
                st.text_area(
                    "Final Hashtags",
                    st.session_state.final_hashtags,
                    disabled=True,
                    height=100,
                    label_visibility="collapsed",
                    key="final_hashtags_display"
                )

            # Character Counter
            total_chars = len(st.session_state.final_caption) + len(st.session_state.final_hashtags) + 1
            limit = CharacterLimiter(platform).LIMITS.get(platform, 280)
            percentage = min(total_chars / limit, 1.0)

            st.markdown('<div style="margin-top: 1rem;">', unsafe_allow_html=True)
            st.markdown('<div class="progress-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="progress-bar" style="width: {percentage*100}%"></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.caption(f"📊 Characters: {total_chars}/{limit} ({percentage*100:.1f}%)")
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="text-align: center; padding: 3rem; color: #b8c5d6;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎨</div>
                <h4>Ready to Create Magic!</h4>
                <p>Upload an image on the left and watch AI transform it into engaging social media content</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # End glow card

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; color: #666;">
        <p>✨ Powered by AI • Built with ❤️ • Made for creators</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
