"""This module handles the loading of environment variables for the application.

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

import os
from dotenv import load_dotenv

DOTENV_PATH = "/app/backend/.env"
load_dotenv(DOTENV_PATH)

# pylint: disable=too-few-public-methods

class EnviromentVariables:
    """Class for loading and storing environment variables."""

    def __init__(self):
        """Initializes environment variables from the .env file."""
        self.path_users_data = os.getenv("PATH_USERS_DATA")
        self.jwt_secret_key = os.getenv("JWT_SECRET_KEY")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM")
        self.expire_minutes = os.getenv("JWT_EXPIRE_MINUTES")
