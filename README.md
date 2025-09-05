# 🎨 Artisan's AI Marketing Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

A generative AI-powered platform designed to empower local Indian artisans by instantly creating compelling marketing content, bridging the gap between traditional craft and the digital marketplace.

---

### **Quick Links**
* **Live Application:** `[Link to your deployed Streamlit App]`
* **Video Demo (3 mins):** `[Link to your YouTube/Vimeo video]`
* **Project Proposal:** `[Link to your detailed proposal document, if separate]`

---

## 💡 The Problem

India's local artisans are custodians of a rich cultural heritage. However, they often face significant hurdles in the modern digital economy. A lack of digital marketing skills, limited resources, and the difficulty of telling their story effectively online prevent them from reaching a wider audience, limiting their profitability and threatening the sustainability of their craft.

## ✨ Our Solution

**Artisan's AI Marketing Assistant** acts as a personal marketing expert for every artisan. By leveraging Google's Gemini Pro AI, our application analyzes a photo of their craft and instantly generates a complete digital marketing kit, including:

* **Product Titles:** Catchy and optimized for online searches.
* **Product Descriptions:** Warm, story-driven text that highlights the product's heritage and value.
* **Social Media Posts:** Engaging captions with relevant hashtags, ready for platforms like Instagram.

This tool automates the difficult task of content creation, allowing artisans to focus on what they do best: creating beautiful art.

---

## 🛠️ Tech Stack & Architecture

* **Frontend:** Streamlit
* **Backend & Logic:** Python
* **Generative AI:** Google Gemini 1.5 Pro API
* **Deployment:** Streamlit Community Cloud

**Workflow:**
`User Upload (Image + Text) -> Streamlit UI -> Python Backend -> Gemini API Call -> JSON Response -> Display Formatted Content`

---

## ⚙️ Setup & Local Installation

To run this project on your local machine, please follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone [Link to your GitHub repository]
    cd artisan-ai-app
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate on Windows
    .\.venv\Scripts\activate

    # Activate on macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    * Create a new file named `.env` in the root of the project folder.
    * Add your Google Gemini API key to the file like this:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

5.  **Run the Streamlit App**
    ```bash
    streamlit run app.py
    ```

---

## 👤 Creator

* **Himasri**