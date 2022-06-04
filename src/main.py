import random
from winsound import SND_NODEFAULT
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

        if login.check_username(username, inp_username):
            if login.check_password(password, inp_password):
                print("\nLogin efetuado com sucesso")
            else:
                print("Senha incorreta")
                return
        else:
            print("Usuário não existe")
            return

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

        if len(used_letters) > 0:
            print("letras já usadas:", end="")
            for letters in used_letters:
                print(letters, end=" ")

        print("\nPalavra: ", end="")
        for letter in user_word:
            print(letter, end=" ")

        user_letter = input("\n>Digite uma letra: ")
        used_letters.append(user_letter)

        if check_letter(user_letter, word):
            user_word, letters_found = add_letter(
                user_letter, word, user_word, letters_found)
        else:
            print(">Letra não encontrada")
            attempts_count += 1
            if attempts_count == attempts:
                print(">Número máximo de tentativas atingido\n>Você perdeu!")
                print("Você errou, a palavra era:", word)
                break

        if letters_found == len(word):
            print("\nPalavra: ", end="")
            for letter in user_word:
                print(letter, end=" ")

            if check_full_word:
                print("\nParabéns, você ganhou!")
                break
            else:
                print("\nVocê perdeu!")
                break

        if len(word) - letters_found <= len(word) // 2:
            print("\nPalavra: ", end="")
            for letter in user_word:
                print(letter, end=" ")
            usr_choice = input(
                "\n>falta metade das letras, quer chutar a palavra ou tentar outra letra? (chutar/letra)\n")

            if usr_choice == "chutar":
                user_word = input("Digita a palavra: ")
                if check_full_word(user_word, word):
                    print("\nVocê venceu!")
                    break

                else:
                    print("\nVocê perdeu!")
                    print("Você errou, a palavra era:", word)
                    break


if __name__ == "__main__":
    main()
