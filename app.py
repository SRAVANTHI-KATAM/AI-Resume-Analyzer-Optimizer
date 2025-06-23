import streamlit as st
from resume_utils import extract_resume_text
from jd_utils import extract_keywords, match_keywords
from linkedin_bio import generate_linkedin_bio
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume Analyzer & Optimizer", layout="wide")
st.title("📄 AI Resume Analyzer & Optimizer")

st.markdown("This tool analyzes your resume against a job description and provides ATS tips + LinkedIn bio.")

# Upload resume
resume_file = st.file_uploader("📤 Upload Your Resume (.pdf or .docx)", type=["pdf", "docx"])
# Paste JD
jd_input = st.text_area("📌 Paste the Job Description here", height=200)

if resume_file and jd_input:
    with st.spinner("🔍 Extracting and analyzing resume..."):
        resume_text = extract_resume_text(resume_file)
        keywords = extract_keywords(jd_input)
        matched_keywords, match_score = match_keywords(resume_text, keywords)

    st.subheader("✅ Keyword Match Report")
    st.write(f"**Match Score:** {match_score:.2f}%")
    st.write(f"**Matched Keywords:**")
    st.code(", ".join(matched_keywords.keys()) if matched_keywords else "None matched")

    st.write(f"**Missing Keywords:**")
    missing_keywords = list(set(keywords) - set(matched_keywords.keys()))
    st.code(", ".join(missing_keywords) if missing_keywords else "None missing")

    # ATS Suggestions
    st.subheader("🧠 ATS Optimization Suggestions")
    with st.spinner("🧠 AI is generating suggestions..."):
        ats_prompt = f"""You are a resume optimization assistant.
Analyze the following resume and suggest improvements to pass ATS filters. Provide your suggestions in bullet points.

Resume:
{resume_text}
"""
        ats_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": ats_prompt}]
        )
        suggestions = ats_response.choices[0].message.content
        st.markdown(suggestions)

    # LinkedIn Bio Generator
    st.subheader("👤 LinkedIn Bio Generator")
    if st.button("Generate LinkedIn Bio"):
        with st.spinner("✍️ Generating bio..."):
            bio = generate_linkedin_bio(resume_text)
            st.success("Here's your LinkedIn bio:")
            st.markdown(bio)

else:
    st.info("Please upload a resume and provide a job description to continue.")
