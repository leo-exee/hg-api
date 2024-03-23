from datetime import datetime, timezone

from app.models.authentification import JWTTokenModelInDTO
from app.models.user import AuthUserOutDTO, UserInDAO
from app.repositories.user_repository import create_user
from app.utils.token_utils import encode_token


async def register_user_service(user: UserInDAO) -> AuthUserOutDTO:
    id = "1"
    new_user = await create_user(user)
    token = encode_token(
        JWTTokenModelInDTO(
            userId=id, isAdmin=False, dateCreated=datetime.now(timezone.utc)
        )
    )

    return AuthUserOutDTO(**user.dict(), id=id, token=token)
