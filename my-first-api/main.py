from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
import json
from pathlib import Path


app = FastAPI(
    title="Angewandte Programmierung",
    despription="Notizenmanagement"
    )

@app.get("/")
def root():
    return {"message": "Hello, Andreas Moritz!"}

@app.get("/status")
def get_status():
    return{
        "status": "online",
        "version": "0.1.0",
        "day": 1
    }

@app.get("/about")
def get_about():
    return {
        "project": "My First API",
        "author": "Andreas",
        "course": "Applied Programming"
    }

@app.get("/square/{number}")
def square(number: int):
    square_result = number **2
    return {"number": number, 
            "square": square_result, 
            "calculation": f"{number} x {number} = {square_result}"
            }

@app.get("/student")
def get_student():
    return {
        "name": "Andreas",
        "semster": 2,
        "course": "Wirtschaftsinformatik 2.0",
        "university": "Hochschule Coburg"
    }

@app.get("/double/{number}")
def double(number: int):
    doppelt= number*2
    return {
        "number": number,
        "double": doppelt,
        "calculation": f"{number} x 2 = {doppelt}"
        }