"""This module is used to handle data related to user data.

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

from pydantic import BaseModel
from backend.enviroment_variables import EnviromentVariables #pylint: disable=import-error
from backend.repositories.base_repository import BaseRepository #pylint: disable=import-error

class UserDAO(BaseModel):
    """Data Access Object for user data."""
    user_id: int
    username: str
    password: str

class UserRepository(BaseRepository):
    """Repository for managing user data."""

    def __init__(self):
        """Initializes the repository and loads user data."""
        env = EnviromentVariables()
        super().__init__(env.path_users_data)

    def _extract_data(self, data: dict) -> list[dict]:
        """Extracts user data from the provided dictionary.

        Args:
            data (dict): The raw data containing user information.

        Returns:
            list[dict]: A list of dictionaries representing users.
        """
        return data.get("users", [])

    def get_users(self) -> list[UserDAO]:
        """Gets all users.

        Returns:
            list[UserDAO]: A list of user objects.
        """
        users = []
        for user in self.data:
            user_temp = UserDAO(
                user_id = user["id"],
                username = user["username"],
                password = user["password"]
            )
            users.append(user_temp)
        return users
