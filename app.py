import os
import streamlit as st

from downloader import download_youtube_audio
from video_downloader import download_youtube_video


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="AUDIO VIDEO DOWNLOADER",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');


    /* =====================================================
       GLOBAL
    ===================================================== */

    html,
    body,
    [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }


    /* =====================================================
       BACKGROUND
    ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(244, 114, 182, 0.18),
                transparent 30%
            ),

            radial-gradient(
                circle at 90% 20%,
                rgba(129, 140, 248, 0.20),
                transparent 30%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(56, 189, 248, 0.15),
                transparent 35%
            ),

            linear-gradient(
                135deg,
                #fff7fb,
                #f5f3ff,
                #f0f9ff
            );

        background-attachment: fixed;
    }


    /* Hide Streamlit default UI */

    #MainMenu,
    header,
    footer {
        visibility: hidden;
    }


    /* =====================================================
       TITLE
    ===================================================== */

    .app-title {
        text-align: center;

        font-size: 3rem;

        font-weight: 800;

        background:
            linear-gradient(
                90deg,
                #ec4899,
                #8b5cf6,
                #3b82f6
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        background-clip: text;

        margin-top: 1rem;

        margin-bottom: 0.5rem;

        letter-spacing: -1.5px;
    }


    /* =====================================================
       SUBTITLE
    ===================================================== */

    .app-subtitle {
        text-align: center;

        color: #64748b;

        font-size: 1.3rem;

        font-weight: 500;

        margin-bottom: 3rem;

        line-height: 1.6;
    }


    /* =====================================================
       LABELS
    ===================================================== */

    label {
        color: #6d28d9 !important;

        font-weight: 700 !important;

        font-size: 1.2rem !important;
    }


    /* =====================================================
       YOUTUBE URL INPUT
    ===================================================== */

    div[data-baseweb="input"] {
        min-height: 62px !important;

        border-radius: 16px !important;

        border: 2px solid #e9d5ff !important;

        background: rgba(255, 255, 255, 0.95) !important;

        transition:
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }


    div[data-baseweb="input"]:focus-within {
        border-color: #a78bfa !important;

        box-shadow:
            0 0 0 4px rgba(167, 139, 250, 0.15) !important;
    }


    div[data-baseweb="input"] input {
        height: 58px !important;

        color: #4c1d95 !important;

        font-size: 1.15rem !important;

        font-weight: 500 !important;

        padding-left: 18px !important;
    }


    /* =====================================================
       RADIO SECTIONS
    ===================================================== */

    div[data-testid="stRadio"] {
        margin-top: 2rem;

        margin-bottom: 1rem;

        text-align: center;
    }


    div[data-testid="stRadio"] > div {
        justify-content: center !important;
    }


    div[role="radiogroup"] {
        display: flex !important;

        justify-content: center !important;

        align-items: center !important;

        gap: 25px !important;

        padding: 12px 25px !important;

        background: rgba(255, 255, 255, 0.85);

        border: 2px solid #e9d5ff;

        border-radius: 50px;

        box-shadow:
            0 8px 25px rgba(139, 92, 246, 0.10);

        flex-wrap: wrap;
    }


    div[role="radiogroup"] label {
        display: flex !important;

        align-items: center !important;

        gap: 8px !important;

        padding: 5px 8px !important;

        margin: 0 !important;

        color: #7c3aed !important;

        font-size: 1.1rem !important;

        font-weight: 600 !important;

        white-space: nowrap !important;

        cursor: pointer;
    }


    /* =====================================================
       VIDEO QUALITY SELECTBOX
    ===================================================== */

    div[data-baseweb="select"] > div {
        min-height: 58px !important;

        border-radius: 16px !important;

        border: 2px solid #e9d5ff !important;

        background: rgba(255, 255, 255, 0.95) !important;
    }


    div[data-baseweb="select"] {
        margin-top: 0.5rem;
    }


    /* =====================================================
       DOWNLOAD BUTTON
    ===================================================== */

    div.stButton {
        display: flex;

        justify-content: center;

        margin-top: 2rem;
    }


    div.stButton > button {
        min-width: 320px;

        min-height: 60px;

        padding: 0.9rem 2.5rem;

        border: none;

        border-radius: 999px;

        background:
            linear-gradient(
                90deg,
                #f9a8d4,
                #c4b5fd,
                #93c5fd
            );

        background-size: 200% auto;

        color: #3b0764;

        font-size: 1.2rem;

        font-weight: 700;

        letter-spacing: 0.2px;

        box-shadow:
            0 8px 25px
            rgba(196, 181, 253, 0.35);

        transition: all 0.3s ease;
    }


    div.stButton > button:hover {
        background-position: right center;

        transform: translateY(-3px);

        box-shadow:
            0 12px 30px
            rgba(244, 114, 182, 0.3);

        color: #3b0764;

        border: none;
    }


    div.stButton > button:active {
        transform: translateY(0);
    }


    /* =====================================================
       SAVE BUTTON
    ===================================================== */

    div.stDownloadButton {
        display: flex;

        justify-content: center;

        margin-top: 1rem;
    }


    div.stDownloadButton > button {
        min-width: 320px;

        min-height: 60px;

        padding: 0.9rem 2.5rem;

        border: none;

        border-radius: 999px;

        background:
            linear-gradient(
                90deg,
                #86efac,
                #5eead4
            );

        color: #064e3b;

        font-size: 1.15rem;

        font-weight: 700;

        box-shadow:
            0 8px 25px
            rgba(94, 234, 212, 0.25);

        transition: all 0.3s ease;
    }


    div.stDownloadButton > button:hover {
        transform: translateY(-3px);

        box-shadow:
            0 12px 30px
            rgba(94, 234, 212, 0.35);
    }


    /* =====================================================
       ALERTS
    ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 16px;

        font-size: 1rem;

        font-weight: 500;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer-note {
        text-align: center;

        color: #94a3b8;

        font-size: 0.9rem;

        margin-top: 2rem;

        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="app-title">🎬 AUDIO VIDEO DOWNLOADER </div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="app-subtitle">'
    'Paste a link, choose audio or video, and download it ✨'
    '</div>',
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# YOUTUBE URL
# ---------------------------------------------------------

url = st.text_input(
    "🔗 YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)


# ---------------------------------------------------------
# DOWNLOAD TYPE
# ---------------------------------------------------------

download_type = st.radio(
    "📥 Select download type",
    ["🎵 Audio", "🎬 Video"],
    horizontal=True,
)


# ---------------------------------------------------------
# AUDIO OPTIONS
# ---------------------------------------------------------

if download_type == "🎵 Audio":

    audio_format = st.radio(
        "🎧 Select audio format",
        ["MP3", "WAV"],
        horizontal=True,
    )


# ---------------------------------------------------------
# VIDEO OPTIONS
# ---------------------------------------------------------

else:

    video_quality = st.selectbox(
        "🎬 Select video quality",
        [
            "Best Available",
            "1080p",
            "720p",
            "480p",
            "360p",
        ],
    )


# ---------------------------------------------------------
# DOWNLOAD
# ---------------------------------------------------------

if st.button("⬇️  Download"):

    if not url:

        st.error("⚠️ Please enter a YouTube URL.")

    else:

        try:

            # =============================================
            # AUDIO DOWNLOAD
            # =============================================

            if download_type == "🎵 Audio":

                with st.spinner(
                    "Fetching and converting your audio... 🎶"
                ):

                    file_path = download_youtube_audio(
                        url,
                        audio_format.lower()
                    )

                file_label = "📥 Save Audio"


            # =============================================
            # VIDEO DOWNLOAD
            # =============================================

            else:

                with st.spinner(
                    "Fetching and downloading your video... 🎬"
                ):

                    # Convert Best Available to "best"
                    if video_quality == "Best Available":
                        selected_quality = "best"
                    else:
                        selected_quality = video_quality

                    file_path = download_youtube_video(
                        url,
                        selected_quality
                    )

                file_label = "📥 Save Video"


            # =============================================
            # SUCCESS
            # =============================================

            st.success("✅ Download completed!")

            st.balloons()


            # =============================================
            # DOWNLOAD FILE
            # =============================================

            with open(file_path, "rb") as file:

                st.download_button(
                    label=file_label,
                    data=file,
                    file_name=os.path.basename(file_path),
                )


        except Exception as e:

            st.error(
                f"❌ Download failed: {e}"
            )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    '<div class="footer-note">'
    'Made with 💜 using Streamlit'
    '</div>',
    unsafe_allow_html=True,
)