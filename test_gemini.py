import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.0-flash")

response = model.generate_content(
    "What is AI?",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 100
    }
)

print(response.text)