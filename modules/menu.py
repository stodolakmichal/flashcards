import os
from modules.json_Operations import Json_Operations
from modules.tests import Tests
from modules.interrupts import Interrupts


class Menu:
    @staticmethod
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

    @staticmethod
    def choose_category(cls):
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
                new_words = Tests(dictionary_json.json_file)
                cls.category_menu(new_words, dictionary_json)
            elif category_input == "0":
                new_category_name = input("Podaj nazwę kategorii: ")
                if Interrupts.exit(new_category_name):
                    print("Anulowano dodawanie kategorii")
                Json_Operations(f"{new_category_name}.json")
            elif category_input.lower() == "x":
                print("Nauka zakończona")
                break
            else:
                print("\033[91mNieprawidłowy wybór. Spróbuj ponownie!\033[0m")
