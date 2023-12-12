from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/register_page")
def reg_page():
    return FileResponse("register.html")

@app.post("/register")
def registration(data=Body()):
    login = data["username"]
    password = data["userpass"]
    #if len(login)>=3 and len(password)>=6:
    #    return {"register_response": "okay"}
    #else:
    #    return {"register_response": "wrong login or password"}
    return {"reg-response": "okay"}

@app.post("/login")
def login():
    return {"register_response": "okay"}
