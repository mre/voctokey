import anyconfig
import toml
import platform
from pathlib import Path
import os
import appdirs


def get_config_dir():
    return Path(appdirs.user_data_dir("voctokey", "mre"))


def load_config():
    config_dir = get_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    return anyconfig.load(config_dir / "Config.toml")
