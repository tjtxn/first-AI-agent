import os
import argparse
from dotenv import load_dotenv
from google import genai

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.prompt`

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-2.5-flash", contents = args.prompt
)

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count


def main():
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    
    print(response.text)


if __name__ == "__main__":
    main()
