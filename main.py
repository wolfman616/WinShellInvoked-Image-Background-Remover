import sys
import requests
import os

input_file = sys.argv[1]
print('.', input_file)

output_file = input_file.split('.')[0] + '-nobg.png'

path = os.getcwd()

if os.path.isfile(f'{path}\\{output_file}'):
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
