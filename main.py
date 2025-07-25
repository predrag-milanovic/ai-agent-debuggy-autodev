import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


def main():
    # Loads environment variables from .env file (where API key is stored)
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)  
    
    # Retrieves the secret API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    # Initializes the Gemini client with your API key
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    # Create a message structure compatible with Gemini's chat API
    # Using types.Content ensures proper formatting of:
                                                        # - role ("user" for user input)
                                                        # - parts (array of message components, here just text)
    messages = [
        types.Content(role="user",                # Identifies the message sender (user/assistant)
        parts=[types.Part(text=user_prompt)]),    # Actual content payload
    ]

    # Pass the structured messages to our generation handler
    generate_content(client, messages)

# Handles the actual Gemini API request with proper error boundaries
def generate_content(client, messages):
    # Make the actual API call
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",   # Fast/cheap model for prototyping
        contents=messages,              # Our formatted conversation history
    )
    
    # Prints the AI-generated response
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()  # Standard Python entry point