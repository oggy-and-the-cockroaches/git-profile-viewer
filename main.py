from fastapi import FastAPI
import requests
import json

app = FastAPI()
@app.get("/get_username")
def get_username(username):
    url = f"https://api.github.com/users/{username}"
    global response 
    response = requests.get(url)
    return response.ok

@app.get("/get_repos_url")
def get_repos_url(user):
    get_username(user)
    return response.json()["repos_url"]