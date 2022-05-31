#coding=utf-8

import secrets

basic_vowels = {
    "ㅏ": "a",
    "ㅑ": "ya",
    "ㅓ": "eo",
    "ㅕ": "yeo",
    "ㅗ": "o",
    "ㅛ": "yo",
    "ㅜ": "u",
    "ㅠ": "yu",
    "ㅡ": "eu",
    "ㅣ": "i"
}

diphthongs = {
    "ㅐ": "ae",
    "ㅒ": "yae",
    "ㅔ": "e",
    "ㅖ": "ye",
    "ㅘ": "wa",
    "ㅙ": "wae",
    "ㅚ": "oe",
    "ㅝ": "wo",
    "ㅞ": "we",
    "ㅟ": "wi",
    "ㅢ": "ui"
}

consonants = {
    "ㄱ": "g",
    "ㄴ": "n",
    "ㄷ": "d",
    "ㄹ": "r",
    "ㅁ": "m",
    "ㅂ": "b",
    "ㅅ": "s",
    "ㅇ": "ng",
    "ㅈ": "j",
    "ㅊ": "ch",
    "ㅋ": "k",
    "ㅌ": "t",
    "ㅍ": "p",
    "ㅎ": "h",
    "ㄲ": "kk",
    "ㄸ": "tt",
    "ㅃ": "pp",
    "ㅆ": "ss",
    "ㅉ": "jj"
}

all_alphabets = {**basic_vowels, **diphthongs, **consonants}

while True:
    print("\nWhich pronouciation you would like to test:")
    print("1. All vowels (Basic vowels + Diphthongs/Compound Vowel")
    print("2. Basic Vowels")
    print("3. Diphthongs/Complex Vowels")
    print("4. Consonants")
    print("5. All alphabet")
    print("Enter any other key to exit")
    try:
        choice = int(input("Enter your choice (e.g: 1): "))
    except:
        quit()
        
    if choice == 1:
        questions = [*basic_vowels] + [*diphthongs] 
    elif choice == 2:
        questions = [*basic_vowels]
    elif choice == 3:
        questions = [*diphthongs]
    elif choice == 4:
        questions = [*consonants]
    elif choice == 5:
        questions = [*all_alphabets]
    else:
        quit()

    wrong_questions = []

    index = 0
    while questions:
        picked_question = secrets.choice(questions)
        index = index + 1
        answer = input(f"\n{index}) Pronouciation for {picked_question}: ")
        if answer == all_alphabets[picked_question]:
            print("Correct! ✔️")
        else:
            print("Wrong! ❌")
            print(f"Correct answer: {all_alphabets[picked_question]}")
            wrong_questions.append(picked_question)

        questions.remove(picked_question)
    
    if wrong_questions:
        print("\nQuestion you got wrong (Listed with correct answer)")
        for question in wrong_questions:
            print(f"{question}: {all_alphabets[question]}")
