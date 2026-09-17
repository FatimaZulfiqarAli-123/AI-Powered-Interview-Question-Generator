# ============================================================
# SECTION 06: AI MODEL
# ============================================================

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

from src.config import MODEL_NAME


class InterviewModel:

    def __init__(self):

        print("Loading AI model...")

        self.tokenizer = (
            AutoTokenizer.from_pretrained(
                MODEL_NAME
            )
        )

        self.model = (
            AutoModelForCausalLM.from_pretrained(
                MODEL_NAME,

                torch_dtype=(
                    torch.float16
                    if torch.cuda.is_available()
                    else torch.float32
                ),

                device_map="auto"
            )
        )

        print("AI model loaded successfully!")

    def generate(
        self,
        prompt,
        max_new_tokens=2500
    ):

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        ).to(self.model.device)

        with torch.no_grad():

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )

        response = self.tokenizer.decode(
            outputs[0][
                inputs["input_ids"].shape[1]:
            ],
            skip_special_tokens=True
        )

        return response