from datetime import datetime, timezone

from app.models.authentification import JWTTokenModelInDTO, TokenInDAO
from app.models.user import AuthenticatedUserOutDTO, UserInDAO
from app.repositories.token_repository import create_token
from app.repositories.user_repository import create_user, get_user_by_email
from app.utils.token_utils import encode_token
from app.utils.user_utils import get_password_hash


def register_user_service(user: UserInDAO) -> AuthenticatedUserOutDTO:
    user.password = get_password_hash(user.password)
    new_user = create_user(user)
    token = encode_token(
        JWTTokenModelInDTO(
            userId=new_user.id, isAdmin=False, dateCreated=datetime.now(timezone.utc)
        )
    )
    create_token(
        TokenInDAO(
            userId=new_user.id,
            token=token,
            dateCreated=datetime.now(timezone.utc),
        )
    )
    return AuthenticatedUserOutDTO(**new_user.dict(), token=token)


def login_user_service(email: str, password: str) -> AuthenticatedUserOutDTO:
    test = get_user_by_email(email)
    return AuthenticatedUserOutDTO(id="1", username="test", email="test", token="test")
