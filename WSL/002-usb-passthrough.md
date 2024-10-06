## How to set USB passthrough

For example use ST-link on wsl Ubunut. Based on https://learn.microsoft.com/en-us/windows/wsl/connect-usb

In short:

1) wsl installed

Host side; powershell:
a) install https://github.com/dorssel/usbipd-win/releases
b) usbipd wsl list
c) wsl --update
d) usbipd wsl attach --busid <busid> (Ubuntu shell needs to be running)

WSL side; terminal:
a) sudo apt install linux-tools-generic hwdata
b) sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/*-generic/usbip 20
c) lsusb (for check)