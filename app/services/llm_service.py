import os

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


load_dotenv()


class LLMService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set.")

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-3.6-flash"

    def generate(self, prompt: str):

        interaction = self.client.interactions.create(
            model=self.model,
            input=prompt
        )

        return interaction.output_text

    def generate_structured(
        self,
        prompt: str,
        response_model: type[BaseModel]
    ):

        interaction = self.client.interactions.create(
            model=self.model,
            input=prompt,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": response_model.model_json_schema(),
            },
        )

        return response_model.model_validate_json(
            interaction.output_text
        )