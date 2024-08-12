import streamlit as st
from instaloader import Instaloader, Post
import base64
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load and encode the background image
image_path = "bg.png"
with open(image_path, "rb") as img_file:
    bg_image = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{bg_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .stTitle {{
        color: #4169e1;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }}
    .stMarkdown, .stText {{
        color: #4169e1;
    }}
    .stButton {{
        color: #4169e1;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="stTitle">Welcome to the IG Pollar</h1>', unsafe_allow_html=True)

url = st.text_input("🔗 Paste the Instagram Reel URL here:")

if st.button("Download Reel"):
    if url:
        loader = Instaloader()

        max_retries = 5
        delay = 60  # Initial delay in seconds

        for attempt in range(max_retries):
            try:
                logger.info(f"Attempt {attempt + 1}: Processing URL {url}")
                post = Post.from_shortcode(loader.context, url.split("/")[-2])
                loader.download_post(post, target="downloaded_reel")
                st.success("Downloaded Successfully.")
                logger.info("Download successful.")
                break
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    st.warning(f"Retrying in {delay} seconds... Attempt {attempt + 1}")
                    time.sleep(delay)
                    delay *= 2
                else:
                    st.error(f"Oops! Something went wrong: {e}")
                    logger.error(f"Failed after {max_retries} attempts.")
    else:
        st.warning("Please enter a valid Instagram Reel URL above.")

st.markdown("""
    ---
    **Feedback?** 
    We would love to hear your thoughts! Please share your feedback or suggestions below.
""")
feedback = st.text_area("Your Feedback", "")
if st.button("Submit Feedback"):
    if feedback:
        st.success("Thank you for your feedback!")
    else:
        st.warning("Please provide feedback; it will help us improve this project.")
st.write("Email: wajahatdslearning@gmail.com")
