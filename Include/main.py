import json
import random
import os


class Words:
    def __init__(self, words: dict):
        self.words = words

    def displayWords(self):
        """Opcja 1 - Wyswietlanie zawartosci slownika"""
        for word, translation in self.words.items():
            print(f"{word} - {translation}")

    def testKnowledge(self):
        """Opcja 2 - Sprawdzanie wiedzy. Jesli odpowiedz jest poprawna, zmniejsza się counter i slowo jest usuwane ze slownika
                     Jesli odpowiedz jest niepoprawna, powtarzamy wyswietlanie pytania"""
        counter = len(self.words)
        wrong_answers_counter = 0
        words_copy = dict(self.words)

        while counter != 0:
            random_word = random.choice(list(words_copy.keys()))
            random_translation = words_copy[random_word]
            user_input = input(f"{random_word} - ")
            if user_input == f"{random_translation}":
                print("\033[92mPoprawnie!\033[0m")
                counter -= 1
                del words_copy[random_word]
            else:
                print(f"\033[91mŹle! Poprawnie: {random_word} - {random_translation}\033[0m")
                wrong_answers_counter += 1


class Json_Operations:
    def __init__(self, path_to_json_file=os.path.join(os.getcwd(), "dictionaries", "default_dictionary.json")):
        self.path = path_to_json_file
        self.json_file = self.getParsedDataFromJsonFile()

    def getParsedDataFromJsonFile(self):
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.path, "w") as file:
                return json.dump({}, file, indent=2)

    def getWordsToBeAdded(self):
        while True:
            new_word = input("Podaj słowo (exit konczy dodawanie slow): ")
            if new_word.lower() == "exit":
                break
            new_translation = input("Podaj tlumaczenie: ")
            self.json_file[new_word] = new_translation

    def addNewWordAndTranslationToJson(self):
        self.getWordsToBeAdded()
        try:
            with open(self.path, "w") as file:
                json.dump(self.json_file, file, indent=2)
            print("Nowe słowa zostały dodane do pliku json")
        except FileNotFoundError:
            print(f"Plik {self.path} nie istnieje.")
        file.close()


def show_menu(dictionary_json=None, new_words=None):
    while True:
        print(
            f'''1. Wyswietl dostepne slowa
2. Testuj swoja wiedze
3. Dodaj nowe słowo i tłumaczenie
4. Dodaj nową kategorię
X. Zamknij program''')
        user_input = input("Podaj co chcesz zrobić: ")
        if user_input == "1":
            new_words.displayWords()
        elif user_input == "2":
            new_words.testKnowledge()
        elif user_input == "3":
            dictionary_json.addNewWordAndTranslationToJson()
        elif user_input == "4":
            new_category_name = input("Podaj nazwę kategorii: ")
            Json_Operations(os.path.join(os.getcwd(), "dictionaries", f"{new_category_name}.json"))
            pass
        elif user_input.lower() == "x":
            print("Program zakończony")
            break
        else:
            print("\033[91mNieprawidłowy wybór. Spróbuj ponownie!\033[0m")


if __name__ == "__main__":
    dictionary_json = Json_Operations()
    new_words = Words(dictionary_json.json_file)
    show_menu(dictionary_json, new_words)
