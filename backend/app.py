from fastapi import FastAPI, File, HTTPException
from starlette.requests import Request
from search_algos.list_search import List_Search
from search_algos.inverted_index_search import Inverted_Index_Search
import json

with open('movies.json') as json_file:
    links = json.load(json_file)

app = FastAPI()
list_search = List_Search(data=links)
inverted_index_search = Inverted_Index_Search(data=links)

@app.get("/healthcheck")
def index():
    return "Healthy!"

@app.get("/list_search")
def search_response(search_term: str):
    list_search = List_Search(data=links)
    return list_search.search(search_term)

@app.get("/inverted_index_search")
def search_response(search_term: str):
    return inverted_index_search.search(search_term)
