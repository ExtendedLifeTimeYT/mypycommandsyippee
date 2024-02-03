import requests
import os
import webbrowser

location = f"{os.getcwd()}\\version"

url = 'https://raw.githubusercontent.com/ExtendedLifeTimeYT/mypycommandsyippee/main/version'

response = requests.get(url)

if response.status_code == 200:
    if os.read(location) == response.text:
        print("Up to date")
    else:
        webbrowser.open(url=url)
else:
    print(f"Error {response.status_code}: Unable to retrieve content from {url}")

input("close wit entar")