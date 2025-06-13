from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
from dotenv import load_dotenv
import os
import json

app = FastAPI()

templates = Jinja2Templates(directory="template")

@app.get("/")
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post("/Get Answer")
async def get_answer(request: Request, questions: str=Form(...)):
    pass



