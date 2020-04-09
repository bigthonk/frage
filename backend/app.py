from fastapi import FastAPI, File, HTTPException
from starlette.requests import Request
from search import Search
import json

link1 = {
    "url":"https://cvs.com",
    "title":"cvs",
    "about":"Local health spot",
    "tags":"cvs, drugstore, cvs health"
}

link2 = {
    "url":"https://reddit.com",
    "title":"reddit",
    "about":"Front page of the internet",
    "tags":"liberal content, memes"
}

links = [link1,link2]

with open('movies.json') as json_file:
    links = json.load(json_file)

app = FastAPI()
search = Search(links=links)

@app.get("/healthcheck")
def index():
    return "Healthy!"

@app.get("/list_search")
def search_response(search_term: str):
    return search.list_search(search_term)

@app.get("/inverted_index_search")
def search_response(search_term: str):
    return search.inverted_index_search(search_term)
