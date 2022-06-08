# create user:


def create_user():
    username = input("insira o nome de usuário: ")
    password = input("insira a senha: ")

    save_user(username, password)

    if check_user(username, password):
        print("Usuário criado com sucesso")
        return username
    else:
        print("Erro ao criar usuário")
        return


# end create user


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
