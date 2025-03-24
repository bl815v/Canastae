"""This module handles authentication-related API endpoints, including
login, logout, and access to the main page.

Author: Juan Esteban Bedoya <jebedoyal@udistrital.edu.co>

This file is part of CanastaeSchedule project.

CanastaeSchedule is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

CanastaeSchedule is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with CanastaeSchedule. If not, see <https://www.gnu.org/licenses/>. 
"""

from pathlib import Path
from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from backend.services.user_auth import AuthService
from backend.utils.jwt_handler import create_access_token
from backend.dependencies.auth import get_current_user
from backend.config.templates import templates

router = APIRouter()

# Define paths for login and home templates
LOGIN_TEMPLATE = Path(__file__).resolve().parent.parent.parent / "frontend" \
                / "templates" / "login.html"
INICIO_TEMPLATE = Path(__file__).resolve().parent.parent.parent / "frontend" \
                / "templates" / "inicio.html"

@router.get("/login", response_class=HTMLResponse)
async def login_page() -> HTMLResponse:
    """Serves the login page.
    
    Returns:
        HTMLResponse: The response containing the login page content.
    """
    return HTMLResponse(content=LOGIN_TEMPLATE.read_text())

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    auth_service: AuthService = Depends()
):
    """Handles user login, authenticates credentials, and sets an access token.
    
    Args:
        username (str): The username submitted via form.
        password (str): The password submitted via form.
        auth_service (AuthService): Dependency for authentication service.
    
    Returns:
        RedirectResponse: Redirects to the home page if authentication is successful.
    
    Raises:
        HTTPException: If credentials are invalid.
    """
    authenticated_user = auth_service.authenticate_user(username, password)
    if authenticated_user:
        token = create_access_token(data={"sub": authenticated_user})
        response = RedirectResponse(url="/inicio", status_code=303)
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            secure=False,
            samesite="Lax"
        )
        return response
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/inicio", response_class=HTMLResponse)
async def inicio_page(
    request: Request, current_user: str = Depends(get_current_user)
    ) -> HTMLResponse:
    """Serves the main page for authenticated users.
    
    Args:
        request (Request): The incoming request.
        current_user (str): The username of the authenticated user.
    
    Returns:
        HTMLResponse: The response containing the main page content.
    """
    return templates.TemplateResponse(
        "inicio.html",
        {
            "request": request,
            "username": current_user
        }
    )

@router.get("/logout")
async def logout() -> RedirectResponse:
    """Logs out the user by removing the access token cookie.
    
    Returns:
        RedirectResponse: Redirects to the login page.
    """
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(key="access_token")
    return response
