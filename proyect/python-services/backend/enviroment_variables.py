"""This module is responsible for loading enviroment variables
for the CanastaeSchedule project.

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

#pylint: disable=too-few-public-methods

class EnviromentVariables:
    """
    Manages environment variables for data file paths.
    """

    def __init__(self):
        """Initializes environment variables for data storage paths.

        Attributes:
            path_users_data (str | None): Path to the routes data file.
        """

        self.path_users_data = os.getenv("PATH_USERS_DATA")
