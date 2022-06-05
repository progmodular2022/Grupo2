import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import main

def test_select_word():
    words = ["banana", "abacaxi", "abacate", "coelho", "ventilador"]
    assert main.select_word(words) != words


def test_check_letter():
    assert main.check_letter("a", "banana") == True
    assert main.check_letter("b", "banana") == True
    assert main.check_letter("c", "banana") == False
    assert main.check_letter("d", "banana") == False


def test_add_letter():
    assert main.add_letter("a", "banana", ["_", "_", "_", "_", "_", "_"], 0) == (
        ["_", "a", "_", "a", "_", "a"], 3)
    assert main.add_letter("b", "banana", ["_", "_", "_", "_", "_", "_"], 0) == (
        ["b", "_", "_", "_", "_", "_"], 1)
    assert main.add_letter("c", "banana", ["_", "_", "_", "_", "_", "_"], 0) == (
        ["_", "_", "_", "_", "_", "_"], 0)


def test_check_full_word():
    assert main.check_full_word("banana", "banana") == True
    assert main.check_full_word("abacaxi", "abacate") == False
    assert main.check_full_word("abacaxi", "abacaxi") == True
    assert main.check_full_word("coelho", "ventilador") == False


def test_file_words_to_vector():
    vector = []
    words = ["banana", "abacaxi", "abacate", "coelho", "ventilador"]
    for word in words:
        vector.append(word.strip())
    assert main.file_words_to_vector(words) == vector


# test_select_word()
# test_check_letter()
# test_add_letter()
# test_check_full_word()
test_file_words_to_vector()
