from app.constants import DB
from app.models.user import UserInDAO, UserOutDAO


def create_user(user: UserInDAO) -> UserOutDAO:
    cursor = DB.cursor()
    cursor.execute(
        """
        INSERT INTO User (username, email, password, dateCreated, lastModified)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (user.username, user.email, user.password, user.dateCreated, user.dateCreated),
    )
    cursor.close()
    DB.commit()
    return UserOutDAO(
        **user.dict(), id=str(cursor._last_insert_id), lastModified=user.dateCreated
    )


def get_user_by_email(email: str) -> UserOutDAO | None:
    cursor = DB.cursor()
    cursor.execute(
        """
        SELECT * FROM User WHERE email = %s
        """,
        (email,),
    )
    user = cursor.fetchone()
    cursor.close()

    print(user)

    return None
