# happy2.py

def happy():
    return "Happy birthday to you!\n"

def verseFor(person):
    lyrics = happy() * 2 + "Happy birthday, dear {}.\n".format(person) + happy()
    return lyrics

def main():
    for person in ["Chris", "Stacey", "Lil Chris"]:
        print(verseFor(person))
main()