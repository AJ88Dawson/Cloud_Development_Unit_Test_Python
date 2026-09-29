"""Exercise 3 stretch task - model answers for the TDD repository.

Run with:  pytest solutions

No mocks here. ConcreteUserRepository is the real thing, so these are
ordinary state-based tests. They were written one at a time, each one
failing before the matching line of concrete_user_repository.py existed.
"""

import pytest

from concrete_user_repository import ConcreteUserRepository
from user import User


@pytest.fixture
def repository():
    return ConcreteUserRepository()


@pytest.fixture
def bobby():
    return User(id=1, username="bobby", password="Codes123")


# ---------------------------------------------------------------------------
# exists()
# ---------------------------------------------------------------------------


def test_exists_returns_false_when_the_repository_is_empty(repository):
    # Act
    result = repository.exists("bobby")

    # Assert
    assert result is False


def test_exists_returns_true_after_the_user_is_registered(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act
    result = repository.exists("bobby")

    # Assert
    assert result is True


def test_exists_returns_false_for_a_different_username(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act
    result = repository.exists("alice")

    # Assert
    assert result is False


def test_exists_is_case_sensitive(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act
    result = repository.exists("BOBBY")

    # Assert
    assert result is False


# ---------------------------------------------------------------------------
# register()
# ---------------------------------------------------------------------------


def test_register_returns_the_user_it_was_given(repository, bobby):
    # Act
    result = repository.register(bobby)

    # Assert
    assert result == bobby


def test_register_stores_the_user_in_the_list(repository, bobby):
    # Act
    repository.register(bobby)

    # Assert
    assert repository.users == [bobby]


def test_register_stores_several_different_users(repository, bobby):
    # Arrange
    alice = User(id=2, username="alice", password="Codes456")

    # Act
    repository.register(bobby)
    repository.register(alice)

    # Assert
    assert len(repository.users) == 2


def test_register_raises_value_error_for_a_duplicate_username(repository, bobby):
    # Arrange
    repository.register(bobby)
    duplicate = User(id=2, username="bobby", password="Codes456")

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        repository.register(duplicate)

    assert str(exception_info.value) == "Username already exists"
    assert len(repository.users) == 1


# ---------------------------------------------------------------------------
# login()
# ---------------------------------------------------------------------------


def test_login_returns_the_stored_user_when_the_credentials_match(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act
    result = repository.login(User(id=0, username="bobby", password="Codes123"))

    # Assert
    assert result == bobby


def test_login_raises_value_error_when_the_password_is_wrong(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        repository.login(User(id=0, username="bobby", password="Wrong123"))

    assert str(exception_info.value) == "Invalid username or password"


def test_login_raises_value_error_when_the_username_is_unknown(repository, bobby):
    # Arrange
    repository.register(bobby)

    # Act and Assert
    with pytest.raises(ValueError):
        repository.login(User(id=0, username="alice", password="Codes123"))


def test_login_raises_value_error_when_the_repository_is_empty(repository, bobby):
    with pytest.raises(ValueError):
        repository.login(bobby)
