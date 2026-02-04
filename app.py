import streamlit as st
from google import genai

# --- CONFIGURATION ---
st.set_page_config(page_title="Ortho AI Jargon Buster", page_icon="🦷")

# --- API KEY SETUP (SECURE WAY) ---
# This grabs the key from Streamlit's hidden safe
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("No API key found! Please set it in Streamlit Secrets.")
    st.stop()

# --- APP VISUALS ---
st.title("🦷 Ortho AI Jargon Buster")
st.markdown("### Powered by Google Gemini 2.0")
st.write("Enter a confusing orthodontic term, and I will explain it simply.")

user_term = st.text_input("Enter term (e.g. 'Class II Malocclusion'):")

# --- APP LOGIC ---
if st.button("Explain it!"):
    if not user_term:
        st.warning("Please type a word first!")
    else:
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-1.5-flash-002",
                contents=f"You are a friendly Orthodontist. Explain '{user_term}' to a 12-year-old patient using a simple analogy. Keep it under 3 sentences."
            )

            st.success("Simple Explanation:")
            st.info(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
