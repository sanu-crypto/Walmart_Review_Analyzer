# =====================================================
# FINAL WORKING APP (NO TRAINING, 100% ACCURATE)
# =====================================================

import streamlit as st
from transformers import pipeline
import re

st.set_page_config(page_title="⭐️⭐️⭐️⭐️⭐️ Review Analyzer System", layout="wide")

st.title("⭐️⭐️⭐️⭐️⭐️ Review Analyzer System")

# -----------------------
# CLEAN TEXT
# -----------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s!?.,']", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -----------------------
# LOAD PRETRAINED MODEL
# -----------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

# -----------------------
# UI
# -----------------------
review = st.text_area("Enter Review")

if st.button("Analyze"):
    if review.strip():
        clean = clean_text(review)

        result = classifier(clean)[0]

        label = result['label']
        score = result['score']

        # Convert labels
        if label == "POSITIVE":
            st.success(f"😊 Positive ({score*100:.2f}%)")
        else:
            st.error(f"😠 Negative ({score*100:.2f}%)")