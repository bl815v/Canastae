"""This module provides utility functions for handling JWT authentication.

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

from datetime import datetime, timedelta
from jose import jwt
from backend.enviroment_variables import EnviromentVariables  # pylint: disable=import-error

env = EnviromentVariables()

SECRET_KEY = env.jwt_secret_key
ALGORITHM = env.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = int(env.expire_minutes)

def create_access_token(data: dict) -> str:
    """Generates a JWT access token.

    Args:
        data (dict): The payload to encode in the token.

    Returns:
        str: The generated JWT token.
    """
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    """Decodes a JWT token.

    Args:
        token (str): The JWT token to decode.

    Returns:
        dict: The decoded payload.

    Raises:
        JWTError: If the token is invalid or expired.
    """
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
