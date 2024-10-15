import streamlit as st
import instaloader

# Set up Instaloader instance
loader = instaloader.Instaloader()

# App title
st.title("Instagram Reels Downloader")

# URL input
url = st.text_input("Enter the Instagram Reel URL")

# Button to download Reel
if st.button("Download Reel"):
    try:
        # Load post
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        # Download the reel
        with st.spinner("Downloading..."):
            loader.download_post(post, target="reels_downloaded")
        
        st.success("Download completed!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
