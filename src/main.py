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

        with open("users.txt", "r") as users_file:
            for line in users_file:
                if username == line.strip().split()[0]:
                    user_data = line.split()
                    file_username = user_data[0]
                    file_password = user_data[1]
                    break

            if login.check_username(file_username, username):
                password = input("Insira a senha:\n")
                if login.check_password(file_password, password):
                    print("\nLogin efetuado com sucesso")
                else:
                    print("Senha incorreta")
                    return
            else:
                print("Usuário não existe")
                return
    #

    words = open("words.txt", "r").read()
    words_vector = file_words_to_vector(words.split("\n"))

    word = select_word(words_vector)[0]
    user_word = ["_" for i in range(len(word))]

    letters_found = 0

    attempts = len(word) // 2
    attempts_count = 0

    print("\nTotal de erros permitidos: ", attempts)

    while attempts_count <= attempts:
        print("\nErros cometidos: ", attempts_count, "/", attempts)

        print("\nPalavra: ", end="")
        print(user_word)

        if len(word) - letters_found > len(word) // 2:
            user_letter = input("\nDigite uma letra: ")

            if check_letter(user_letter, word):
                user_word, letters_found = add_letter(
                    user_letter, word, user_word, letters_found)
            else:
                print(".Letra não encontrada")
                attempts_count += 1
                if attempts_count == attempts:
                    print(".Número máximo de tentativas atingido\n.Você perdeu!")
                    print("Você errou, a palavra era:", word)
                    break

        if len(word) - letters_found == len(word) // 2:

            print("\nPalavra: ", end="")
            print(user_word)

            print("falta menos da metade das letras, agora chuta a palavra inteira")
            while (1):
                user_word = input("digite a palavra: ")

                if len(user_word) == 1:
                    print("agora nao pode chutar letra, só a palavra inteira")

                if len(user_word) > 1:
                    if check_full_word(user_word, word):
                        flag = 1
                        print("Boa, você acertou a palavra")
                        break
                    else:
                        flag = 0
                        print("Você errou, a palavra era:", word)
                        break

            if (flag or not flag):
                break


if __name__ == "__main__":
    main()
