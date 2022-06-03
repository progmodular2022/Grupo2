# new user:


def create_username():
    username = input("insira o nome de usuário: ")
    return username


def create_password():
    password = input("insira a senha: ")
    return password

# end new user


# check user credentials


def check_username(username, input_username):
    if username == input_username:
        return True
    else:
        return False


def check_password(password, input_password):
    if password == input_password:
        return True
    else:
        return False

# end check user credentials


# user preferences


def change_password():
    new_password = input("insira a nova senha: ")
    return new_password


def chenge_username():
    new_username = input("insira o novo nome de usuário: ")
    return new_username

# end user preferences


# save user


def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(username + " " + password + "\n")

# end save user
