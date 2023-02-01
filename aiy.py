#!/usr/bin/env python3
import argparse
import platform
import sys

from rich.console import Console
from rich.markdown import Markdown

from resources import config
from resources.condiut import get_completion


def pre_completion(user_input):
    os_name = platform.platform()
    os_arch = platform.architecture()[0]
    user_input = f"Please provide a concise list of commands and a brief guide to accomplish this task:\n" \
             f"OS: {os_name}\n" \
             f"Architecture: {os_arch}\n" \
             f"Format: Markdown, no \n\n{user_input}"
    return user_input
def post_completion(openai_response):
    if config.get_expert_mode() != "true":
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
    parser.add_argument('prompt', type=str, nargs='?', help='Prompt to send')
    args = parser.parse_args()
    console = Console()

    if args.apikey:
        config.set_api_key('')
        config.prompt_new_key()
        sys.exit()
    if args.expert:
        config.toggle_expert_mode()
        sys.exit()
    if not args.prompt:
        prompt = input("Documentation Request: ")
        if prompt == "":
            print("No prompt provided. Exiting...")
            sys.exit()
        prompt = pre_completion(prompt)
    else:
        prompt = pre_completion(args.prompt)
    with console.status(f"Phoning a friend...  ", spinner="pong"):
        post_completion(get_completion(prompt))
