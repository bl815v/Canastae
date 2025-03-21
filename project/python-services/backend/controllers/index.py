"""This module is used to handle API endpoints related to
index page.

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
from fastapi.responses import FileResponse
from fastapi import APIRouter

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent.parent / "frontend"

@router.get("/")
def index_page() -> FileResponse:
    """Serves the index page of the frontend.

    Returns:
        FileResponse: The response containing the index.html file.
    """
    index_path = FRONTEND_DIR / "index.html"
    return FileResponse(index_path)
