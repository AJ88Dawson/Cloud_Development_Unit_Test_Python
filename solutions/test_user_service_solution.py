"""Exercise 2 - model answers.

Run with:  pytest solutions

Every test in this file passes. Two defects carried over from the Java
original have now been fixed in `src/user_service.py`: login() looked the
user up by password, and the password character rules used a whole-string
match against a broken character class. The tests below assert the corrected
behaviour, including the cases that used to be impossible. See
CODE_CORRECTIONS.md for what changed and why.
"""

import pytest

from user_service import UserService


@pytest.fixture
def service():
    return UserService()


# ---------------------------------------------------------------------------
# register() - the happy path
# ---------------------------------------------------------------------------


def test_register_returns_the_trimmed_username_for_a_valid_user(service):
    # Arrange
    username = "  bobby  "
    password = "Codes123"

    # Act
    result = service.register(username, password)

    # Assert
    assert result == "bobby"


def test_register_accepts_a_username_of_exactly_four_characters(service):
    # Arrange - four is the borderline that must be allowed.
    username = "bobs"
    password = "Codes123"

    # Act
    result = service.register(username, password)

    # Assert
    assert result == "bobs"


def test_register_accepts_a_password_of_exactly_six_characters(service):
    # Arrange - six is the borderline that must be allowed.
    username = "bobby"
    password = "Code1s"

    # Act
    result = service.register(username, password)

    # Assert
    assert result == "bobby"


# ---------------------------------------------------------------------------
# register() - every exception
# ---------------------------------------------------------------------------


def test_register_raises_value_error_when_the_username_is_none(service):
    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        service.register(None, "Codes123")

    assert str(exception_info.value) == "Username must not be null"


def test_register_raises_value_error_when_the_username_is_whitespace_only(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("   ", "Codes123")

    assert str(exception_info.value) == "Username must not be whitespace only"


def test_register_raises_value_error_when_the_password_is_none(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", None)

    assert str(exception_info.value) == "Password must not be null"


def test_register_raises_value_error_when_the_password_is_whitespace_only(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "   ")

    assert str(exception_info.value) == "Password must not be whitespace only"


def test_register_raises_value_error_when_the_username_is_too_short(service):
    # Arrange - three characters, one below the borderline.
    with pytest.raises(ValueError) as exception_info:
        service.register("bob", "Codes123")

    assert str(exception_info.value) == "Username must contain at least 4 characters"


def test_register_raises_value_error_when_the_username_is_already_taken(service):
    # Arrange
    service.register("bobby", "Codes123")

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "Codes456")

    assert str(exception_info.value) == "Username already exists"


def test_register_raises_value_error_when_the_password_is_too_short(service):
    # Arrange - five characters, one below the borderline.
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "Cod1e")

    assert str(exception_info.value) == "Password must contain at least 6 characters"


def test_register_raises_value_error_when_the_password_has_no_uppercase(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "codes123")

    assert str(exception_info.value) == "Password must contain at least 1 uppercase character"


def test_register_raises_value_error_when_the_password_has_no_lowercase(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "CODES123")

    assert str(exception_info.value) == "Password must contain at least 1 lowercase character"


def test_register_raises_value_error_when_the_password_has_no_number(service):
    # Test case 2 from the guide's test plan, with the password corrected
    # to six characters. See the next test for why.
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "Codess")

    assert str(exception_info.value) == "Password must contain at least 1 number character"


def test_register_reports_the_length_rule_first_for_the_guides_own_example(service):
    """The guide's test case 2 expects a "missing number" error for the
    password "Codes", but "Codes" is only five characters so the length
    rule fires first. This is a mistake in the guide, not in the code.
    """
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "Codes")

    assert str(exception_info.value) == "Password must contain at least 6 characters"


# ---------------------------------------------------------------------------
# The password character rules, after the fix
#
# The rules used to be whole-string matches against [A-Z|a-z|1-9]. They are
# now one "contains" search per rule, so each rule is judged on its own and
# the message names the rule that actually failed. See CODE_CORRECTIONS.md.
# ---------------------------------------------------------------------------


def test_register_accepts_a_password_whose_only_digit_is_zero(service):
    # Arrange - "Codes0" has an uppercase, a lowercase, a digit and six
    # characters, so every documented rule is satisfied.
    # Act
    result = service.register("bobby", "Codes0")

    # Assert
    assert result == "bobby"


def test_register_accepts_a_password_containing_a_symbol(service):
    """No stated rule forbids a symbol, so one must not be rejected.

    Under the old whole-string match a symbol failed all three rules at
    once, and the user was told the password had no uppercase letter.
    """
    # Act
    result = service.register("bobby", "Cod|es1")

    # Assert
    assert result == "bobby"


def test_register_names_the_uppercase_rule_when_only_uppercase_is_missing(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "codes1")

    assert str(exception_info.value) == "Password must contain at least 1 uppercase character"


def test_register_names_the_lowercase_rule_when_only_lowercase_is_missing(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "CODES1")

    assert str(exception_info.value) == "Password must contain at least 1 lowercase character"


def test_register_names_the_number_rule_when_only_a_number_is_missing(service):
    with pytest.raises(ValueError) as exception_info:
        service.register("bobby", "Codesss")

    assert str(exception_info.value) == "Password must contain at least 1 number character"


# ---------------------------------------------------------------------------
# login()
# ---------------------------------------------------------------------------


def test_login_returns_the_username_after_a_successful_registration(service):
    """Test case 1 from the guide's own test plan."""
    # Arrange
    service.register("bobby", "Codes123")

    # Act
    result = service.login("bobby", "Codes123")

    # Assert
    assert result == "bobby"


def test_login_returns_the_trimmed_username(service):
    """login() trims before returning, exactly as register() does."""
    # Arrange
    service.register("bobby", "Codes123")

    # Act
    result = service.login("  bobby  ", "  Codes123  ")

    # Assert
    assert result == "bobby"


def test_login_raises_value_error_when_the_username_is_none(service):
    with pytest.raises(ValueError) as exception_info:
        service.login(None, "Codes123")

    assert str(exception_info.value) == "Username and password must not be null"


def test_login_raises_value_error_when_the_password_is_none(service):
    with pytest.raises(ValueError) as exception_info:
        service.login("bobby", None)

    assert str(exception_info.value) == "Username and password must not be null"


def test_login_raises_value_error_when_the_username_is_whitespace_only(service):
    with pytest.raises(ValueError) as exception_info:
        service.login("   ", "Codes123")

    assert str(exception_info.value) == "Username and password must not be empty"


def test_login_raises_value_error_when_the_password_is_whitespace_only(service):
    with pytest.raises(ValueError) as exception_info:
        service.login("bobby", "   ")

    assert str(exception_info.value) == "Username and password must not be empty"


def test_login_raises_runtime_error_when_the_user_was_never_registered(service):
    with pytest.raises(RuntimeError) as exception_info:
        service.login("nobody", "Codes123")

    assert str(exception_info.value) == "Invalid username supplied"


def test_login_raises_value_error_when_the_password_is_wrong(service):
    """The "Invalid password supplied" branch, reached the obvious way.

    Before the lookup was fixed this branch needed a second user registered
    under a username equal to the password being supplied. A real user
    simply mistyping their password could never reach it.
    """
    # Arrange
    service.register("bobby", "Codes123")

    # Act and Assert
    with pytest.raises(ValueError) as exception_info:
        service.login("bobby", "wrong1A")

    assert str(exception_info.value) == "Invalid password supplied"
