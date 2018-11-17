import anyconfig
import platform
from pathlib import Path


def get_config_dir():
    system = platform.system()
    if system == "Darwin":
        return Path(".local/share/voctokey")
    raise NotImplementedError


def load_config():
    config_dir = get_config_dir()
    return anyconfig.load(config_dir / "Config.ini")
