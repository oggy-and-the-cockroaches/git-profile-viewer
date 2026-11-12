from fastapi import FastAPI
import requests
import json

app = FastAPI()
@app.get("/get_username")
def get_username(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.ok

