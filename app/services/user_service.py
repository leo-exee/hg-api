from datetime import datetime, timezone

from app.models.authentification import JWTTokenModelInDTO, TokenInDAO
from app.models.user import AuthUserOutDTO, UserInDAO
from app.repositories.token_repository import create_token
from app.repositories.user_repository import create_user
from app.utils.token_utils import encode_token


def register_user_service(user: UserInDAO) -> AuthUserOutDTO:
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
    return AuthUserOutDTO(**new_user.dict(), token=token)
