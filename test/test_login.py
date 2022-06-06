import login
import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

# testing check_username()


def test_check_username():
    assert login.check_username("username", "username") == True
    assert login.check_username("username", "username2") == False

# testing check_password()


def test_check_password():
    assert login.check_password("password", "password") == True
    assert login.check_password("password", "password2") == False
