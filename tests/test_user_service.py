"""Exercise 2 - testing exceptions.

Write the test plan first, then a test case for every exception that
register() and login() can raise.

HOW TO USE THIS FILE
  * One test is already written for you, as a worked example.
  * Every other test is a TODO that SKIPs until you write it. Delete the
    @pytest.mark.skip line and replace the body.

A NOTE BEFORE YOU START
  Every test below can pass against the code as it stands. When one fails,
  read the failure message carefully: the order the validation rules run in
  decides which message you get, and that is easy to get wrong in a plan.
  One row of the exercise guide's own test plan has exactly that mistake in
  it. See CODE_CORRECTIONS.md.
"""

import pytest

from user_service import UserService


@pytest.fixture
def service():
    """A brand new UserService for each test, so no user registered in one
    test can leak into another."""
    return UserService()


# ---------------------------------------------------------------------------
# register()
# ---------------------------------------------------------------------------


def test_register_rejects_a_password_with_no_number(service):
    """WORKED EXAMPLE - test case 2 from the guide's test plan, corrected.

    The guide uses the password "Codes". That is only five characters, so
    the length rule fires first and you get "Password must contain at least
    6 characters" instead. "Codess" is six characters with no digit, which
    is what the test case was actually trying to express.
    """
    # Arrange
    username = "bobby"
    password = "Codess"

    # Act and Assert. pytest.raises is the pytest equivalent of JUnit's
    # assertThrows. The `match` argument is a regular expression searched
    # for in the message, so special characters would need escaping.
    with pytest.raises(ValueError) as exception_info:
        service.register(username, password)

    assert str(exception_info.value) == "Password must contain at least 1 number character"


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_returns_the_trimmed_username_for_a_valid_user(service):
    # Should assert that register("  bobby  ", "Codes123") returns "bobby".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_username_is_none(service):
    # Should assert the message "Username must not be null".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_username_is_whitespace_only(service):
    # Should assert the message "Username must not be whitespace only".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_password_is_none(service):
    # Should assert the message "Password must not be null".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_password_is_whitespace_only(service):
    # Should assert the message "Password must not be whitespace only".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_username_is_too_short(service):
    # Should assert "Username must contain at least 4 characters" for a
    # three character username. Four characters is the borderline that
    # must be accepted.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_username_is_already_taken(service):
    # Should register a user, register the same username again, and assert
    # the message "Username already exists".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_password_is_too_short(service):
    # Should assert "Password must contain at least 6 characters" for a
    # five character password such as "Cod1e".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_password_has_no_uppercase(service):
    # Should assert "Password must contain at least 1 uppercase character"
    # for a password such as "codes123".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_raises_value_error_when_the_password_has_no_lowercase(service):
    # Should assert "Password must contain at least 1 lowercase character"
    # for a password such as "CODES123".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_register_accepts_a_password_whose_only_digit_is_zero(service):
    # Should assert that register("bobby", "Codes0") returns "bobby",
    # because "Codes0" does contain a number. Zero is a number.
    pass


# ---------------------------------------------------------------------------
# login()
# ---------------------------------------------------------------------------


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_returns_the_username_after_a_successful_registration(service):
    # This is test case 1 from the guide's test plan: register
    # "bobby" / "Codes123", then log in with the same pair and assert
    # that "bobby" is returned.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_raises_value_error_when_the_username_is_none(service):
    # Should assert "Username and password must not be null".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_raises_value_error_when_the_password_is_none(service):
    # Should assert "Username and password must not be null".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_raises_value_error_when_the_username_is_whitespace_only(service):
    # Should assert "Username and password must not be empty".
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_raises_runtime_error_when_the_user_was_never_registered(service):
    # Should assert RuntimeError with the message
    # "Invalid username supplied" for an unknown user.
    pass


@pytest.mark.skip(reason="TODO - delete this line and write the test")
def test_login_raises_value_error_when_the_password_is_wrong(service):
    # Should register "bobby" / "Codes123", then log in as "bobby" with a
    # different password and assert ValueError with the message
    # "Invalid password supplied".
    pass
