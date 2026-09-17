# ============================================================
# SECTION 08: QUESTION GENERATOR
# ============================================================

from src.prompt_generator import create_interview_prompt


class QuestionGenerator:

    def __init__(self, model):

        self.model = model


    def generate(
        self,
        intern_profile,
        job_description,
        question_bank,
        technical_count=5,
        behavioral_count=5,
        difficulty="Medium"
    ):

        prompt = create_interview_prompt(
            intern_profile=intern_profile,
            job_description=job_description,
            question_bank=question_bank,
            technical_count=technical_count,
            behavioral_count=behavioral_count,
            difficulty=difficulty
        )

        result = self.model.generate(
            prompt
        )

        return result