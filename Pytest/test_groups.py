import pytest
@pytest.mark.login
def test_login_valid_user():
    username="newuser"
    password="newuser"
    assert username=="newuser" and password=="newuser"
@pytest.mark.login
def test_login_invalid_user():
    username="wronguser"
    password="wronguser"
    assert username=="wronguser" and password=="wronguser"