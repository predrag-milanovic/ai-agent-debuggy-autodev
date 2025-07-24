import os
from google import genai
from dotenv import load_dotenv


def main():
    # Loads environment variables from .env file (where API key is stored)
    load_dotenv()
    
    # Retrieves the secret API key from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Initializes the Gemini client with your API key
    client = genai.Client(api_key=api_key)
    
    # Sends prompt to Gemini's flash model and gets response
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",  # Free-tier efficient model
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",  # Your prompt
    )
    
    # Debugging info - shows token usage (important for cost monitoring)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    # Prints the AI-generated response
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()  # Standard Python entry point