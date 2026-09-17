# ============================================================
# AI-POWERED INTERVIEW QUESTION GENERATOR
# app.py
# ============================================================

import gradio as gr
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)


# ============================================================
# SECTION 01 — CONFIGURATION
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"

MAX_NEW_TOKENS = 2500


# ============================================================
# SECTION 02 — LOAD AI MODEL
# ============================================================

print("=" * 70)
print("AI-POWERED INTERVIEW QUESTION GENERATOR")
print("=" * 70)

print("\nLoading AI model...")
print(f"Model: {MODEL_NAME}")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=(
        torch.float16
        if torch.cuda.is_available()
        else torch.float32
    ),
    device_map="auto"
)

print("AI model loaded successfully!")

if torch.cuda.is_available():
    print(
        "Using GPU:",
        torch.cuda.get_device_name(0)
    )
else:
    print("Using CPU")


# ============================================================
# SECTION 03 — GENERATE TEXT
# ============================================================

def generate_text(prompt, max_new_tokens=MAX_NEW_TOKENS):

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        text,
        return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():

        outputs = model.generate(
            **inputs,

            max_new_tokens=max_new_tokens,

            temperature=0.7,

            top_p=0.9,

            do_sample=True,

            repetition_penalty=1.1
        )

    response = tokenizer.decode(
        outputs[0][
            inputs["input_ids"].shape[1]:
        ],
        skip_special_tokens=True
    )

    return response.strip()


# ============================================================
# SECTION 04 — CREATE INTERVIEW PROMPT
# ============================================================

def create_interview_prompt(
    intern_profile,
    job_description,
    question_bank,
    technical_count,
    behavioral_count,
    difficulty
):

    prompt = f"""
You are an expert technical interviewer
specialized in internship recruitment.

Your task is to generate a customized interview
question set for an internship candidate.

==================================================
CANDIDATE PROFILE
==================================================

{intern_profile}

==================================================
JOB DESCRIPTION
==================================================

{job_description}

==================================================
EXISTING QUESTION BANK
==================================================

{question_bank}

==================================================
INTERVIEW REQUIREMENTS
==================================================

Generate:

Technical Questions:
{technical_count}

Behavioral Questions:
{behavioral_count}

Difficulty Level:
{difficulty}

==================================================
IMPORTANT INSTRUCTIONS
==================================================

1. Analyze the candidate profile carefully.

2. Analyze the job description carefully.

3. Identify the candidate's relevant skills,
   education, projects and experience.

4. Match questions to the job requirements.

5. Questions should be suitable for an intern.

6. Avoid irrelevant questions.

7. Do not simply copy questions from the
   existing question bank.

8. Generate original questions where possible.

9. Include a mixture of conceptual and
   practical technical questions.

10. Behavioral questions should relate to
    teamwork, communication, challenges,
    learning, problem solving and motivation.

11. Questions should reflect the requested
    difficulty level.

12. Include a follow-up question for every
    main question.

==================================================
OUTPUT FORMAT
==================================================

TECHNICAL QUESTIONS

Question 1:
Difficulty:
Why Relevant:
Follow-up Question:

Question 2:
Difficulty:
Why Relevant:
Follow-up Question:

Continue until all technical questions
are generated.

==================================================

BEHAVIORAL QUESTIONS

Question 1:
Difficulty:
Why Relevant:
Follow-up Question:

Question 2:
Difficulty:
Why Relevant:
Follow-up Question:

Continue until all behavioral questions
are generated.

==================================================

FINAL REQUIREMENT
==================================================

Make the interview questions specific to the
candidate and the internship role.

Do not provide explanations outside the requested
format.
"""

    return prompt


# ============================================================
# SECTION 05 — MAIN INTERVIEW GENERATOR
# ============================================================

def interview_generator(
    intern_profile,
    job_description,
    question_bank,
    technical_count,
    behavioral_count,
    difficulty
):

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not intern_profile.strip():

        return (
            "⚠️ Please enter the candidate "
            "profile or resume."
        )

    if not job_description.strip():

        return (
            "⚠️ Please enter the job description."
        )

    if not question_bank.strip():

        question_bank = (
            "No existing question bank was provided. "
            "Generate original questions based on "
            "the candidate and job description."
        )

    # --------------------------------------------------------
    # Create prompt
    # --------------------------------------------------------

    prompt = create_interview_prompt(

        intern_profile=intern_profile,

        job_description=job_description,

        question_bank=question_bank,

        technical_count=int(
            technical_count
        ),

        behavioral_count=int(
            behavioral_count
        ),

        difficulty=difficulty
    )

    # --------------------------------------------------------
    # Generate questions
    # --------------------------------------------------------

    try:

        result = generate_text(
            prompt
        )

        return result

    except Exception as error:

        return (
            "❌ An error occurred while generating "
            f"the questions:\n\n{str(error)}"
        )


# ============================================================
# SECTION 06 — MODERN CSS
# ============================================================

custom_css = """

/* ==========================================================
   GLOBAL
   ========================================================== */

body {
    margin: 0;
    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
}

.gradio-container {
    max-width: 1500px !important;
    margin: auto !important;
}


/* ==========================================================
   MAIN APPLICATION
   ========================================================== */

#main-container {

    min-height: 100vh;

    padding:
        25px
        35px
        60px
        35px;

}


/* ==========================================================
   HEADER
   ========================================================== */

#header {

    text-align: center;

    padding:
        35px
        20px
        30px
        20px;

}


#header .badge {

    display: inline-block;

    padding:
        8px
        17px;

    border-radius: 50px;

    background:
        rgba(99, 102, 241, 0.12);

    color:
        #6366f1;

    font-size:
        12px;

    font-weight:
        750;

    letter-spacing:
        0.5px;

    margin-bottom:
        18px;

}


#header h1 {

    margin:
        0;

    font-size:
        44px;

    font-weight:
        850;

    letter-spacing:
        -1.5px;

    line-height:
        1.1;

}


#header p {

    max-width:
        760px;

    margin:
        18px auto 0 auto;

    font-size:
        16px;

    line-height:
        1.7;

    opacity:
        0.68;

}


/* ==========================================================
   INPUT CARDS
   ========================================================== */

.input-card {

    border:
        1px solid
        rgba(120, 120, 120, 0.18)
        !important;

    border-radius:
        18px
        !important;

    padding:
        22px
        !important;

    background:
        rgba(255, 255, 255, 0.035)
        !important;

    box-shadow:
        0 10px 30px
        rgba(0, 0, 0, 0.06)
        !important;

    transition:
        all 0.25s ease;

}


.input-card:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 15px 35px
        rgba(0, 0, 0, 0.10)
        !important;

}


/* ==========================================================
   CARD TITLE
   ========================================================== */

.card-title {

    font-size:
        18px;

    font-weight:
        750;

    margin-bottom:
        6px;

}


.card-description {

    font-size:
        13px;

    opacity:
        0.62;

    line-height:
        1.5;

    margin-bottom:
        15px;

}


/* ==========================================================
   TEXT INPUT
   ========================================================== */

textarea {

    border-radius:
        12px
        !important;

    border:
        1px solid
        rgba(120, 120, 120, 0.25)
        !important;

    font-size:
        14px
        !important;

    line-height:
        1.6
        !important;

}


textarea:focus {

    border-color:
        #6366f1
        !important;

    box-shadow:
        0 0 0 3px
        rgba(99, 102, 241, 0.12)
        !important;

}


/* ==========================================================
   SETTINGS
   ========================================================== */

#settings-card {

    margin-top:
        22px;

    padding:
        25px
        !important;

    border-radius:
        18px
        !important;

    border:
        1px solid
        rgba(120, 120, 120, 0.18)
        !important;

}


/* ==========================================================
   GENERATE BUTTON
   ========================================================== */

#generate-btn {

    margin-top:
        25px;

    height:
        58px;

    border-radius:
        14px
        !important;

    font-size:
        16px
        !important;

    font-weight:
        750
        !important;

    border:
        none
        !important;

    background:
        linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        )
        !important;

    color:
        white
        !important;

    transition:
        all 0.25s ease;

}


#generate-btn:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 12px 30px
        rgba(99, 102, 241, 0.30);

}


/* ==========================================================
   OUTPUT CARD
   ========================================================== */

#output-card {

    margin-top:
        30px;

    border-radius:
        18px
        !important;

    padding:
        25px
        !important;

    border:
        1px solid
        rgba(120, 120, 120, 0.18)
        !important;

}


#output-card textarea {

    min-height:
        550px !important;

}


/* ==========================================================
   FOOTER
   ========================================================== */

#footer {

    text-align:
        center;

    margin-top:
        45px;

    opacity:
        0.5;

    font-size:
        13px;

}


/* ==========================================================
   RESPONSIVE DESIGN
   ========================================================== */

@media (max-width: 900px) {

    #main-container {

        padding:
            15px;

    }

    #header h1 {

        font-size:
            32px;

    }

}

"""


# ============================================================
# SECTION 07 — HTML HEADER
# ============================================================

header_html = """

<div id="header">

    <div class="badge">
        ✦ AI-POWERED INTERVIEW SYSTEM
    </div>

    <h1>
        Interview Question Generator
    </h1>

    <p>
        Generate intelligent, role-specific technical
        and behavioral interview questions using
        candidate profiles, job descriptions,
        and existing question banks.
    </p>

</div>

"""


# ============================================================
# SECTION 08 — BUILD GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    css=custom_css,
    title="AI Interview Question Generator"
) as app:

    # ========================================================
    # HEADER
    # ========================================================

    gr.HTML(
        header_html
    )


    # ========================================================
    # MAIN CONTAINER
    # ========================================================

    with gr.Column(
        elem_id="main-container"
    ):

        # ====================================================
        # INPUT SECTION
        # ====================================================

        with gr.Row():

            # ------------------------------------------------
            # CANDIDATE PROFILE
            # ------------------------------------------------

            with gr.Column(
                elem_classes="input-card"
            ):

                gr.HTML(
                    """
                    <div class="card-title">
                        👤 Candidate Profile
                    </div>

                    <div class="card-description">
                        Enter the intern's resume,
                        education, skills and projects.
                    </div>
                    """
                )

                intern_profile = gr.Textbox(

                    placeholder=(
                        "Paste the candidate's "
                        "resume or profile here..."
                    ),

                    lines=12,

                    show_label=False
                )


            # ------------------------------------------------
            # JOB DESCRIPTION
            # ------------------------------------------------

            with gr.Column(
                elem_classes="input-card"
            ):

                gr.HTML(
                    """
                    <div class="card-title">
                        💼 Job Description
                    </div>

                    <div class="card-description">
                        Enter the internship role,
                        responsibilities and requirements.
                    </div>
                    """
                )

                job_description = gr.Textbox(

                    placeholder=(
                        "Paste the internship job "
                        "description here..."
                    ),

                    lines=12,

                    show_label=False
                )


            # ------------------------------------------------
            # QUESTION BANK
            # ------------------------------------------------

            with gr.Column(
                elem_classes="input-card"
            ):

                gr.HTML(
                    """
                    <div class="card-title">
                        📚 Question Bank
                    </div>

                    <div class="card-description">
                        Add your existing technical
                        and behavioral questions.
                    </div>
                    """
                )

                question_bank = gr.Textbox(

                    placeholder=(
                        "Paste existing interview "
                        "questions here..."
                    ),

                    lines=12,

                    show_label=False
                )


        # ====================================================
        # SETTINGS
        # ====================================================

        with gr.Column(
            elem_id="settings-card"
        ):

            gr.Markdown(
                "### ⚙️ Interview Settings"
            )

            with gr.Row():

                technical_count = gr.Slider(

                    minimum=1,

                    maximum=15,

                    value=5,

                    step=1,

                    label="Technical Questions"
                )


                behavioral_count = gr.Slider(

                    minimum=1,

                    maximum=15,

                    value=5,

                    step=1,

                    label="Behavioral Questions"
                )


                difficulty = gr.Dropdown(

                    choices=[
                        "Easy",
                        "Medium",
                        "Hard"
                    ],

                    value="Medium",

                    label="Difficulty Level"
                )


        # ====================================================
        # GENERATE BUTTON
        # ====================================================

        generate_button = gr.Button(

            "✨ Generate Interview Questions",

            elem_id="generate-btn"
        )


        # ====================================================
        # OUTPUT
        # ====================================================

        with gr.Column(
            elem_id="output-card"
        ):

            gr.Markdown(
                "## 🎯 Generated Interview Questions"
            )

            output = gr.Textbox(

                show_label=False,

                lines=30,

                placeholder=(
                    "Your customized interview "
                    "questions will appear here..."
                )
            )


        # ====================================================
        # FOOTER
        # ====================================================

        gr.HTML(
            """
            <div id="footer">
                AI-Powered Interview Question Generator
                • Internship Recruitment System
            </div>
            """
        )


    # ========================================================
    # BUTTON EVENT
    # ========================================================

    generate_button.click(

        fn=interview_generator,

        inputs=[

            intern_profile,

            job_description,

            question_bank,

            technical_count,

            behavioral_count,

            difficulty

        ],

        outputs=output
    )


# ============================================================
# SECTION 09 — LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

    print("\nStarting web application...")

    app.launch(
        share=True
    )