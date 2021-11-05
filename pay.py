import requests

url = 'http://localhost:5000/manage_file'
headers = dict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "action": "download"
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.content)