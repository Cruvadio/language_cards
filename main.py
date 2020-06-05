from database_manager import DataBase
from constants import LANGUAGES


def show_languages():
    for i in range(len(LANGUAGES)):
        print("{0} - {1}".format(i + 1, LANGUAGES[i]))


def choose_language(promt):
    show_languages()
    num = int(input(promt))
    while num > len(LANGUAGES) or num < 1:
        print("Wrong number! Number must be in range of 1 to {0}.".format(len(LANGUAGES)))
        num = int(input())
    return LANGUAGES[num - 1]


if __name__ == "__main__":
    db = DataBase("words.db")
    print(db.show_tables())
    native = choose_language("Choose your native language: ")
    foreign = choose_language("Chose foreign language you want to learn: ")
    db.add_new_language(foreign, native)
    while True:
        print("1 - Add a word\n2 - Show table\n3 - Exit")
        choice = input()
        if choice == '1':
            word = input("Enter word you want to repeat: ")
            translate = input("Enter it's translation: ")
            db.add_new_word(word, translate, foreign, native)
        elif choice == '2':
            print(db.return_all_table(foreign, native))
        elif choice == '3':
            break
        else:
            print("Wrong command!")
    print("See you soon!")