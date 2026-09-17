# ============================================================
# SECTION 07: PROMPT GENERATOR
# ============================================================


def create_interview_prompt(
    intern_profile,
    job_description,
    question_bank,
    technical_count=5,
    behavioral_count=5,
    difficulty="Medium"
):

    prompt = f"""
You are an expert technical interviewer.

Your task is to generate customized interview
questions for an internship candidate.

========================
CANDIDATE PROFILE
========================

{intern_profile}

========================
JOB DESCRIPTION
========================

{job_description}

========================
EXISTING QUESTION BANK
========================

{question_bank}

========================
INTERVIEW REQUIREMENTS
========================

Generate:

Technical questions: {technical_count}

Behavioral questions: {behavioral_count}

Difficulty: {difficulty}

========================
IMPORTANT RULES
========================

1. Questions must be relevant to the candidate.

2. Questions must match the job description.

3. Consider the candidate's skills and projects.

4. Do not simply copy questions from the question bank.

5. Create original questions where appropriate.

6. Avoid irrelevant questions.

7. Include follow-up questions.

8. Questions should be appropriate for an intern.

========================
OUTPUT
========================

Divide the output into:

TECHNICAL QUESTIONS

BEHAVIORAL QUESTIONS

For every question include:

Question:
Difficulty:
Why Relevant:
Follow-up Question:

"""

    return prompt