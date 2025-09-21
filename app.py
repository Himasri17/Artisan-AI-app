# app.py (Final Version with bug fix)

import streamlit as st
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from PIL import Image

# --- CONFIGURATION ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except AttributeError:
    st.error("Google API Key not found. Please make sure it's set in your .env file or Streamlit secrets.")
    st.stop()


# --- CORE AI FUNCTION ---
def get_gemini_response(image, craft_name, artist_name):
    #model = genai.GenerativeModel('gemini-1.5-pro-latest')
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"""
    You are an expert e-commerce and social media marketer specializing in helping Indian artisans.
    Your tone should be warm, evocative, and respectful of the craft's heritage.
    An artisan has provided an image of their product and some basic details.
    The product is a '{craft_name}' by '{artist_name}'.

    Based on the provided image and details, generate the following marketing content:
    1.  **title**: A catchy and descriptive product title that is SEO-friendly.
    2.  **description**: A warm, story-driven product description of about 100-150 words. It should highlight the craftsmanship, cultural heritage, the materials used, and what makes the product special.
    3.  **social_post**: An engaging Instagram post caption. It should start with a hook, tell a mini-story about the piece, describe it, and end with a call to action. Include 5-7 relevant and popular hashtags like #handmadeinindia, #indianartisan, #supportlocalartisans, etc.

    Your output must be ONLY a valid JSON object with these exact keys: "title", "description", "social_post".
    Do not include the word "json" or the backticks ``` in your response.
    """
    response = model.generate_content([prompt, image])
    return response.text


# --- STREAMLIT APP INTERFACE ---
st.set_page_config(page_title="Artisan's AI Assistant", page_icon="🎨", layout="wide")
st.title("🎨 Artisan's AI Marketing Assistant")
st.write("Upload a photo of your craft, add a few details, and let our AI create your marketing content instantly!")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Your Craft Details")
    uploaded_file = st.file_uploader("1. Upload a photo of your craft", type=["png", "jpg", "jpeg"])
    craft_name = st.text_input("2. What is the name of your craft?", placeholder="e.g., 'Jaipuri Blue Pottery Vase'")
    artist_name = st.text_input("3. What is your name or your brand's name?", placeholder="e.g., 'Kala Emporium'")
    submit_button = st.button("✨ Generate My Marketing Kit", type="primary")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Your Uploaded Craft", use_container_width=True)

with col2:
    st.subheader("Your AI-Generated Content")
    if submit_button:
        if uploaded_file and craft_name and artist_name:
            with st.spinner("Our AI is crafting your story... Please wait a moment."):
                response_text = "" # Initialize the variable here to prevent NameError
                try:
                    image = Image.open(uploaded_file)
                    response_text = get_gemini_response(image, craft_name, artist_name)
                    clean_response_text = response_text.strip().replace("```json", "").replace("```", "")
                    results = json.loads(clean_response_text)
                    
                    st.write("#### **Generated Product Title:**")
                    st.success(results['title'])
                    st.write("#### **Generated Product Description:**")
                    st.info(results['description'])
                    st.write("#### **Generated Instagram Post Caption:**")
                    st.info(results['social_post'])

                except Exception as e:
                    st.error("An error occurred. This might be due to API rate limits or an unexpected response from the AI.")
                    st.error(f"Error Details: {e}")
                    st.warning("Raw AI Response (for debugging):")
                    st.code(response_text)
        else:
            st.warning("Please upload an image and fill out all the details before generating.")
    else:
        st.info("Please fill out the details on the left and click 'Generate' to see your marketing content here.")
