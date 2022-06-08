import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import login

# test create_user()

# def test_create_user():
#     assert login.create_user("test1", "928") == True
#     assert login.create_user("usr", "1pwd") == True


# test check_user()
def test_check_user():
    assert login.check_user("usuario123", "senha420") == False
    assert login.check_user("dev", "dev123") == True


# test change_username()
def test_change_username():
    assert login.change_username("testenew", "928", "test2") == True
    assert login.change_username("test5", "928", "test3") == False


# test change_password()
def test_change_password():
    assert login.change_password("test2", "asd", "231") == True
    assert login.change_password("test3", "929", "930") == False


# test check_username_duplicity()
def test_check_username_duplicity():
    assert login.check_username_duplicity("test1") == False
    assert login.check_username_duplicity("test4") == False
    assert login.check_username_duplicity("dev") == True
    assert login.check_username_duplicity("testenew") == True
