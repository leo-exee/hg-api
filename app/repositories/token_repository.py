from app.constants import DB
from app.models.authentification import TokenInDAO, TokenOutDAO


def create_token(token: TokenInDAO) -> TokenOutDAO:
    cursor = DB.cursor()
    cursor.execute(
        """
        INSERT INTO Token (userId, token, dateCreated)
        VALUES (%s, %s, %s)
        """,
        (token.userId, token.token, token.dateCreated),
    )
    cursor.close()
    DB.commit()
    return TokenOutDAO(**token.dict(), id=str(cursor._last_insert_id))
