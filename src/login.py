# new user:


def create_username():
    username = input("insira o nome de usuário: ")
    return username


def create_password():
    password = input("insira a senha: ")
    return password

# end new user


# check user credentials

def check_user(username, password):
    with open("./src/users.txt", "r") as user_file:
        for line in user_file:
            user_data = line.strip().split()
            if username == user_data[0] and password == user_data[1]:
                if username == "flavio" or username == "modular":
                    print("\U0001F34D")
                return True
        else:
            return False


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


def change_username(usr_username, usr_password, new_username):

    with open("./src/users.txt", "r") as users_file:
        lines = users_file.readlines()

    with open("./src/users.txt", "w") as users_file_write:
        for line in lines:
            if line.strip().split()[0] != usr_username:
                users_file_write.write(line)
            else:
                users_file_write.write(
                    new_username + " " + usr_password + "\n")

    print("Nome de usuário alterado com sucesso!")
    users_file.close()
    users_file_write.close()


def change_password(usr_username, usr_password, new_password):

    with open("./src/users.txt", "r") as users_file:
        lines = users_file.readlines()

    with open("./src/users.txt", "w") as users_file_write:
        for line in lines:
            if line.strip().split()[1] != usr_password:
                users_file_write.write(line)
            else:
                users_file_write.write(
                    usr_username + " " + new_password + "\n")

    print("Senha alterada com sucesso!")
# end user preferences


# save user


def save_user(username, password):
    with open("./src/users.txt", "a") as file:
        file.write(username + " " + password + "\n")

# end save user
