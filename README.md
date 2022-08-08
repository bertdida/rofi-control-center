# Rofi Control Center Plugin (Fedora)

Search Control Center/System Settings on Fedora distro using [rofi](https://github.com/davatorium/rofi).

![rofi control center screenshot 1](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/01.png)

![rofi control center screenshot 2](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/02.png)

![rofi control center screenshot 3](https://raw.githubusercontent.com/bertdida/rofi-control-center/main/screenshots/03.png)

## Installation

1. Download the script

```bash
sudo wget https://raw.githubusercontent.com/bertdida/rofi-control-center/main/rofi-control-center.py -P ~/.local/bin/
```

2. ...then make it executable.

```bash
chmod +x ~/.local/bin/rofi-control-center.py
```

2. Update rofi's modi config to load the script.

```css
configuration {
  modi: "drun,settings:~/.local/bin/rofi-control-center.py";
}
```
