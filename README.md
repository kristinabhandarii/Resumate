
# 📄 Resumate: Automated Resume Screening System

Resumate is an AI-powered resume screening system designed to help organizations streamline the recruitment process. It automates the tedious and time-consuming task of manually going through resumes by evaluating and ranking candidates based on job-specific criteria.

---

## 🔍 Problem Statement

Recruiters often receive hundreds of resumes for a single job opening. Manually scanning each one is inefficient, error-prone, and often leads to qualified candidates being overlooked. Resumate solves this by using NLP and machine learning techniques to automate and improve the screening process.

---

## ⚙️ System Workflow

The system follows a step-by-step pipeline:

1. **Upload Resumes and Job Description**  
   - Users upload multiple resumes and a job description file.
   - Weights are assigned to features based on HR preferences.

2. **Text Extraction using Tika (Python)**  
   - Extracts raw text content from documents (PDFs, DOCX, etc.).

3. **Feature Extraction (NER)**  
   - Named Entity Recognition is performed using the `spaCy-transformers` library to extract key information such as skills, education, and experience.

4. **Data Cleaning**  
   - Cleans and normalizes extracted text by removing noise, stopwords, and irrelevant tokens.

5. **Word Embedding**  
   - Utilizes **FastText** to generate vector representations of text for semantic comparison.

6. **Cosine Similarity Calculation**  
   - Measures the similarity between resume vectors and the job description vector using cosine similarity.

7. **Score Calculation**  
   - Computes a total weighted score based on predefined feature importance.

8. **Ranking & Display**  
   - Displays the top-ranked candidates based on similarity scores.

---

## 🧠 Technologies Used

- **Python**
- **Apache Tika** – for document parsing
- **spaCy-transformers** – for advanced Named Entity Recognition
- **FastText** – for word embedding
- **Scikit-learn** – for similarity calculations
- **Django** – (if applicable, for web interface)

---
