"""This module is used to handle the different routers of the app.

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

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .controllers import index_router, user_router, user_auth_router

app = FastAPI(
    title="CanastaeSchedule",
    version="0.1.0"
)

app.mount("/static", StaticFiles(directory="/app/frontend/assets"), name="static")

app.include_router(index_router)
app.include_router(user_router)
app.include_router(user_auth_router)
