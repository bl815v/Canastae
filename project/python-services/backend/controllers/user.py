"""This module is used to handle API endpoints related to
user data.

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
from fastapi import APIRouter, HTTPException
from backend.services.user import UserServices
from backend.repositories.users.user import UserDAO

router = APIRouter()

services = UserServices()

@router.get("/user/all")
def get_all() -> List[UserDAO]:
    """Retrieves all users.

    Returns:
        List[UserDAO]: A list of all users.
    """
    return services.get_all()

@router.get("/user/by_id/{user_id}")
def get_by_id(user_id: int) -> list[UserDAO]:
    """Retrieves users that match a given id.
    
    Args:
        user_id (int): The id of the user to search for.

    Returns:
        list[UserDAO]: The user that matches the given id.
    
    Raises:
        HTTPException: If no user is found with the given id.
    """
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found")
    return services.get_by_id(user_id)
