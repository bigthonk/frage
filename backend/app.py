from fastapi import FastAPI, File, HTTPException
from starlette.requests import Request
from search import search

app = FastAPI()

@app.get("/healthcheck")
def index():
    return "Healthy!"

@app.get("/search")
def search_response(search_term: str):
    return search(search_term)
