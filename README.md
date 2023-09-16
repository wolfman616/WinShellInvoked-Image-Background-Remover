# ShellInvoked Image Background Remover

This Python program uses the ClipDrop API to remove the background from images from the shell.
To use the ClipDrop API, you will need to obtain an API key from the [ClipDrop website](https://clipdrop.co/apis/account), add the key to the following key: Computer\HKEY_CURRENT_USER\Software\_MW\clipdrop. add txt string with name apikey.



## Requirements
- AHK v1
- [Python 3](https://www.python.org/downloads/)
- [requests library](https://pypi.org/project/requests/) (`pip install requests`)

## Usage

1. Clone this repository or download the source code.
2. Obtain an API key from the [ClipDrop website](https://clipdrop.co/apis/account) and place it in "API_KEY.reg".
3. pass argument to ahk script from shell. Or load the reg file "example_menuentry.reg"

![image](https://github.com/wolfman616/WinShellInvoked-Image-Background-Remover/assets/62726599/2d650ef1-bb0b-4f37-a9f3-17960ac49568)
<img width="727" alt="Clipboarder 2023 09 16-018" src="https://github.com/wolfman616/WinShellInvoked-Image-Background-Remover/assets/62726599/ef37f8d4-2d83-40b2-9668-da3823236042">
Note the ahk python loader script location must match in the registry command.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
