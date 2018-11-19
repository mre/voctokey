# voctokey

Control [voctomix] via keyboard shortcuts.  
It connects to the [TCP server of voctocore](https://github.com/voc/voctomix/tree/master/voctocore#example-communication).
It can run as a daemon and listen for keyboard inputs in the background.
Should work cross-platform on Linux/Windows/macOS.

## Requirements

On macOS, you have to [allow the app to control the computer](https://www.mactrast.com/2017/05/enable-app-accessibility-features-mac/).

## Installation

```
pip install voctokey
```

## Configuration

`voctokey` can be configured dynamically with a config file.  

The path to the config file is as follows (see [docs](https://github.com/ActiveState/appdirs)):

* Linux: `/home/username/.local/share/voctokey/Config.toml`
* macOS: `/Users/username/Library/Application Support/voctokey/Config.toml`
* Windows: `C:\\Users\\username\\AppData\\Local\\mre\\voctokey/Config.toml`

Here is a sample config:

```toml
[server]
ip = "127.0.0.1"
port = "9999"

[hotkeys]
"command+h" = "help"
"command+j"= "set_video_a cam1"
"command+k"= "set_composite_mode side_by_side_equal"
"command+l"= "get_video"
```

The server config is pointing to the voctocore TCP server.  
See the [`keyboard` documentation](https://github.com/boppreh/keyboard) for a list of hotkeys.
The commands are sent verbatim over the wire and the result is printed to `stdout`.

## Development

Run `make help` to see the available commands.


[voctomix]: https://github.com/voc/voctomix

