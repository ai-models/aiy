#!/usr/bin/env python3
import argparse
import os
import platform
import sys

from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt

from resources import config
from resources.conduit import get_completion

console = Console()
version = "0.2.0"


def pre_completion(user_input):
    user_input = "Users Kernel:" + platform.platform() + "\n" \
                 "Users OS:" + os.uname().version + "\n" \
                 "Users Shell:" + os.environ.get("SHELL", "").split("/")[-1] + "\n\n" \
                 f"User question: {user_input}\n\n" \
                 f"Please provide a concise response to the user's question. Where appropriate provide commands or " \
                 f"code examples with descriptions. Unless specified otherwise assume the kernel, OS, and shell " \
                 f"information provides context for the users question.\n " \
                 f"Response Format: Markdown\n\n"
    return user_input


def post_completion(openai_response):
    if config.get_expert_mode() != "true":
        openai_response = f"> Aiy v{version}\n\n" + openai_response
        openai_response += '\n\n[Notice] OpenAI\'s models have limited knowledge after 2020. Commands and versions' \
                           'may be outdated. Recommendations are not guaranteed to work and may be dangerous.' \
                           'To disable this notice, switch to expert mode with `aiy --expert`.'
    return openai_response


def main():
    desc = "This tool sends a query to OpenAI from the command line and is used to resolve\n" \
           "technical questions that a user might encounter while working in the shell or CLI \n" \
           "environment.\n\n" \
           "  Example: aiy 'how to install a package in python'\n" \
           "           aiy 'how do I search for a file or directory'\n\n" \
           "The query contains information about your OS and architecture, as well as the\n" \
           "question you asked to ensure that the responses are tailored to your system.\n\n" \
           "  System information: \n" \
           "    Kernel:\t" + platform.platform() + "\n" \
           "    OS:    \t" + os.uname().version + "\n" \
           "    Shell: \t" + os.environ.get("SHELL", "").split("/")[-1] + "\n\n" \
           "Report any issues at: https://github.com/visioninit/aiy/issues"
    epilog = "Please note that the responses from OpenAI's API are not guaranteed to be accurate and " \
            "use of the tool is at your own risk.\n"

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(prog='aiy - CLI assistant',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=desc,
                                     epilog=epilog)

    # Add arguments for expert mode, API key reset, version, and prompt
    parser.add_argument('-x', '--expert', action="store_true", help='Toggle warning', dest='expert')
    parser.add_argument('-i', '--key', action="store_true", help='Reset API key', dest='apikey')
    parser.add_argument('-v', '--version', action="store_true", help='Get Version', dest='version')
    parser.add_argument('prompt', type=str, nargs='?', help='Prompt to send')
    args = parser.parse_args()

    if args.version:
        console.print("aiy version: " + version)
        sys.exit()
    config.check_config(console)
    if args.apikey:
        config.prompt_new_key()
        sys.exit()
    if args.expert:
        config.toggle_expert_mode()
        sys.exit()
    if not args.prompt:
        prompt = Prompt.ask("Documentation Request")
        if prompt == "":
            print("No prompt provided. Exiting...")
            sys.exit()
        prompt = pre_completion(prompt)
    else:
        prompt = pre_completion(args.prompt)

    with console.status(f"Phoning a friend...  ", spinner="pong"):
        openai_response = post_completion(get_completion(prompt))
        console.print(Markdown(openai_response.strip()))


if __name__ == "__main__":
    main()
