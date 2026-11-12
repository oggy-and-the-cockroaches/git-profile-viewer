import requests

response = requests.get("http://127.0.0.1:8000/")
print(response)
print(response.status_code)
print(response.reason)
print(response.url)
print(response.text)
print(response.headers)
print(response.cookies)
print(response.elapsed)
print(response.ok)
print(type(response))
print(dir(response))