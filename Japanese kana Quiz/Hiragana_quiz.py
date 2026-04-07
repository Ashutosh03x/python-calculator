import random
from colorama import Fore, init
init(autoreset=True)

print(Fore.MAGENTA+"\n===HIRAGANA QUIZ===")
    

quiz={
    "あ": "a",  "い": "i",   "う": "u",   "え": "e",   "お": "o",
    "か": "ka", "き": "ki",  "く": "ku",  "け": "ke",  "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su",  "せ": "se",  "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te",  "と": "to",
    "な": "na", "に": "ni",  "ぬ": "nu",  "ね": "ne",  "の": "no",
    "は": "ha", "ひ": "hi",  "ふ": "fu",  "へ": "he",  "ほ": "ho",
    "が": "ga", "ぎ": "gi",  "ぐ": "gu",  "げ": "ge",  "ご": "go",
    "ざ": "za", "じ": "ji",  "ず": "zu",  "ぜ": "ze",  "ぞ": "zo",
    "だ": "da", "ぢ": "ji",  "づ": "zu",  "で": "de",  "ど": "do",
    "ば": "ba", "び": "bi",  "ぶ": "bu",  "べ": "be",  "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi",  "ぷ": "pu",  "ぺ": "pe",  "ぽ": "po",
    "ま": "ma", "み": "mi",  "む": "mu",  "め": "me",  "も": "mo",
    "や": "ya",               "ゆ": "yu",               "よ": "yo",
    "ら": "ra", "り": "ri",  "る": "ru",  "れ": "re",  "ろ": "ro",
    "わ": "wa", "を": "wo",  "ん": "n",

}
total_questions = 0
correct_answers = 0

while True:
    question, answer = random.choice(list(quiz.items()))
    print("____")
    print(Fore.BLUE + f"|{question}|")
    print("----")
    romaji = input(Fore.YELLOW + "Enter the correct romaji (or 'q' to quit): ").strip().lower()

    if romaji == "q":
        if total_questions == 0:
            print(Fore.RED + "No questions answered yet!.")
        else:
            accuracy = (correct_answers / total_questions) * 100
            print(
                Fore.CYAN+ f"\nScore: {correct_answers}/{total_questions} (accuracy:{accuracy:.1f}%)")
        break

    if not romaji:
        print(Fore.RED + "Please enter an answer.")
        continue

    total_questions += 1
    if romaji == answer.lower():
        correct_answers += 1
        print(Fore.GREEN + "True!")
    else:
        print(Fore.RED + f"False! Correct answer: {answer}")
