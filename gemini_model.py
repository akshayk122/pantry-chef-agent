import os
import google.generativeai as genai

# Minimal compatibility wrapper
class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class GeminiModel:
    def __init__(self, model="gemini-2.5-pro-preview-03-25", temperature=0.7):
        #genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        genai.configure(api_key='AIzaSyDOwA6QzNY5ezsX03nfkCU0yRR0_7Pp3RY')
        self.client = genai.GenerativeModel(model)
        self.temperature = temperature

    def __call__(self, input_messages, stop_sequences=None):
        if isinstance(input_messages, list) and isinstance(input_messages[0], dict):
            prompt_parts = []
            for msg in input_messages:
                content = msg.get("content")
                if isinstance(content, str):
                    prompt_parts.append(content)
                elif isinstance(content, list):
                    for part in content:
                        if isinstance(part, str):
                            prompt_parts.append(part)
                        elif isinstance(part, dict):
                            prompt_parts.append(part.get("text", ""))
            prompt = "\n".join(prompt_parts)
        else:
            prompt = str(input_messages)

        result = self.client.generate_content([{"role": "user", "parts": [prompt]}])
        return Message(role="assistant", content=result.text)




if __name__ == "__main__":
    os.environ["GOOGLE_API_KEY"] = "AIzaSyDOwA6QzNY5ezsX03nfkCU0yRR0_7Pp3RY"
    model = GeminiModel()
    print(model([
        {"role": "system", "content": "You are a helpful cooking assistant."},
        {"role": "user", "content": "Suggest a veg recipe under 300 calories"}
    ]))