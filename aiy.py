#!/usr/bin/env python3
import argparse
import os
import platform

import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# load dotenv from real path
load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    console.print("  [ERROR] OpenAI API key not found. Please follow these steps to get the API key:\n"
                  "\t1. Go to OpenAI website (https://openai.com/api/login)\n"
                  "\t2. Sign up or log into your account\n"
                  "\t3. Go to the API Key section (https://platform.openai.com/account/api-keys)\n"
                  "\t4. Create a New Secret Key\n"
                  "\t4. Copy the API key\n"
                  "\t5. Set the API key in your .env file as `OPENAI_API_KEY=<your_api_key>`")
    exit()


def pretty_print(response):
    if os.getenv("OPENAI_DISABLE_NOTICE") != "true":
        response += "\n[Notice] OpenAI's models have limited knowledge after 2020. Commands and versions may be outdated." \
                    "Command recommendations are not guaranteed to work and may be dangerous. Use at your own risk.\n" \
                    "To disable this notice, set the environment variable OPENAI_DISABLE_NOTICE to true."
    console.print(Markdown(response.strip()))


def main(prompt):
    os_name = platform.system()
    os_arch = platform.architecture()[0]
    bash_version = platform.python_version()
    prompt = f"Please provide a concise list of commands and a brief guide to accomplish this tasks:\n" \
             f"OS name: {os_name}\n" \
             f"Architecture: {os_arch}\n" \
             f"Bash version: {bash_version}\n\n" \
             f"Format: Markdown, no \n\n{prompt}"

    with console.status("Phoning a friend... ", spinner="pong"):
        response = openai.Completion.create(
            engine=os.getenv("OPENAI_MODEL"),
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        pretty_print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query OpenAI')
    parser.add_argument('prompt', type=str, nargs='?', help='prompt to send')
    args = parser.parse_args()

    if args.prompt:
        main(args.prompt)
    else:
        prompt = input("Documentation Request: ")
        main(prompt)