import sys
import requests
import os
import ctypes
import winreg

# Set DPI awareness to "per monitor v2"
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except AttributeError:
    pass  # Not available on this version of Windows

input_file = sys.argv[1]
print('.', input_file)

output_file = input_file.split('.')[0] + '-nobg.png'

path = os.getcwd()

if os.path.isfile(f'{path}\\{output_file}'):
    print(f'ERROR: {output_file} File already exists.')
else:
    filetype = input_file.split('.')[-1]

try:
    # Read the API key from the Windows Registry
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\_MW\clipdrop")
    api_key, _ = winreg.QueryValueEx(registry_key, "ApiKey")
    winreg.CloseKey(registry_key)
except FileNotFoundError:
    api_key = "API_KEY_NOT_FOUND"  # Set a default value if the Registry key doesn't exist

r = requests.post('https://clipdrop-api.co/remove-background/v1',
    files={
        'image_file': (
            input_file, open(f'{input_file}', 'rb'), f'image/{filetype}'
        )
    },
    headers={'x-api-key': api_key}
)

if r.ok:
    with open(f'{output_file.replace(filetype, "png")}', 'wb') as f:
        f.write(r.content)
    print(f'Removed background from {input_file} and saved as {output_file}')
else:
    r.raise_for_status()
    print(f'ERROR: Could not remove background from {input_file}')
