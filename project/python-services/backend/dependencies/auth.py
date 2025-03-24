"""This module provides authentication utilities for handling user authentication
through JWT tokens stored in cookies.

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

from fastapi import HTTPException, Cookie
from fastapi.security import OAuth2PasswordBearer
from backend.utils.jwt_handler import decode_token #pylint: disable=import-error

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(access_token: str = Cookie(None)) -> str:
    """Retrieves the current authenticated user based on the provided access token.

    Args:
        access_token (str): The JWT access token stored in a cookie.

    Returns:
        str: The username of the authenticated user.

    Raises:
        HTTPException: If no access token is provided.
        HTTPException: If the token is invalid or does not contain a username.
    """
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = decode_token(access_token)
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid token.") from exc
