import getpass
import os
import platform
import re
import subprocess
import sys

import appdirs
from rich.prompt import Prompt

def user_data(type):
    if type == "bash":
        result = subprocess.run(['bash', '--version'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        match = re.search(r'GNU bash, version ([\d.]+)', output)
        if match:
            version = match.group(1)
            print(f"The version of bash is: {version}")
        else:
            print("Could not determine the version of bash")

def prompt_new_key():
    apikey_new = Prompt.ask("OpenAI API Key (hidden)", password=True)
    if len(apikey_new) != 51:
        print('Invalid API key. Exiting...')
        sys.exit()
    set_api_key(apikey_new)
    return apikey_new


def check_config(console):
    if not get_api_key():
        os_name = str(os.name)
        os_uname = os.uname()

        console.print("--[Aiy - CLI Assistant]-------\n"
                      "\n"
                      "OpenAI API key not found. Please follow these steps to get the API key:\n"
                      "  1. Go to OpenAI website (https://openai.com/api/login)\n"
                      "  2. Sign up or log into your account\n"
                      "  3. Go to the API Key section (https://platform.openai.com/account/api-keys)\n"
                      "  4. Create a New Secret Key\n"
                      "  4. Copy the API key\n"
                      "\n"
                      "The queries sent to OpenAI contain your OS and architecture information, as well as the "
                      "question you asked. This is so that responses will be catered to you as much as possible\n"
                      "Example:\n"
                      "  " + platform.platform() + "\n"
                      "  " + os_uname.version + "\n"
                      "  " + os.environ.get("SHELL", "").split("/")[-1] + "\n"
                      "Please be advised that responses from OpenAI's API are not guaranteed to be accurate. "
                      "Use at your own risk.\n")
        key = prompt_new_key()
        set_api_key(key)
    if not get_model():
        set_model("text-davinci-003")
    if not get_expert_mode():
        set_expert_mode("false")


def _get_config(key):
    if not os.path.exists(_config_file):
        return None

    with open(_config_file, "r") as f:
        for line in f.readlines():
            if line.startswith(f"{key}="):
                return line.split("=")[1].strip()



def _update_config(key, value):
    if not os.path.exists(_config_dir):
        os.makedirs(_config_dir)

    lines = []
    if os.path.exists(_config_file):
        with open(_config_file, "r") as f:
            lines = f.readlines()

    updated = False
    with open(_config_file, "w") as f:
        for line in lines:
            if line.startswith(f"{key}="):
                f.write(f"{key}={value}\n")
                updated = True
            else:
                f.write(line)

    if not updated:
        with open(_config_file, "a") as f:
            f.write(f"{key}={value}\n")


def set_api_key(api_key):
    _update_config("OPENAI_API_KEY", api_key)


def get_api_key():
    if not os.path.exists(_config_file):
        return None

    with open(_config_file, "r") as f:
        for line in f:
            if line.startswith("OPENAI_API_KEY="):
                return line[len("OPENAI_API_KEY="):].strip()


def set_model(model):
    _update_config("OPENAI_MODEL", model)


def get_model():
    if not os.path.exists(_config_file):
        return None

    with open(_config_file, "r") as f:
        for line in f:
            if line.startswith("OPENAI_MODEL="):
                return line[len("OPENAI_MODEL="):].strip()


def toggle_expert_mode():
    if get_expert_mode() == "true":
        print("Expert mode disabled. You will see the warning again.")
        set_expert_mode("false")
    else:
        print("Expert mode enabled. You will not see the warning again.")
        set_expert_mode("true")


def set_expert_mode(expert_mode):
    _update_config("OPENAI_DISABLE_NOTICE", expert_mode)


def get_expert_mode():
    if not os.path.exists(_config_file):
        return None

    with open(_config_file, "r") as f:
        for line in f:
            if line.startswith("OPENAI_DISABLE_NOTICE="):
                return line[len("OPENAI_DISABLE_NOTICE="):].strip()


if os.path.exists('.env'):
    _config_dir = os.path.dirname(os.path.realpath(__file__))
    _config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env")
else:
    _config_dir = appdirs.user_config_dir("aiy-config")
    _config_file = os.path.join(_config_dir, "aiy-config.ini")
