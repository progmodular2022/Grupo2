import main
import sys
path_to_module = "./src/"
sys.path.append(path_to_module)


def test_check_letter():
    assert main.check_letter("a", "banana") == True
    assert main.check_letter("b", "banana") == True
    assert main.check_letter("c", "banana") == False
    assert main.check_letter("d", "banana") == False


# def test_add_letter():
#     assert main.add_letter("a", "banana", ["_", "_", "_", "_", "_", "_"], 3) == [
#         "_", "a", "_", "a", "_", "a"]

#     assert main.add_letter("b", "banana", ["_", "_", "_", "_", "_", "_"], 1) == [
#         "b", "_", "_", "_", "_", "_"]

#     assert main.add_letter("f", "garfo", ["_", "_", "_", "_", "_"], 1) == [
#         "_", "_", "_", "f", "_"]


def test_check_full_word():
    assert main.check_full_word("banana", "banana") == True
    assert main.check_full_word("abacaxi", "abacate") == False
    assert main.check_full_word("abacaxi", "abacaxi") == True
    assert main.check_full_word("coelho", "ventilador") == False


test_check_letter()
test_add_letter()
test_check_full_word()
