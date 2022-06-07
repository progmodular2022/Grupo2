import login
import sys
path_to_module = "./src/"
sys.path.append(path_to_module)


# test create_user()

def test_create_user():
    assert login.create_user("test1", "928") == True
    assert login.create_user("usr", "1pwd") == True


# test check_user()
def test_check_user():
    assert login.check_user("usuario123", "senha420") == True
    assert login.check_user("test456", "24senhaforte69") == True


# test change_username()
def test_change_username():
    assert login.change_username("test1", "928", "test2") == True
    assert login.change_username("test2", "928", "test3") == True
