"""
Provides a wrapper for Google's Gemini API to make it compatible with
frameworks or systems that expect a specific model interface (e.g., a callable
model or a model with a specific message format).
"""
import os
import google.generativeai as genai

class Message:
    """
    Represents a message in a conversation, typically with a role (e.g., "user",
    "assistant") and content. This class provides a minimal structure for
    compatibility with certain agent frameworks or logging systems.
    """
    def __init__(self, role: str, content: str):
        """
        Initializes a Message object.

        Args:
            role: The role of the message sender (e.g., "user", "assistant", "system").
            content: The textual content of the message.
        """
        self.role = role
        self.content = content

class GeminiModel:
    """
    A wrapper class for Google's Gemini API, making it callable and adaptable
    to specific input/output message formats. It handles API configuration,
    model initialization, and request formatting.
    """
    def __init__(self, model_name="gemini-1.5-flash", temperature=0.7):
        """
        Initializes the GeminiModel.

        Args:
            model_name: The name of the Gemini model to use (e.g., "gemini-1.5-flash", "gemini-pro").
            temperature: The sampling temperature for generation, controlling randomness.
                         Lower values make the output more deterministic.
        """
        # Configure the Gemini API with the API key from environment variables.
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # Initialize the generative model client.
        self.client = genai.GenerativeModel(model_name)
        self.temperature = temperature # Note: Temperature is set but not directly used in generate_content call in this version.
                                     # It would typically be passed to generation_config.

    def __call__(self, input_messages, stop_sequences=None):
        """
        Makes the model callable, processing input messages and returning the model's response.

        Args:
            input_messages: Can be a string or a list of message dictionaries.
                            If a list, messages are concatenated to form the prompt.
                            Each dictionary should have a "content" key.
            stop_sequences: A list of sequences to stop generation at (currently not used by this wrapper
                            but common in LLM APIs).

        Returns:
            A Message object containing the assistant's response.
        """
        if isinstance(input_messages, list) and input_messages and isinstance(input_messages[0], dict):
            # If input is a list of message dicts, extract content and join.
            # This handles formats like OpenAI's messages or similar structures.
            prompt_parts = []
            for msg in input_messages:
                content = msg.get("content")
                if isinstance(content, str):
                    prompt_parts.append(content)
                elif isinstance(content, list): # Handles cases where content might be a list of parts (e.g., multimodal)
                    for part in content:
                        if isinstance(part, str):
                            prompt_parts.append(part)
                        elif isinstance(part, dict) and "text" in part: # Common for text parts in multimodal
                            prompt_parts.append(part.get("text", ""))
            prompt = "\n".join(prompt_parts)
        elif isinstance(input_messages, str):
            prompt = input_messages
        else:
            # Fallback for other input types.
            prompt = str(input_messages)

        # Note: The current genai.GenerativeModel().generate_content() call here is simple.
        # For more control (like temperature, stop_sequences), a GenerationConfig object
        # would be used: genai.types.GenerationConfig(temperature=self.temperature, stop_sequences=stop_sequences)
        # and passed to generate_content(..., generation_config=config).
        # The current implementation uses the model's default temperature unless explicitly configured in GenerationConfig.
        result = self.client.generate_content(contents=[{"role": "user", "parts": [{"text": prompt}]}]) # Ensure 'contents' is a list of Content parts

        # The API might return multiple candidates or parts; here we take the text from the first part of the first candidate.
        # Error handling for empty or unexpected response structure would be beneficial in production.
        response_text = ""
        if result.candidates and result.candidates[0].content and result.candidates[0].content.parts:
            response_text = result.candidates[0].content.parts[0].text

        return Message(role="assistant", content=response_text)


if __name__ == "__main__":
    # Example Usage:
    # Important: Set your GOOGLE_API_KEY environment variable before running.
    # For testing purposes, you can uncomment and set it here:
    # os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE" # Do not commit your actual key!

    # Ensure the API key is available, otherwise, the script will fail here.
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please set it before running the example.")
    else:
        # Initialize the model (using a readily available model like gemini-1.5-flash)
        model = GeminiModel(model_name="gemini-1.5-flash-latest") # Using a common, generally available model

        # Example 1: Simple string input
        print("--- Example 1: String Input ---")
        response1 = model("Suggest a quick and healthy breakfast idea.")
        print(f"Assistant: {response1.content}\n")

        # Example 2: List of message dictionaries (OpenAI-like format)
        print("--- Example 2: List of Dicts Input ---")
        messages = [
            {"role": "system", "content": "You are a helpful cooking assistant specialized in vegetarian cuisine."},
            {"role": "user", "content": "Suggest a vegetarian recipe under 300 calories for dinner."}
        ]
        response2 = model(messages)
        print(f"Assistant: {response2.content}")
