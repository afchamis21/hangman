import random
from typing import Set

from Game import Game
from Utils import get_hangman_words, select_language


class Hangman(Game):
    def __init__(self):
        self.words: [str] = []
        self.__selected_word: str = ""
        self.__encoded_word: str = ""
        self.__correct_letters: Set[str] = set()
        self.__chosen_letters: Set[str] = set()
        self.__lives = 6

    def run(self) -> str:
        self.words = get_hangman_words(select_language())
        self.__selected_word = self.__get_random_word()
        self.__correct_letters = self.__find_correct_letters(self.__selected_word)
        self.__encoded_word = self.__encode_word(self.__selected_word)

        while "_" in self.__encoded_word and self.__lives > 0:
            self.__handle_new_letter_input()

        if self.__lives == 0:
            return f"Oops, you've lost. Your word was: {self.__selected_word}"

        if "_" not in self.__encoded_word:
            return "Congratulations, you've won "

    def __handle_new_letter_input(self):
        while True:
            self.__print_lives()
            self.__show_word()
            self.__print_chosen_letters()
            new_letter = input("Type a letter: ").lower()
            if new_letter in self.__chosen_letters:
                print("Type a letter that hasn't been chosen")
                continue

            if new_letter == " ":
                print("Type a valid letter")
                continue

            if new_letter not in self.__correct_letters:
                self.__handle_invalid_letter()
                self.__chosen_letters.add(new_letter)
                return

            self.__chosen_letters.add(new_letter)
            self.__update_encoded_word(new_letter)
            return

    def __handle_invalid_letter(self) -> None:
        self.__lives -= 1

    def __print_chosen_letters(self) -> None:
        print(f"Chosen letters: {[*self.__chosen_letters]}")

    def __print_lives(self):
        print(f"\nYou've got {self.__lives} lives left")

    def __get_random_word(self) -> str:
        return random.choice(self.words)

    def __update_encoded_word(self, new_leter: str) -> None:
        new_encoded_word = ""
        for i, (letter, encoded_letter) in enumerate(zip(self.__selected_word, self.__encoded_word)):
            if letter == new_leter:
                new_encoded_word += new_leter
            else:
                new_encoded_word += encoded_letter

        self.__encoded_word = new_encoded_word

    @staticmethod
    def __encode_word(word: str) -> str:
        encoded_word = ""
        for letter in word:
            if letter == " ":
                encoded_word += " "
            else:
                encoded_word += "_"

        return encoded_word

    @staticmethod
    def __find_correct_letters(word: str) -> Set[str]:
        letters: Set[str] = set()
        for letter in word.replace(" ", ""):
            letters.add(letter.lower())

        return letters

    def __show_word(self):
        print(f"{self.__encoded_word}")
