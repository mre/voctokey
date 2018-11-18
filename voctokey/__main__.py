import keyboard
import anyconfig
import sys

from voctokey.config import load_config
from voctokey.tcp import TcpClient


def get_config():
    try:
        return load_config()
    except NotImplementedError as e:
        print("Platform not supported yet:", e)
        sys.exit(1)


def try_send(client, command):
    """
    Try to send a msessage via TCP and prints a human readable message
    """
    try:
        client.send(command.encode('ascii'))
    except Exception as e:
        print(e)


def main():
    config = get_config()
    print(config)

    # Print all inputs. Good for debugging
    keyboard.hook(print)

    print(config["hotkeys"])
    client = TcpClient(config["server"]["ip"], config["server"]["port"])
    for hotkey, command in config["hotkeys"].items():
        keyboard.add_hotkey(hotkey, try_send, args=(client, command))
    keyboard.wait()


if __name__ == '__main__':
    main()
