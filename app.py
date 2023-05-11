import streamlit as st
st.title("Text to Summary to Image")
st.header("This is a sample web app that summarizes text and generates an image of the summary")
text = st.text_area("Enter your text below","Astronaut riding a bicycle in the beach")
if st.button("Summarize and Generate Image"):
    if not text