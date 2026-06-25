import os
import google.generativeai as genai

api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "What is AI?",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 100
    }
)

print(response.text)