import streamlit as st
from transformers import pipeline

# Load the model from Hugging Face
MODEL_NAME = "H4KAI/Answer-From-Vaathiyar"  # Replace with your Hugging Face model
pipe = pipeline("text-generation", model=MODEL_NAME)

# Streamlit UI
st.title("🤖 GPT-2 Text Generator")
st.subheader("Enter a prompt and generate text!")

# User input
prompt = st.text_area("Enter your text prompt:", "Hello, AI!")

if st.button("Generate"):
    with st.spinner("Generating text..."):
        result = pipe(prompt, max_length=50)
        st.success("Generated Text:")
        st.write(result[0]["generated_text"])
