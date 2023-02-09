import requests
import dotenv
import os
import logging
from rich.logging import RichHandler

dotenv.load_dotenv()

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

def query(input):
    response = requests.get(
        "https://platform.openai.com/v1/engines/text-davinci-003-playground/completions",
        headers={
            'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
            },
            params={
                'prompt': input,
            },
            timeout=10,
    )
    return response.json()

def main():
    logging.info("Welcome to the OpenAI Text Completion API Demo")
    logging.info("Type 'exit' to quit")
    while True:
        promt = input("Enter a prompt: ")
        if promt == "exit":
            break
        response = query(promt)
        logging.info(f"Completion: {response['choices'][0]['text']}")

if __name__ == "__main__":
    main()