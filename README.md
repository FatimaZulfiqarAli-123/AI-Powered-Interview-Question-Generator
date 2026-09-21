# AI-Powered Interview Question Generator

An AI-powered interview question generation system that creates **personalized technical and behavioral interview questions** based on a candidate's resume, a job description, and a predefined question bank.

The system processes the candidate's profile and job requirements, uses an AI model to generate relevant interview questions, and saves the generated questions into a report.

---

## 🚀 Features

* 📄 Reads candidate resumes from PDF/document files
* 💼 Processes job descriptions
* 📚 Uses a predefined interview question bank
* 🤖 AI-powered question generation
* 🎯 Generates questions based on the candidate's profile and job requirements
* 🧠 Supports technical and behavioral questions
* 📊 Configurable number of questions
* 🎚️ Supports difficulty levels
* 📝 Automatically generates and saves an interview report
* 🗂️ Organized modular project structure

---

## 🏗️ Project Pipeline

```text
Candidate Resume
       │
       ▼
Document Loader
       │
       ▼
Text Cleaning
       │
       ├───────────────┐
       │               │
       ▼               ▼
Job Description   Question Bank
       │               │
       └───────┬───────┘
               │
               ▼
        AI Interview Model
               │
               ▼
      Question Generator
               │
               ▼
 Technical + Behavioral Questions
               │
               ▼
        Report Generator
               │
               ▼
    generated_questions.txt
```

---

## 🧩 Main Components

### 📄 Document Loader

The `document_loader.py` module is responsible for:

* Reading input files
* Extracting text
* Cleaning extracted content

```python
from src.document_loader import read_file, clean_text
```

---

### 🤖 Interview Model

The `model.py` module contains the AI model used by the application to generate interview questions.

```python
from src.model import InterviewModel

ai_model = InterviewModel()
```

---

### 📝 Question Generator

The `question_generator.py` module combines:

* Candidate information
* Job description
* Question bank
* Desired question count
* Difficulty level

```python
generator = QuestionGenerator(ai_model)
```

Questions are generated using:

```python
result = generator.generate(
    intern_profile=intern_profile,
    job_description=job_description,
    question_bank=question_bank,
    technical_count=5,
    behavioral_count=5,
    difficulty="Medium"
)
```

---

### 📊 Report Generator

The `report_generator.py` module creates and saves the generated interview questions.

```python
report = create_report(
    candidate_name="Fatima",
    result=result
)

save_report(
    report,
    "outputs/generated_questions.txt"
)
```

---

## ⚙️ Input Data

The application uses three main inputs.

### 1. Candidate Resume

```text
data/resumes/Fatima_CV_001.pdf
```

The resume provides information about the candidate's:

* Education
* Skills
* Projects
* Experience
* Technical background

### 2. Job Description

```text
data/job_descriptions/ml_intern_job.pdf
```

The job description provides the requirements and responsibilities associated with the target position.

### 3. Question Bank

```text
data/question_bank/questions.txt
```

The question bank provides a collection of interview questions that can help guide the generation process.

---

## 🎯 Question Generation

The current configuration generates:

| Question Type | Number |
| ------------- | -----: |
| Technical     |      5 |
| Behavioral    |      5 |
| Difficulty    | Medium |
| Total         |     10 |

The configuration can easily be changed:

```python
technical_count=5
behavioral_count=5
difficulty="Medium"
```

For example:

```python
technical_count=10
behavioral_count=5
difficulty="Hard"
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 🤖 Artificial Intelligence / Machine Learning
* 📄 PDF/Text Document Processing
* 🧠 AI-based Question Generation
* 📊 Automated Report Generation

---

## 🔄 How It Works

### Step 1 — Load Documents

The system reads the resume, job description, and question bank.

```python
intern_profile = clean_text(
    read_file(resume_path)
)

job_description = clean_text(
    read_file(job_path)
)

question_bank = clean_text(
    read_file(question_bank_path)
)
```

### Step 2 — Initialize AI Model

```python
ai_model = InterviewModel()
```

### Step 3 — Initialize Question Generator

```python
generator = QuestionGenerator(ai_model)
```

### Step 4 — Generate Questions

The generator receives all relevant information and produces personalized interview questions.

### Step 5 — Display Questions

The generated questions are displayed in the terminal.

### Step 6 — Save Report

The generated questions are saved to:

```text
outputs/generated_questions.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/FatimaZulfiqarAli-123/AI-Powered-Interview-Question-Generator.git
```

Navigate to the project directory:

```bash
cd AI-Powered-Interview-Question-Generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run the main pipeline:

```bash
python main.py
```

You should see output similar to:

```text
Loading documents...

Documents loaded successfully!

Generating interview questions...

======================================================================
GENERATED INTERVIEW QUESTIONS
======================================================================

[Generated technical and behavioral interview questions]
```

The generated report will be saved in:

```text
outputs/generated_questions.txt
```

---

## 📌 Customization

You can customize the system by changing the following parameters in `main.py`:

### Resume

```python
resume_path = "data/resumes/your_resume.pdf"
```

### Job Description

```python
job_path = "data/job_descriptions/your_job_description.pdf"
```

### Question Bank

```python
question_bank_path = "data/question_bank/questions.txt"
```

### Number of Questions

```python
technical_count=5
behavioral_count=5
```

### Difficulty

```python
difficulty="Medium"
```

Possible difficulty levels can be configured according to the implementation of your `QuestionGenerator`.

---

## 📈 Example Use Cases

This project can be used for:

* 🎓 Student interview preparation
* 💼 Internship interview preparation
* 🧑‍💻 Technical interview preparation
* 📋 Personalized mock interviews
* 🏢 Recruitment assistance
* 🤖 AI-based HR tools
* 📚 Interview practice platforms
