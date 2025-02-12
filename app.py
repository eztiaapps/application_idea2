import streamlit as st
import docx2txt
import requests
import os
from utils import rewrite_cv

groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure API key is set in environment variables
GROQ_API_URL = "https://api.groq.com/v1/completions"  # Update if needed

def main():
    st.set_page_config(page_title="CV Rewriter - FAANG & ATS Optimized")
    st.title("📄 CV Rewriter for FAANG & ATS")
    st.write("Upload your CV in Word format, and get an optimized version instantly!")
    
    uploaded_file = st.file_uploader("Upload your CV (.docx)", type=["docx"])
    
    if uploaded_file is not None:
        with st.spinner("Processing your CV..."):
            extracted_text = docx2txt.process(uploaded_file)
            optimized_cv = rewrite_cv(extracted_text, groq_api_key)
            
            if not optimized_cv:
                st.error("Failed to process CV. Please try again.")
                return
            
            st.subheader("🔹 Optimized CV Preview")
            st.text_area("", optimized_cv, height=400)
            
            st.download_button("Download Optimized CV", optimized_cv, file_name="optimized_cv.txt")
            
if __name__ == "__main__":
    main()
