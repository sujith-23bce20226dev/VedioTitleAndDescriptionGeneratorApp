import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
    return tokenizer, model

tokenizer, model = load_model()

st.title("Video Title & Description Generator")

# User input
video_topic = st.text_area("Enter your video topic, idea, or keywords:")

if st.button("Generate Titles & Descriptions"):
    if not video_topic.strip():
        st.error("❌ Please enter a video topic before generating.")
    else:
        with st.spinner("Generating content..."):

            # Title generation prompt
            title_prompt = f"Generate 5 creative YouTube video titles for the following topic:\n{video_topic}\n\nTitles:"
            title_inputs = tokenizer(title_prompt, return_tensors="pt", max_length=512, truncation=True)
            title_outputs = model.generate(
                **title_inputs,
                max_length=40,
                num_return_sequences=5,
                do_sample=True,
                temperature=0.9,
                top_p=0.95
            )
            generated_titles = [tokenizer.decode(output, skip_special_tokens=True) for output in title_outputs]

            # Description generation prompt
            desc_prompt = f"Write a YouTube video description in a 3-5 line paragraph for the following topic:\n{video_topic}"
            desc_inputs = tokenizer(desc_prompt, return_tensors="pt", max_length=512, truncation=True)
            desc_outputs = model.generate(
                **desc_inputs,
                max_length=200,
                min_length=100,          
                num_return_sequences=1,
                do_sample=True,
                temperature=0.85,
                top_p=0.9,
                early_stopping=True
            )
            generated_desc = tokenizer.decode(desc_outputs[0], skip_special_tokens=True)

        st.success("✅ Content generated!")

        # Display Titles
        st.markdown("### Video Titles:")
        for i, title in enumerate(generated_titles, 1):
            st.write(f"{i}. {title}")

        # Display Description
        st.markdown("### Video Description:")
        st.write(generated_desc)
