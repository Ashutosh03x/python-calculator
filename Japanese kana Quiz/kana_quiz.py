import random
from colorama import Fore, init
init(autoreset=True)

hiragana_quiz = {
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

katakana_quiz = {
    "ア": "a",  "イ": "i",   "ウ": "u",   "エ": "e",   "オ": "o",
    "カ": "ka", "キ": "ki",  "ク": "ku",  "ケ": "ke",  "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su",  "セ": "se",  "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te",  "ト": "to",
    "ナ": "na", "ニ": "ni",  "ヌ": "nu",  "ネ": "ne",  "ノ": "no",
    "ハ": "ha", "ヒ": "hi",  "フ": "fu",  "ヘ": "he",  "ホ": "ho",
    "ガ": "ga", "ギ": "gi",  "グ": "gu",  "ゲ": "ge",  "ゴ": "go",
    "ザ": "za", "ジ": "ji",  "ズ": "zu",  "ゼ": "ze",  "ゾ": "zo",
    "ダ": "da", "ヂ": "ji",  "ヅ": "zu",  "デ": "de",  "ド": "do",
    "バ": "ba", "ビ": "bi",  "ブ": "bu",  "ベ": "be",  "ボ": "bo",
    "パ": "pa", "ピ": "pi",  "プ": "pu",  "ペ": "pe",  "ポ": "po",
    "マ": "ma", "ミ": "mi",  "ム": "mu",  "メ": "me",  "モ": "mo",
    "ヤ": "ya",               "ユ": "yu",               "ヨ": "yo",
    "ラ": "ra", "リ": "ri",  "ル": "ru",  "レ": "re",  "ロ": "ro",
    "ワ": "wa", "ヲ": "wo",  "ン": "n",
}


def play_quiz(quiz, title):
    print(Fore.MAGENTA + f"\n==={title}===")
    total_questions = 0
    correct_answers = 0

    while True:
        question, answer = random.choice(list(quiz.items()))
        print("____")
        print(Fore.BLUE + f"|{question}|")
        print("----")
        romaji = input(Fore.YELLOW + "Enter the correct romaji (or 'q' to menu): ").strip().lower()

        if romaji == "q":
            if total_questions == 0:
                print(Fore.RED + "No questions answered yet!.")
            else:
                accuracy = (correct_answers / total_questions) * 100
                print(
                    Fore.CYAN + f"\nScore: {correct_answers}/{total_questions} (accuracy:{accuracy:.1f}%)"
                )
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


while True:
    print(Fore.MAGENTA + "\n===MAIN MENU===")
    print(Fore.CYAN + "h - Hiragana Quiz")
    print(Fore.CYAN + "k - Katakana Quiz")
    print(Fore.CYAN + "q - Quit")

    choice = input(Fore.YELLOW + "Choose (h/k/q): ").strip().lower()

    if choice == "h":
        play_quiz(hiragana_quiz, "HIRAGANA QUIZ")
    elif choice == "k":
        play_quiz(katakana_quiz, "KATAKANA QUIZ")
    elif choice == "q":
        print(Fore.GREEN + "Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please use h, k, or q.")
