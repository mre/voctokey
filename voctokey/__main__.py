import keyboard
import anyconfig
import sys

from voctokey.config import load_config


def get_config():
    try:
        return load_config()
    except NotImplementedError as e:
        print("Platform not supported yet:", e)
        sys.exit(1)


def main():
    config = get_config()
    print(config)

    # Print all inputs. Good for debugging
    keyboard.hook(print)

    keyboard.add_hotkey(config["hotkeys"]["camera1"],
                        print, args=('camera', '1'))
    keyboard.add_hotkey(config["hotkeys"]["camera2"],
                        print, args=('camera', '2'))
    keyboard.add_hotkey(config["hotkeys"]["camera3"],
                        print, args=('camera', '3'))
    keyboard.add_hotkey(config["hotkeys"]["camera4"],
                        print, args=('camera', '4'))
    keyboard.wait()


if __name__ == '__main__':
    main()
