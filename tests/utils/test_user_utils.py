import pytest

from app.utils.user_utils import get_password_hash, verify_password


@pytest.fixture(scope="module")
def passwords() -> list[dict]:
    return [
        {"plain": "valid", "hashed": get_password_hash("valid")},
        {"plain": "valid", "hashed": get_password_hash("invalid")},
    ]


@pytest.mark.parametrize(
    ("index", "expected"),
    [
        (0, True),
        (1, False),
    ],
)
def test_verify_password(index: int, expected: bool, passwords: list[dict]):
    assert (
        verify_password(passwords[index]["plain"], passwords[index]["hashed"])
        == expected
    )
