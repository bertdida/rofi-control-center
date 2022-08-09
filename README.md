# Rofi Control Center Plugin

Search Control Center/System Settings on GNOME based distro using [rofi](https://github.com/davatorium/rofi).

![rofi control center screenshot 1](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/01.png)

![rofi control center screenshot 2](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/02.png)

![rofi control center screenshot 3](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/03.png)

## Installation

1. Download the script

```bash
sudo wget https://raw.githubusercontent.com/bertdida/rofi-control-center/main/rofi-control-center.py -P ~/.local/bin/
```

2. ...make it executable.

```bash
sudo chmod +x ~/.local/bin/rofi-control-center.py
```

3. Launch using rofi command
```bash
rofi -modi "settings:~/.local/bin/rofi-control-center.py" -show settings -show-icons
```
or edit your rofi config to load the script automatically.
```css
configuration {
  modi: "drun,settings:~/.local/bin/rofi-control-center.py";
}
```
