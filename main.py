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
        if wrong_answers_counter == 10:
            print("Odpowiedziałeś 10 razy źle! Zacznij do nowa!")


class Json_Operations:
    def __init__(self, category_file="default_dictionary.json"):
        self.path = os.path.join(os.getcwd(), "dictionaries", category_file)
        self.json_file = self.getParsedDataFromJsonFile()

    def getParsedDataFromJsonFile(self):
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.path, "w") as file:
                json.dump({}, file, indent=2)
                return {}

    def getWords(self):
        while True:
            new_word = input("Podaj słowo (exit konczy dodawanie slow): ")
            return new_word

    def getWordsToBeAdded(self):
        while True:
            new_word = input("Podaj słowo (exit konczy dodawanie slow): ")
            if new_word.lower() == "exit":
                break
            new_translation = input("Podaj tlumaczenie: ")
            self.json_file[new_word] = new_translation

    def getWordsToBeDeleted(self):
        while True:
            new_word = input("Podaj słowo (exit konczy dodawanie slow): ")
            if new_word.lower() == "exit":
                break
            if new_word in self.json_file:
                del self.json_file[new_word]
                print(f"Slowo {new_word} zostało usunięte!")
            else:
                print(f"Slowa {new_word} nie ma w slowniku!")

    def updateJsonFile(self):
        try:
            with open(self.path, "w") as file:
                json.dump(self.json_file, file, indent=2)
            print("Nowe słowa zostały dodane do pliku json")
        except FileNotFoundError:
            print(f"Plik {self.path} nie istnieje!")
        file.close()

    def addNewWordAndTranslationToJson(self):
        self.getWordsToBeAdded()
        self.updateJsonFile()

    def deleteWordFromDictionary(self):
        self.getWordsToBeDeleted()
        self.updateJsonFile()


def choose_category():
    while True:
        path_to_json_file = os.path.join(os.getcwd(), "dictionaries")
        categories = os.listdir(path_to_json_file)
        category_json_files_without_extensions = [os.path.splitext(file)[0] for file in categories]
        for index, category in enumerate(category_json_files_without_extensions, start=1):
            print(f"{index}. {category}")
        print("0. Dodaj kategorię")
        print("X. Zakończ naukę")
        category_input = input("Wybierz kategorię: ")

        if "1" <= category_input <= f"{len(categories)}":
            dictionary_json = Json_Operations(categories[int(category_input) - 1])
            new_words = Words(dictionary_json.json_file)
            category_menu(new_words, dictionary_json)
        elif category_input == "0":
            new_category_name = input("Podaj nazwę kategorii: ")
            Json_Operations(f"{new_category_name}.json")
        elif category_input.lower() == "x":
            print("Nauka zakończona")
            break
        else:
            print("\033[91mNieprawidłowy wybór. Spróbuj ponownie!\033[0m")


def category_menu(new_words, dictionary_json):
    while True:
        print(
            '''1. Wyswietl dostepne slowa
2. Testuj swoja wiedze
3. Dodaj nowe słowo i tłumaczenie
4. Usun slowo
X. Zmień kategorię''')
        user_input = input("Podaj co chcesz zrobić: ")
        if user_input == "1":
            new_words.displayWords()
        elif user_input == "2":
            new_words.testKnowledge()
        elif user_input == "3":
            dictionary_json.addNewWordAndTranslationToJson()
        elif user_input == "4":
            dictionary_json.deleteWordFromDictionary()
        elif user_input.lower() == "x":
            break
        else:
            print("\033[91mNieprawidłowy wybór. Spróbuj ponownie!\033[0m")


if __name__ == "__main__":
    choose_category()
