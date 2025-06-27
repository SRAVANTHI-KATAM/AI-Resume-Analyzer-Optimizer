#  AI Resume Analyzer & Optimizer

An intelligent Streamlit-powered web application that analyzes your resume against any job description and provides personalized, AI-generated improvements — including ATS optimization tips and a ready-to-use LinkedIn bio.

---

##  About This Project

**AI Resume Analyzer & Optimizer** is a smart web application designed to help job seekers enhance their resumes using the power of artificial intelligence. Built with **Python**, **Streamlit**, and **OpenAI's GPT model**, this tool analyzes a user's resume against a specific job description (JD) to provide actionable, personalized feedback.

The application goes beyond simple keyword matching. It applies natural language processing (NLP) to understand context, evaluate alignment with the job description, and generate **ATS-friendly** optimization suggestions. Users receive a **match score** and a detailed breakdown of matched and missing keywords relevant to the role.

It also features a **LinkedIn bio generator**, which uses GPT to craft a compelling, personalized summary in the first person — ideal for updating your LinkedIn profile or professional bio.

###  Why This Project Matters

- ⏱ Saves hours of manual tweaking by automating resume optimization  
- 🎯 Increases chances of interview calls through smart keyword alignment  
- 🤖 Uses GPT-3.5 to generate contextual, role-specific feedback  
- 👩‍💻 Ideal for students, job seekers, and career development professionals  

---

##  Features

✅ Upload your resume (`.pdf` or `.docx`)  
✅ Paste any job description (JD)  
✅ AI-based resume vs JD keyword matching  
✅ ATS (Applicant Tracking System) readability & structure suggestions  
✅ Match Score and keyword coverage report  
✅ AI-generated LinkedIn bio tailored to your resume  
✅ Built with OpenAI's GPT model and modern NLP libraries  

---

##  Preview

> *(Insert your screenshot here)*  
> Example:  
> ![App Screenshot](https://your-screenshot-url-or-local-file.png)

---

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: OpenAI GPT (`gpt-3.5-turbo`)
- **NLP Libraries**: SpaCy, FuzzyWuzzy
- **File Parsing**: PyPDF2, python-docx
- **Environment Management**: python-dotenv

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-resume-optimizer.git
cd ai-resume-optimizer
