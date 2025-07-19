from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/about")
def about_me():
    return {
        "name": "Miraji Semwanza",
        "profession": "Computer Engineering Student / Software Developer",
        "focus": "Working on FastAPI project for web development",
        "location": "Tanzania",
        "goal": "Learning to build scalable backend APIs with Python FastAPI"
    }
