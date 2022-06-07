# new user:


def create_username():
    username = input("insira o nome de usuário: ")
    return username


def create_password():
    password = input("insira a senha: ")
    return password

# end new user


# check user credentials

def check_user(inp_username, inp_password):
    with open("./src/users.txt", "r") as user_file:
        for line in user_file:
            user_data = line.split()
            if inp_username == user_data[0] and inp_password == user_data[1]:
                if inp_username == "flavio" or inp_username == "modular":
                    print("\U0001F34D")
                return True
            else:
                return False

        user_file.close()


# def check_username(username, input_username):
#     if username == input_username:
#         return True
#     else:
#         return False


# def check_password(password, input_password):
#     if password == input_password:
#         return True
#     else:
#         return False

# end check user credentials


# user preferences


def change_password():
    new_password = input("insira a nova senha: ")
    return new_password


def change_username():
    new_username = input("insira o novo nome de usuário: ")
    return new_username

# end user preferences


# save user


def save_user(username, password):
    with open("./src/users.txt", "a") as file:
        file.write(username + " " + password + "\n")

# end save user
