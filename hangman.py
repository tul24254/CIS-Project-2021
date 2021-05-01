#Hangman on Python by Justin Schneider, CIS 1051 Spring 2021
import random
def randword():
    while True:
        uppercase = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        bank = open('words.txt').readlines()
        keyword = random.choice(bank)
        chars = list(keyword)
        if uppercase not in chars:
            keyword = keyword[:-1]
            keyword.lower()
            return keyword

def guess(keyword):
    letters = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    while True:
        print()
        print("Guess a letter")
        guess = input()
        if guess in letters:
            break
        print("That's not a letter")
    if guess not in keyword:
        return guess
    char = list(keyword)
    charnum = []
    for i in range(len(char)):
        if char[i] == guess:
            charnum += [i]
    return charnum


def hangmain():
    letters = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    keyword =randword()
    guessword = ''
    blank = "_ "
    hyphen = '- '
    top = "||-------------"
    side_rope = "||            |"
    head = "||            O"
    left = "||            |\\"
    arms = "||           /|\\"
    leg = "||             \\"
    legs = "||           / \\"
    base = "||______________"
    side = "||"
    wrong_counter = 0
    wrong = []
    correct = []
    for i in range(len(keyword)):
        char = keyword[i]
        if char == "-":
            guessword += hyphen
        else:
            guessword += blank
    print("Welcome to Hangman!")
    print("Guess the letters in the word to win. Guess too many wrong, and you lose.")
    print("Your word has ", len(keyword), "letters. Good Luck!")
    print()
    print(guessword)
    #print(keyword)
    while True:
        guess1 = guess(keyword)
        if guess1 in letters:
            if guess1 not in wrong:
                wrong += guess1
                print(guess1,"is not in the word!")
                guess1 = []
                wrong_counter += 1
            else:
                print("You already guessed that!")
                guess1 = []
        correct += guess1
        print()
        print(top)
        print(side_rope)
        print(side_rope)
        if wrong_counter >0:
            print(head)
        else:
            print(side)
        if wrong_counter == 2:
            print(side_rope)
            print(side_rope)
        elif wrong_counter == 3:
            print(left)
            print(side_rope)
        elif wrong_counter >3:
            print(arms)
            print(side_rope)
        else:
            print(side)
            print(side)
        if wrong_counter == 5:
            print(leg)
        elif wrong_counter>5:
            print(legs)
        else:
            print(side)
        print(side)
        print(side)
        print(base)
        guessword = ''
        for i in range(len(keyword)):
            if i in correct:
                guessword += keyword[i]
                guessword += ' '
            elif char == "-":
                guessword += hyphen
            else:
                guessword += blank
        print()
        print(guessword)
        if blank not in guessword:
            print()
            print("Great Job! You got the word!")
            break
        if wrong_counter>0:
            print()
            print("Here are your wrong guesses so far:")
            print(wrong)
        if wrong_counter >= 6:
            print()
            print("Sorry! You guessed too many wrong letters! You lost!")
            print("The word was", keyword)
            break
def play():
    hangmain()
    yes = 'YES','Yes','yes','y','Y'
    no = 'NO','No','no','n','N'
    while True:
        inp = input("Want to play again?")
        if inp in yes:
            hangmain()
        if inp in no:
            print("Thank you for playing!")
            break
            
play()
