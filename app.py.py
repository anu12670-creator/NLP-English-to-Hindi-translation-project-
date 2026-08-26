import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Page configuration
st.set_page_config(
    page_title="English to Hindi Translator",
    page_icon="🌐",
    layout="centered"
)

# Hugging Face model
MODEL_NAME = "Helsinki-NLP/opus-mt-en-hi"

@st.cache_resource
def load_model():
    tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
    model = MarianMTModel.from_pretrained(MODEL_NAME)
    return tokenizer, model

tokenizer, model = load_model()

# App title
st.title("🌐 English to Hindi Translator")
st.write("Enter an English sentence and translate it into Hindi.")

# Input
text = st.text_area(
    "Enter English text:",
    placeholder="Example: What is your name?"
)

# Translate button
if st.button("Translate"):
    if text.strip():
        with st.spinner("Translating..."):
            inputs = tokenizer(
                [text],
                return_tensors="pt",
                padding=True,
                truncation=True
            )

            translated = model.generate(**inputs)
            hindi_text = tokenizer.decode(
                translated[0],
                skip_special_tokens=True
            )

        st.success("Translation")
        st.write(hindi_text)
    else:
        st.warning("Please enter some English text.")

st.markdown("---")
st.caption("Powered by Hugging Face MarianMT")
