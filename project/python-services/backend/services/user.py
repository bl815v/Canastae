"""This module defines services for handling user data.

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

from typing import List
from backend.repositories.users.user import UserRepository, UserDAO #pylint: disable=import-error

class UserServices:
    """Provides services for searching user data."""

    def __init__(self):
        """Initializes the service with a user repository."""
        self.repository = UserRepository()

    def get_all(self) -> List[UserDAO]:
        """Retrieves all users.
        
        Returns:
            List[UserDAO]: A list of all users.
        """
        return self.repository.get_users()

    def get_by_id(self, user_id: int) -> list[UserDAO]:
        """Retrieves users that match a given id.
        Args:
            user_id (int): The id of the user to search for.

        Returns:
            list[UserDAO]: The user that matches the given id.
        """
        response = []
        for user in self.repository.get_users():
            if user.user_id == user_id:
                response.append(user)
        return response
