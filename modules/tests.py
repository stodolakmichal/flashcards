import random
from modules.my_decorators import dashes_before_after_text

class Tests:
    def __init__(self, words: dict):
        self.words = words

    @dashes_before_after_text
    def displayWords(self):
        """Opcja 1 - Wyswietlanie zawartosci slownika"""
        for word, translation in self.words.items():
            print(f"{word} - {translation}")

    @dashes_before_after_text
    def testKnowledge(self):
        """Opcja 2 - Sprawdzanie wiedzy.
        Jesli odpowiedz jest poprawna, zmniejsza się counter i slowo jest usuwane ze slownika
        Jesli odpowiedz jest niepoprawna, powtarzamy wyswietlanie pytania
        """
        counter = len(self.words)
        wrong_answers_counter = 0
        words_copy = dict(self.words)

        while counter != 0 and wrong_answers_counter <= 9:
            random_word = random.choice(list(words_copy.keys()))
            random_translation = words_copy[random_word]
            user_input = input(f"{random_word} - ")
            if user_input == f"{random_translation}":
                print("Poprawnie!")
                counter -= 1
                del words_copy[random_word]
            else:
                print(f"Źle! Poprawnie: {random_word} - {random_translation}")
                wrong_answers_counter += 1
            #TODO print(f"Złych odpowiedzi: {wrong_answers_counter}")
        if wrong_answers_counter == 10:
            print("Odpowiedziałeś 10 razy źle! Zacznij do nowa!")
