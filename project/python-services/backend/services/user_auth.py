"""This module provides authentication services for user verification.

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

from backend.repositories.users.user import UserRepository

class AuthService:
    """Service class for handling user authentication."""

    def __init__(self):
        """Initializes the authentication service with a user repository."""
        self.user_repo = UserRepository()

    def authenticate_user(self, username: str, password: str) -> str | None:
        """Authenticates a user by checking the provided credentials.

        Args:
            username (str): The username of the user attempting to log in.
            password (str): The password associated with the username.

        Returns:
            str | None: The username if authentication is successful, otherwise None.
        """
        users = self.user_repo.get_users()
        for user in users:
            if user.username == username and user.password == password:
                return username
        return None
