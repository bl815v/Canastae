
from pathlib import Path
from fastapi import APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from backend.services.user_auth import AuthService # pylint: disable=import-error

router = APIRouter()

LOGIN_TEMPLATE = Path(__file__).resolve().parent.parent.parent / "frontend" / "templates" / "login.html"

@router.get("/login", response_class=HTMLResponse)
async def login_page():

    return HTMLResponse(content=LOGIN_TEMPLATE.read_text(), status_code=200)

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    auth_service: AuthService = Depends()
):

    if auth_service.authenticate_user(username, password):
        return RedirectResponse(url="/", status_code=303)
    return RedirectResponse(url="/login?error=invalid_credentials", status_code=303)
