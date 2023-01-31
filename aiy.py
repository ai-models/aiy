#!/usr/bin/env python3
import argparse
import getpass
import os
import platform
import sys

import openai
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

import aiy_config


def prompt_new_key():
    console.print("[ERROR] OpenAI API key not found. Please set your API key.")
    apikey_new = getpass.getpass("API Key (hidden): ")
    # check if api key is 51 characters long
    if len(apikey_new) != 51:
        print('Invalid API key. Exiting...')
        sys.exit()
    aiy_config.set_api_key(apikey_new)
    return apikey


def pretty_print(openai_response):
    if aiy_config.get_expert_mode() != "true":
        openai_response += '\n\n[Notice] OpenAI\'s models have limited knowledge after 2020. Commands and versions' \
                           'may be outdated.' \
                           'Command recommendations are not guaranteed to work and may be dangerous. Use at your own' \
                           'risk.\n' \
                           'To disable this notice, switch to expert mode with `aiy -x`.'
    console.print(Markdown(openai_response.strip()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query OpenAI')
    parser.add_argument('-x', '--expert', action="store_true", help='Toggle warning', dest='expert')
    parser.add_argument('-i', '--key', action="store_true", help='Clear API key', dest='apikey')
    parser.add_argument('prompt', type=str, nargs='?', help='Prompt to send', dest='prompt')
    args = parser.parse_args()
    console = Console()
    if os.path.exists('.env'):
        load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            console.print("[ERROR] OpenAI API key not found. Please follow these steps to get the API key:\n"
                          "\t1. Go to OpenAI website (https://openai.com/api/login)\n"
                          "\t2. Sign up or log into your account\n"
                          "\t3. Go to the API Key section (https://platform.openai.com/account/api-keys)\n"
                          "\t4. Create a New Secret Key\n"
                          "\t4. Copy the API key\n"
                          "\t5. Set the API key in your .env file as `OPENAI_API_KEY=<your_api_key>`")
            sys.exit()
        os.getenv("OPENAI_MODEL")
    else:  # if .env file doesn't exist, use aiy_config.py
        openai.api_key = aiy_config.get_api_key()
        if not openai.api_key:
            apikey = prompt_new_key()
            openai.api_key = apikey
        engine = aiy_config.get_model()
        if not engine:
            engine = "text-davinci-003"
            aiy_config.set_model(engine)
    if args.apikey:
        aiy_config.set_api_key('')
        console.print("API key cleared. Run aiy again to set a new API key.")
        sys.exit()
    if args.expert:
        aiy_config.toggle_expert_mode()
        sys.exit()
    if not args.prompt:
        prompt = input("Documentation Request: ")
        if prompt == "":
            print("No prompt provided. Exiting...")
            sys.exit()
    os_name = platform.platform()
    os_arch = platform.architecture()[0]
    bash_version = platform.python_version()
    python_version = platform.python_version()
    prompt = f"Please provide a concise list of commands and a brief guide to accomplish this task:\n" \
             f"OS: {os_name}\n" \
             f"Architecture: {os_arch}\n" \
             f"Bash version: {bash_version}\n\n" \
             f"Python version: {python_version}\n\n" \
             f"Format: Markdown, no \n\n{prompt}"
    with console.status(f"Phoning a friend...  ", spinner="pong"):
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        pretty_print(response)
