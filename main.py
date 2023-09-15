import sys
import requests
import os
import ctypes

# Set DPI awareness to "per monitor v2"
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except AttributeError:
    pass  # Not available on this version of Windows

input_file = sys.argv[1]
print('.', input_file)

output_file = input_file.split('.')[0] + '-nobg.png'

path = os.getcwd()

if os.path.isfile(f'{output_file}'):
    print(f'ERROR: {output_file} File already exists.')
else:
    filetype = input_file.split('.')[-1]

r = requests.post('https://clipdrop-api.co/remove-background/v1',
files={
    'image_file': (
        input_file, open(f'{input_file}', 'rb'), f'image/{filetype}'
    )
},
headers={'x-api-key': open(f"{path}\\YOUR_API_KEY.txt", 'r+').read().strip()}
)
if r.ok:
    with open(f'{output_file.replace(filetype, "png")}', 'wb') as f:
        f.write(r.content)
    print(f'Removed background from {input_file} and saved as {output_file}')
else:
    r.raise_for_status()
    print(f'ERROR: Could not remove background from {input_file}')

    # Create a message box
    import ctypes

    # Define constants for MessageBoxW
    MB_ICONINFORMATION = 0x00000040
    MB_OK = 0x00000000
    MB_TIMEOUT = 0x00000200  # Indicates a timeout will be used

    # Call the MessageBoxW function
    user32 = ctypes.windll.user32
    user32.MessageBoxW(None, "Could not remove background from {input_file}", "ERROR",  MB_ICONWARNING | MB_OK | MB_TIMEOUT, 0, 5000)
