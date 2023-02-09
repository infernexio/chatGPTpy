from pyChatGPT import ChatGPT
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

def main():
    api = ChatGPT(os.getenv("OPENAI_TOKEN"),chrome_args=['--window-size=800,600'])  # auth with session token
    inp = input("input: ")
    resp = api.send_message(inp)
    print(resp['message'])


if __name__ == "__main__":
    main()