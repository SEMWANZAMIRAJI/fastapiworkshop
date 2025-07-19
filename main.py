from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

@app.get("/about", response_class=HTMLResponse)
def about_me(request: Request):
    context = {
        "request": request,
        "title": "About Me",
        "name": "Miraji Semwanza",
        "profession": "Computer Engineering Student / Software Developer",
        "focus": "Working on FastAPI project for web development",
        "location": "Tanzania",
        "goal": "Learning to build scalable backend APIs with Python FastAPI"
    }
    return templates.TemplateResponse("about.html", context)
