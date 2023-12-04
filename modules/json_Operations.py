import json
import os
from modules.interrupts import Interrupts


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

    @staticmethod
    def getWords():
        new_word = input("Podaj słowo (\"exit\" konczy pobieranie słów): ")
        return new_word

    def updateJsonFile(self):
        try:
            with open(self.path, "w") as file:
                json.dump(self.json_file, file, indent=2)
            print("Slownik został zaktualizowany!")
        except FileNotFoundError:
            print(f"Plik {self.path} nie istnieje!")
        file.close()

    def getWordsToBeAdded(self):
        while True:
            new_word = self.getWords()
            if Interrupts.exit(new_word):
                break
            new_translation = input("Podaj tlumaczenie: ")
            self.json_file[new_word] = new_translation

    def getWordsToBeDeleted(self):
        while True:
            new_word = self.getWords()
            if Interrupts.exit(new_word):
                break
            if new_word in self.json_file:
                del self.json_file[new_word]
                print(f"Slowo {new_word} zostało usunięte!")
            else:
                print(f"Slowa {new_word} nie ma w slowniku!")

    def addNewWordAndTranslationToJson(self):
        self.getWordsToBeAdded()
        self.updateJsonFile()

    def deleteWordFromDictionary(self):
        self.getWordsToBeDeleted()
        self.updateJsonFile()
