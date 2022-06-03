from main import *
import unittest
import sys
path_to_module = "./src/"
sys.path.append(path_to_module)


def check_letter():
    assert main.check_letter("a", "banana") == True
    assert main.check_letter("b", "banana") == True
    assert main.check_letter("c", "banana") == False
    assert main.check_letter("d", "banana") == False


def add_letter():
    assert main.add_letter("a", "banana", ["_", "_", "_", "_", "_", "_"], 0) == [
        "_", "a", "_", "a", "_", "a"]

    assert main.add_letter("b", "banana", ["_", "_", "_", "_", "_", "_"], 0) == [
        "b", "_", "_", "_", "_", "_"]

    assert main.add_letter("f", "garfo", ["_", "_", "_", "_", "_"], 0) == [
        "_", "_", "_", "f", "_"]


def check_full_word():
    assert main.check_full_word("banana", "banana") == True
    assert main.check_full_word("abacaxi", "abacate") == False
    assert main.check_full_word("abacaxi", "abacaxi") == True
    assert main.check_full_word("coelho", "ventilador") == False
