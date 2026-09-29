"""Exercise 3 - model answers, with the repository mocked.

Run with:  pytest solutions

Mockito does not exist in Python. unittest.mock from the standard library
does the same job, so MagicMock replaces @Mock and passing the mock to the
constructor replaces @InjectMocks.
"""

from unittest.mock import MagicMock

import pytest

from user import User
from user_controller import UserController


@pytest.fixture
def repository():
    """The mocked UserRepository."""
    return MagicMock()


@pytest.fixture
def controller(repository):
    """The controller under test, with the mock injected."""
    return UserController(repository)


@pytest.fixture
def valid_user():
    return User(id=1, username="bobby", password="Codes123")


# ---------------------------------------------------------------------------
# register()
# ---------------------------------------------------------------------------


def test_register_saves_a_valid_user_through_the_repository(controller, repository, valid_user):
    # Arrange
    repository.exists.return_value = False
    repository.register.return_value = valid_user

    # Act
    result = controller.register(valid_user)

    # Assert
    assert result == valid_user
    repository.exists.assert_called_once_with("bobby")
    repository.register.assert_called_once_with(valid_user)


def test_register_passes_the_trimmed_username_to_exists(controller, repository):
    # Arrange - the controller trims before the uniqueness check even
    # though it stores the untrimmed user.
    user = User(id=1, username="  bobby  ", password="Codes123")
    repository.exists.return_value = False
    repository.register.return_value = user

    # Act
    controller.register(user)

    # Assert
    repository.exists.assert_called_once_with("bobby")


def test_register_raises_value_error_when_the_user_is_none(controller, repository):
    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        controller.register(None)

    assert str(exception_info.value) == "User must not be null"
    repository.exists.assert_not_called()


def test_register_raises_value_error_when_the_username_is_none(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username=None, password="Codes123"))

    assert str(exception_info.value) == "Username must not be null"
    repository.exists.assert_not_called()


def test_register_raises_value_error_when_the_username_is_whitespace_only(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="   ", password="Codes123"))

    assert str(exception_info.value) == "Username must not be whitespace only"


def test_register_raises_value_error_when_the_password_is_none(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password=None))

    assert str(exception_info.value) == "Password must not be null"


def test_register_raises_value_error_when_the_password_is_whitespace_only(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="   "))

    assert str(exception_info.value) == "Password must not be whitespace only"


def test_register_raises_value_error_when_the_username_is_too_short(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bob", password="Codes123"))

    assert str(exception_info.value) == "Username must contain at least 4 characters"
    repository.exists.assert_not_called()


def test_register_raises_value_error_when_the_repository_says_the_username_exists(
    controller, repository, valid_user
):
    """The exception that is new in exercise 3, and the reason we mock."""
    # Arrange
    repository.exists.return_value = True

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        controller.register(valid_user)

    assert str(exception_info.value) == "Username already exists"
    repository.register.assert_not_called()


def test_register_raises_value_error_when_the_password_is_too_short(controller, repository):
    # Arrange
    repository.exists.return_value = False

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="Cod1e"))

    assert str(exception_info.value) == "Password must contain at least 6 characters"
    repository.register.assert_not_called()


def test_register_raises_value_error_when_the_password_has_no_uppercase(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="codes123"))

    assert str(exception_info.value) == "Password must contain at least 1 uppercase character"


def test_register_raises_value_error_when_the_password_has_no_lowercase(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="CODES123"))

    assert str(exception_info.value) == "Password must contain at least 1 lowercase character"


def test_register_raises_value_error_when_the_password_has_no_number(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        # Six characters with no digit. The guide's "Codes" is only five
        # characters and would trip the length rule first.
        controller.register(User(id=1, username="bobby", password="Codess"))

    assert str(exception_info.value) == "Password must contain at least 1 number character"


def test_register_accepts_a_password_whose_only_digit_is_zero(controller, repository):
    """The fixed password rules reach the controller too, because both
    classes share the same patterns. "Codes0" satisfies every stated rule,
    so it must be accepted. See CODE_CORRECTIONS.md."""
    # Arrange
    user = User(id=1, username="bobby", password="Codes0")
    repository.exists.return_value = False
    repository.register.return_value = user

    # Act
    result = controller.register(user)

    # Assert
    assert result == user
    repository.register.assert_called_once_with(user)


def test_register_accepts_a_password_containing_a_symbol(controller, repository):
    """No stated rule forbids a symbol, so one must not be rejected."""
    # Arrange
    user = User(id=1, username="bobby", password="Cod|es1")
    repository.exists.return_value = False
    repository.register.return_value = user

    # Act
    result = controller.register(user)

    # Assert
    assert result == user
    repository.register.assert_called_once_with(user)


def test_register_names_the_uppercase_rule_when_only_uppercase_is_missing(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="codes1"))

    assert str(exception_info.value) == "Password must contain at least 1 uppercase character"
    repository.register.assert_not_called()


def test_register_names_the_lowercase_rule_when_only_lowercase_is_missing(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="CODES1"))

    assert str(exception_info.value) == "Password must contain at least 1 lowercase character"


def test_register_names_the_number_rule_when_only_a_number_is_missing(controller, repository):
    repository.exists.return_value = False

    with pytest.raises(ValueError) as exception_info:
        controller.register(User(id=1, username="bobby", password="Codesss"))

    assert str(exception_info.value) == "Password must contain at least 1 number character"


# ---------------------------------------------------------------------------
# login()
# ---------------------------------------------------------------------------


def test_login_returns_the_user_the_repository_gives_back(controller, repository, valid_user):
    # Arrange
    repository.login.return_value = valid_user

    # Act
    result = controller.login(valid_user)

    # Assert
    assert result == valid_user
    repository.login.assert_called_once_with(valid_user)


def test_login_lets_a_repository_error_propagate(controller, repository, valid_user):
    """side_effect is how you make a mock raise instead of return."""
    # Arrange
    repository.login.side_effect = ValueError("Invalid username or password")

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        controller.login(valid_user)

    assert str(exception_info.value) == "Invalid username or password"


def test_login_raises_value_error_when_the_user_is_none(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.login(None)

    assert str(exception_info.value) == "User must not be null"
    repository.login.assert_not_called()


def test_login_raises_value_error_when_the_username_is_none(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.login(User(id=1, username=None, password="Codes123"))

    assert str(exception_info.value) == "Username and password must not be null"
    repository.login.assert_not_called()


def test_login_raises_value_error_when_the_password_is_none(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.login(User(id=1, username="bobby", password=None))

    assert str(exception_info.value) == "Username and password must not be null"


def test_login_raises_value_error_when_the_username_is_empty(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.login(User(id=1, username="", password="Codes123"))

    assert str(exception_info.value) == "Username and password must not be empty"


def test_login_raises_value_error_when_the_password_is_empty(controller, repository):
    with pytest.raises(ValueError) as exception_info:
        controller.login(User(id=1, username="bobby", password=""))

    assert str(exception_info.value) == "Username and password must not be empty"


def test_login_passes_a_whitespace_only_username_straight_to_the_repository(
    controller, repository
):
    """Faithful to the Java original, which calls isEmpty() without
    trimming in login(), unlike register()."""
    # Arrange
    user = User(id=1, username="   ", password="Codes123")
    repository.login.return_value = user

    # Act
    result = controller.login(user)

    # Assert
    assert result == user
    repository.login.assert_called_once_with(user)
