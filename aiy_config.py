import os
import appdirs

_config_dir = appdirs.user_config_dir("aiy-config")
_config_file = os.path.join(_config_dir, "aiy-config.ini")


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
        os.environ["OPENAI_DISABLE_NOTICE"] = "false"
        print("Expert mode disabled. You will see the warning again.")
        _update_config("OPENAI_DISABLE_NOTICE", "false")
    else:
        os.environ["OPENAI_DISABLE_NOTICE"] = "true"
        print("Expert mode enabled. You will not see the warning again.")
        _update_config("OPENAI_DISABLE_NOTICE", "true")


def get_expert_mode():
    if not os.path.exists(_config_file):
        _update_config("OPENAI_DISABLE_NOTICE", "true") # default to true
        return True

    with open(_config_file, "r") as f:
        for line in f:
            if line.startswith("OPENAI_DISABLE_NOTICE="):
                return line[len("OPENAI_DISABLE_NOTICE="):].strip()

