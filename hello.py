import requests

response = requests.get("https://github.com/7amyxl")
print(response.status_code)