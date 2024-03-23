from app.constants import DB
from app.models.user import UserInDAO, UserOutDAO


async def create_user(user: UserInDAO) -> UserOutDAO:
    cursor = DB.cursor()
    cursor.execute(
        f"INSERT INTO User (username, email, password, dateCreated, lastModified) VALUES ('{user.username}', '{user.email}', '{user.password}', '{user.dateCreated}', '{user.dateCreated}')"
    )
    DB.commit()
    return UserOutDAO(
        **user.dict(), id=str(cursor._last_insert_id), lastModified=user.dateCreated
    )
