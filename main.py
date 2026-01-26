from fastapi import FastAPI
from _skill import create_poster
from pydantic import BaseModel


app = FastAPI()


class CreatePosterRequest(BaseModel):
    prompt: str


@app.post("/create_poster/")
async def read_root(request: CreatePosterRequest):
    poster = create_poster(prompt=request.prompt)
    return poster
    