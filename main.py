import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt       # Import the system prompt


def main():
    # Loads environment variables from .env file (where API key is stored)
    load_dotenv()

    # New verbose flag detection (before processing args)
    verbose = "--verbose" in sys.argv   # Checks if --verbose is anywhere in args
    args = []
    for arg in sys.argv[1:]:
         if not arg.startswith("--"):   # Excludes all flag-style arguments
            args.append(arg)            # Keeps only prompt parts

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)  
    
    # Retrieves the secret API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    # Initializes the Gemini client with your API key
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    # Verbose output for prompt
    if verbose:
        print(f"User prompt: {user_prompt}\n")    # Shows raw prompt

    # Create a message structure compatible with Gemini's chat API
    # Using types.Content ensures proper formatting of:
                                                        # - role ("user" for user input)
                                                        # - parts (array of message components, here just text)
    messages = [
        types.Content(role="user",                # Identifies the message sender (user/assistant)
        parts=[types.Part(text=user_prompt)]),    # Actual content payload
    ]

    # Pass the structured messages to our generation handler
    generate_content(client, messages, verbose)

# Handles the actual Gemini API request with proper error boundaries
def generate_content(client, messages, verbose):
    # Make the actual API call
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",   # Fast/cheap model for prototyping
        contents=messages,              # Our formatted conversation history
        config=types.GenerateContentConfig(
            system_instruction=system_prompt    # Force AI behavior
        ),
    )
    if verbose:     # New token counters
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)  
  
    # Prints the AI-generated response
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()  # Standard Python entry point