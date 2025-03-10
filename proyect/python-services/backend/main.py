
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR / "assets")), name="static")

@app.get("/")
async def serve_index():

    index_path = FRONTEND_DIR / "index.html"
    return FileResponse(index_path)
