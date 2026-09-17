# ============================================================
# AI-POWERED INTERVIEW QUESTION GENERATOR
# MAIN PIPELINE
# ============================================================

from src.document_loader import (
    read_file,
    clean_text
)

from src.model import InterviewModel

from src.question_generator import (
    QuestionGenerator
)

from src.report_generator import (
    create_report,
    save_report
)


# ------------------------------------------------------------
# SECTION 11.1 — FILE PATHS
# ------------------------------------------------------------

resume_path = (
    "data/resumes/Fatima_CV_001.pdf"
)

job_path = (
    "data/job_descriptions/ml_intern_job.pdf"
)

question_bank_path = (
    "data/question_bank/questions.txt"
)


# ------------------------------------------------------------
# SECTION 11.2 — LOAD DOCUMENTS
# ------------------------------------------------------------

print("\nLoading documents...")

intern_profile = clean_text(
    read_file(resume_path)
)

job_description = clean_text(
    read_file(job_path)
)

question_bank = clean_text(
    read_file(question_bank_path)
)

print("Documents loaded successfully!")


# ------------------------------------------------------------
# SECTION 11.3 — LOAD AI MODEL
# ------------------------------------------------------------

ai_model = InterviewModel()


# ------------------------------------------------------------
# SECTION 11.4 — CREATE QUESTION GENERATOR
# ------------------------------------------------------------

generator = QuestionGenerator(
    ai_model
)


# ------------------------------------------------------------
# SECTION 11.5 — GENERATE QUESTIONS
# ------------------------------------------------------------

print("\nGenerating interview questions...")

result = generator.generate(

    intern_profile=intern_profile,

    job_description=job_description,

    question_bank=question_bank,

    technical_count=5,

    behavioral_count=5,

    difficulty="Medium"
)


# ------------------------------------------------------------
# SECTION 11.6 — DISPLAY RESULT
# ------------------------------------------------------------

print("\n")
print("=" * 70)

print(
    "GENERATED INTERVIEW QUESTIONS"
)

print("=" * 70)

print(result)


# ------------------------------------------------------------
# SECTION 11.7 — SAVE REPORT
# ------------------------------------------------------------

report = create_report(
    candidate_name="Fatima",
    result=result
)

save_report(
    report,
    "outputs/generated_questions.txt"
)