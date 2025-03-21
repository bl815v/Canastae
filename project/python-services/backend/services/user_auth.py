
from backend.repositories.users.user import UserRepository # pylint: disable=import-error

class AuthService:

    def __init__(self):

        self.user_repo = UserRepository()

    def authenticate_user(self, username: str, password: str) -> bool:
    
        users = self.user_repo.get_users()
        return any(user.username == username and user.password == password for user in users)
