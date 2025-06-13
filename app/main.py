from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import threading
import os

from app.login import tianyi_login
from app.strm_generator import generate_strm
from app.proxy import stream_from_tianyi

management_app = FastAPI()
management_app.mount("/static", StaticFiles(directory="app/static"), name="static")
management_app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@management_app.get("/", response_class=HTMLResponse)
def login_page():
    return open("app/templates/login.html", encoding="utf-8").read()

@management_app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    os.makedirs("app/data", exist_ok=True)
    success = tianyi_login(username, password, "app/data/session.json")
    return RedirectResponse("/", status_code=302)

@management_app.post("/add_links")
async def add_links(request: Request):
    form = await request.form()
    links = form.get("links", "").splitlines()
    generate_strm(links)
    return RedirectResponse("/", status_code=302)

proxy_app = FastAPI()

@proxy_app.get("/user/cloud_file")
async def proxy_video(share_id: str, file_id: str):
    return await stream_from_tianyi(share_id, file_id)

def start_management():
    uvicorn.run(management_app, host="0.0.0.0", port=8000)

def start_proxy():
    uvicorn.run(proxy_app, host="0.0.0.0", port=8060)

if __name__ == "__main__":
    threading.Thread(target=start_management).start()
    threading.Thread(target=start_proxy).start()