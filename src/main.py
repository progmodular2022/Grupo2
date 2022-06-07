import random
import login


def select_word(words):
    random.shuffle(words)
    return words


def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


def add_letter(letter, word, user_word, letters_found):
    for i in range(len(word)):
        if word[i] == letter:
            user_word[i] = letter
            letters_found += 1
    return user_word, letters_found


def check_full_word(user_word, word):
    if user_word == word:
        return True
    else:
        return False


def file_words_to_vector(words):
    words_vector = []
    for word in words:
        words_vector.append(word.strip())
    return words_vector


def display_hangman():
    stages = [
        """
                    --------
                    |      |
                    |
                    |
                    |
                    |
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |
                    |
                    |
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |      |
                    |      |
                    |
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |     \\|
                    |      |
                    |
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     /
                    -
        """,
        """
                    --------
                    |      |
                    |      0
                    |     \\|/
                    |      |
                    |     / \\
                    -
        """
    ]
    return stages


def main():
    # utilizando componente reutilizavel para login

    usr_inp = input("Já possui conta? (s/n)\n")

    if usr_inp == "n":
        username = login.create_username()
        password = login.create_password()

        login.save_user(username, password)

        print("Conta criada, agora utilize os dados para logar.\n")

        inp_username = input("Insira o nome de usuário:\n")
        inp_password = input("Insira a senha:\n")

        if login.check_user(inp_username, inp_password):
            print("Login realizado com sucesso!")

        else:
            print("Login inválido!")

    else:
        username = input("Insira o nome de usuário:\n")

        with open("./src/users.txt", "r") as users_file:
            for line in users_file:
                if username == line.strip().split()[0]:
                    user_data = line.split()
                    file_username = user_data[0]
                    file_password = user_data[1]
                    break
            else:
                print("Usuário não existe")
                return

            if login.check_username(file_username, username):
                password = input("Insira a senha:\n")
                if login.check_password(file_password, password):
                    print("\nLogin efetuado com sucesso")

                    # usr_change = input(
                    #     "\nDeseja alterar o nome de usuário ou senha? (s/n)\n")

                    # if usr_change == "s":

                    #     alter_username = input(
                    #         "Deseja alterar o nome de usuário? (s/n)\n")

                    #     if alter_username == "s":
                    #         new_username = login.change_username()

                    #         with open("./src/users.txt", "r") as users_file:
                    #             for line in users_file:
                    #                 if username == line.strip().split()[0]:
                    #                     line.strip().split()[0] = new_username
                    #                     old_username = line.strip().split()[0]
                    # else:
                    #     print("nome de usuário não encontrado")
                    #     users_file.close()
                    #     return

                    # with open("./src/users.txt", "r") as users_file:
                    #     with open("./src/users.txt", "w") as users_file_write:
                    #         for line in users_file:
                    #             if old_username == line.strip().split()[0]:
                    #                 line = line.strip().split()
                    #                 line[0] = new_username
                    #                 line = " ".join(line)
                    #                 users_file_write.write(
                    #                     line + "\n")

                    #                 if line.strip().split()[0] == new_username:
                    #                     print(
                    #                         "Nome de usuário alterado com sucesso")
                    #                 else:
                    #                     print(
                    #                         "Nome de usuário não alterado")
                    #             else:
                    #                 users_file_write.write(line)

                    if username == "flavio" or username == "modular":
                        print("\U0001F34D")

                else:
                    print("Senha incorreta")
                    return

    #

    words = open("./src/words.txt", "r").read()
    words_vector = file_words_to_vector(words.split("\n"))

    word = select_word(words_vector)[0]
    user_word = ["_" for i in range(len(word))]

    stages = display_hangman()

    letters_found = 0

    attempts = len(stages)
    attempts_count = 0

    used_letters = []

    while attempts_count <= attempts:
        print(stages[attempts_count])

        # printando letras usadas
        if len(used_letters) > 0:
            print("letras já usadas:", end="")
            for letters in used_letters:
                print(letters, end=" ")

        # printando a palavra do player
        print("\nPalavra: ", end="")
        for letter in user_word:
            print(letter, end=" ")

        # pegando input do player
        user_letter = input("\n>Digite uma letra: ")
        print("Se quiser chutar a palavra completa digite 'chutar' para então digitar a palavra")

        if user_letter == "chutar":
            user_word = input("Digite a palavra completa: ")
            if check_full_word:
                print("\nParabéns, você ganhou!")
                return
            else:
                print("\nVocê perdeu!")
                return

        # verificando se a letra já foi usada
        if user_letter in used_letters:
            print("\nLetra já usada")
            continue

        else:
            used_letters.append(user_letter)

            # verificando se a letra digitada existe na palavra
            if check_letter(user_letter, word):
                user_word, letters_found = add_letter(
                    user_letter, word, user_word, letters_found)
            else:
                print("\n>Letra não encontrada")
                attempts_count += 1
                if attempts_count == attempts:
                    print(">Número máximo de tentativas atingido\n>Você perdeu!")
                    print("Você errou, a palavra era:", word)
                    return

        # verificando se numero de letras encontradas tem o tamanho da palavra pra ver se o player ganhou sem digitar a palavra completa
        if letters_found == len(word):
            print("\nPalavra: ", end="")
            for letter in user_word:
                print(letter, end=" ")

            # verificando se palavra formada pelas letras está certa
            if check_full_word:
                print("\nParabéns, você ganhou!")
                return
            else:
                print("\nVocê perdeu!")
                return


if __name__ == "__main__":
    main()
