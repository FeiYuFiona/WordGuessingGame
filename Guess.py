import os
import StringDatabase


os.system('clear')                 # Clear the screen before the menu displays the first time

class Guess:
    def __init__(self):
        # point value of each letter
        self.dic = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23,
               'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
               'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99,
               's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
               'y': 1.97, 'z': 0.07}

    def test_mode(self):
        i = 1
        scoreSum = 0.00
        guessCounter = 0 # Record the number of incorrect word guess of each round of the game
        wrongLetterCount = [] # Record the number of incorrect letter guess during the game
        letterCounter = 0  # Record the number of wrongly guessed letters to calculate the scores
        score = 0.00  # Initialize the score of a single round to be 0
        scoreSum = 0.00  # Initialize the total score of the game to be 0
        status = []  # Will record the status of each round of game
        counter = []  # Will record the number of each round of game
        wordGen = []  # Will record the current word of each round of game
        badGuesses = []  # Will record the number of bad guesses of each round of game
        scores = []  # Will record the score of each round of game
        currentWord = StringDatabase.randomWord()  # This is the current word of the first round of the game
        wordGen.append(currentWord)
        counter.append(i)
        currentGuess = "----"
        lettersGuessed = " "
        condition = True
        while condition:
            os.system('clear')
            print("++")  # Display the menu
            print("++ The great guessing game")
            print("++\n")
            print("Current Word:   " + currentWord)
            print("Current Guess:   ", end="")
            print(currentGuess)
            print("Letters guessed:", end="")
            print(lettersGuessed)
            print("\ng = guess, t = tell me, l for a letter, and q to quit\n")
            option = input("Enter Option: ")
            option = option.lower()

            flag = True
            while flag:
                if option == "g":
                    word = input("\nMake your guess: ")
                    if word.lower() == currentWord:
                        print("\n@@")
                        print("@@ FEEDBACK: You're right, Einstein!")
                        print("@@\n")
                        if score == 0.00:
                            score = self.dic[currentWord[0]] + self.dic[currentWord[1]] + self.dic[currentWord[2]] + self.dic[currentWord[3]]
                        if letterCounter == 0:
                            score = score - score * 0.10 * guessCounter
                        else:
                            score = score / letterCounter
                            score = score - score * 0.10 * guessCounter
                        status.append("Success")
                        wrongLetterCount.append(letterCounter)
                        badGuesses.append(guessCounter)
                        scores.append(score)
                        currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                        wordGen.append(currentWord)
                        letterCounter = 0  # Initialize the letterCounter to be 0
                        score = 0.00  # Reset the score to be 0 for a new round of the game
                        guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                        i = i + 1  # Increment i if start a new round of the game
                        counter.append(i)
                        currentGuess = "----"  # Reset currentGuess
                        lettersGuessed = " "  # Reset lettersGuessed
                    else:
                        guessCounter = guessCounter + 1
                        print("\n@@")
                        print("@@ FEEDBACK: Try again, Loser!")
                        print("@@\n")
                    flag = False
                    Input = input("Press any key to continue... ")
                    if input == "":
                        break

                elif option == "t":
                    print("\n@@")
                    print("@@ FEEDBACK: You really should have guessed this...'mots'")
                    print("@@\n")
                    status.append("Gave up")
                    wrongLetterCount.append(letterCounter)
                    score1 = 0.00
                    score2 = 0.00
                    score3 = 0.00
                    score4 = 0.00
                    if currentGuess[0] == "-":          # The total points lost should simply be the sum
                        score1 = -self.dic[currentWord[0]]   # of the letters that have not yet been guessed/uncovered
                    if currentGuess[1] == "-":
                        score2 = -self.dic[currentWord[1]]
                    if currentGuess[2] == "-":
                        score3 = -self.dic[currentWord[2]]
                    if currentGuess[3] == "-":
                        score4 = -self.dic[currentWord[3]]
                    score = score1 + score2 + score3 + score4
                    badGuesses.append(guessCounter)
                    scores.append(score)
                    i = i + 1  # Increment i if start a new round of the game
                    counter.append(i)
                    currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                    wordGen.append(currentWord)
                    letterCounter = 0
                    score = 0.00  # Reset the score to be 0 for a new round of the game
                    guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                    currentGuess = "----"
                    lettersGuessed = " "
                    flag = False
                    input("Press any key to continue... ")
                    if input == "":
                        break

                elif option == "l":
                    letter = input("\nEnter a letter: ")
                    letter = letter.lower()
                    lettersGuessed = lettersGuessed + " " + letter
                    print("\n@@")
                    if (letter in currentWord):
                        if letter == currentWord[0]:
                            currentGuess = letter + currentGuess[1] + currentGuess[2] + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[1]:
                            currentGuess = currentGuess[0] + letter + currentGuess[2] + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[2]:
                            currentGuess = currentGuess[0] + currentGuess[1] + letter + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[3]:
                            currentGuess = currentGuess[0] + currentGuess[1] + currentGuess[2] + letter
                            score = score + self.dic[letter]
                        print("@@ FEEDBACK: Woo hoo, you found 1 letters")
                    else:
                        letterCounter = letterCounter + 1
                        print("@@ FEEDBACK: Not a single match, genius")
                    if currentWord == currentGuess: # If all the letters are caught after the current letter guess
                        print("\n@@")
                        print("@@ FEEDBACK: You have get the whole word!")
                        print("@@\n")
                        if letterCounter > 0:
                            score = score / letterCounter
                            score = score - score * 0.10 * guessCounter
                        else:
                            score = score - score * 0.10 * guessCounter
                        status.append("Success")
                        badGuesses.append(guessCounter)
                        scores.append(score)
                        wrongLetterCount.append(letterCounter)
                        i = i + 1  # Increment i if start a new round of the game
                        counter.append(i)
                        currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                        wordGen.append(currentWord)
                        letterCounter = 0
                        score = 0.00  # Reset the score to be 0 for a new round of the game
                        guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                        currentGuess = "----"
                        lettersGuessed = " "
                    flag = False
                    print("@@\n")
                    input("Press any key to continue... ")
                    if input == "":
                        break


                elif option == "q":
                    status.append("Gave up")
                    wrongLetterCount.append(letterCounter)
                    badGuesses.append(guessCounter)
                    scores.append(0.00)
                    flag = False
                    condition = False

                else:
                    option = input("\nInvalid option. Please re-enter: ")

        if len(scores) > 1:
            for x in scores:
                scoreSum = scoreSum + round(x, 2)
        return counter, wordGen, status, badGuesses, wrongLetterCount, scores, scoreSum





    # This function is exactly the same as test_mode() except it doesn't show the generated word
    def play_mode(self):
        i = 1
        scoreSum = 0.00
        guessCounter = 0  # Record the number of incorrect word guess of each round of the game
        wrongLetterCount = []  # Record the number of incorrect letter guess during the game
        letterCounter = 0  # Record the number of wrongly guessed letters to calculate the scores
        score = 0.00  # Initialize the score of a single round to be 0
        scoreSum = 0.00  # Initialize the total score of the game to be 0
        status = []  # Will record the status of each round of game
        counter = []  # Will record the number of each round of game
        wordGen = []  # Will record the current word of each round of game
        badGuesses = []  # Will record the number of bad guesses of each round of game
        scores = []  # Will record the score of each round of game
        currentWord = StringDatabase.randomWord()  # This is the current word of the first round of the game
        wordGen.append(currentWord)
        counter.append(i)
        currentGuess = "----"
        lettersGuessed = " "
        condition = True
        while condition:
            os.system('clear')
            print("++")  # Display the menu
            print("++ The great guessing game")
            print("++\n")
            print("Current Guess:   ", end="")
            print(currentGuess)
            print("Letters guessed:", end="")
            print(lettersGuessed)
            print("\ng = guess, t = tell me, l for a letter, and q to quit\n")
            option = input("Enter Option: ")
            option = option.lower()

            flag = True
            while flag:
                if option == "g":
                    word = input("\nMake your guess: ")
                    if word.lower() == currentWord:
                        print("\n@@")
                        print("@@ FEEDBACK: You're right, Einstein!")
                        print("@@\n")
                        if score == 0.00:
                            score = self.dic[currentWord[0]] + self.dic[currentWord[1]] + self.dic[currentWord[2]] + \
                                    self.dic[currentWord[3]]
                        if letterCounter == 0:
                            score = score - score * 0.10 * guessCounter
                        else:
                            score = score / letterCounter
                            score = score - score * 0.10 * guessCounter
                        status.append("Success")
                        wrongLetterCount.append(letterCounter)
                        badGuesses.append(guessCounter)
                        scores.append(score)
                        currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                        wordGen.append(currentWord)
                        letterCounter = 0  # Initialize the letterCounter to be 0
                        score = 0.00  # Reset the score to be 0 for a new round of the game
                        guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                        i = i + 1  # Increment i if start a new round of the game
                        counter.append(i)
                        currentGuess = "----"  # Reset currentGuess
                        lettersGuessed = " "  # Reset lettersGuessed
                    else:
                        guessCounter = guessCounter + 1
                        print("\n@@")
                        print("@@ FEEDBACK: Try again, Loser!")
                        print("@@\n")
                    flag = False
                    Input = input("Press any key to continue... ")
                    if input == "":
                        break

                elif option == "t":
                    print("\n@@")
                    print("@@ FEEDBACK: You really should have guessed this...'mots'")
                    print("@@\n")
                    status.append("Gave up")
                    wrongLetterCount.append(letterCounter)
                    score1 = 0.00
                    score2 = 0.00
                    score3 = 0.00
                    score4 = 0.00
                    if currentGuess[0] == "-":  # The total points lost should simply be the sum
                        score1 = -self.dic[currentWord[0]]  # of the letters that have not yet been guessed/uncovered
                    if currentGuess[1] == "-":
                        score2 = -self.dic[currentWord[1]]
                    if currentGuess[2] == "-":
                        score3 = -self.dic[currentWord[2]]
                    if currentGuess[3] == "-":
                        score4 = -self.dic[currentWord[3]]
                    score = score1 + score2 + score3 + score4
                    badGuesses.append(guessCounter)
                    scores.append(score)
                    i = i + 1  # Increment i if start a new round of the game
                    counter.append(i)
                    currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                    wordGen.append(currentWord)
                    letterCounter = 0
                    score = 0.00  # Reset the score to be 0 for a new round of the game
                    guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                    currentGuess = "----"
                    lettersGuessed = " "
                    flag = False
                    input("Press any key to continue... ")
                    if input == "":
                        break

                elif option == "l":
                    letter = input("\nEnter a letter: ")
                    letter = letter.lower()
                    lettersGuessed = lettersGuessed + " " + letter
                    print("\n@@")
                    if (letter in currentWord):
                        if letter == currentWord[0]:
                            currentGuess = letter + currentGuess[1] + currentGuess[2] + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[1]:
                            currentGuess = currentGuess[0] + letter + currentGuess[2] + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[2]:
                            currentGuess = currentGuess[0] + currentGuess[1] + letter + currentGuess[3]
                            score = score + self.dic[letter]
                        if letter == currentWord[3]:
                            currentGuess = currentGuess[0] + currentGuess[1] + currentGuess[2] + letter
                            score = score + self.dic[letter]
                        print("@@ FEEDBACK: Woo hoo, you found 1 letters")
                    else:
                        letterCounter = letterCounter + 1
                        print("@@ FEEDBACK: Not a single match, genius")
                    if currentWord == currentGuess:  # If all the letters are caught after the current letter guess
                        print("\n@@")
                        print("@@ FEEDBACK: You have get the whole word!")
                        print("@@\n")
                        if letterCounter > 0:
                            score = score / letterCounter
                            score = score - score * 0.10 * guessCounter
                        else:
                            score = score - score * 0.10 * guessCounter
                        status.append("Success")
                        badGuesses.append(guessCounter)
                        scores.append(score)
                        wrongLetterCount.append(letterCounter)
                        i = i + 1  # Increment i if start a new round of the game
                        counter.append(i)
                        currentWord = StringDatabase.randomWord()  # Randomly choose a new word for a new round of the game
                        wordGen.append(currentWord)
                        letterCounter = 0
                        score = 0.00  # Reset the score to be 0 for a new round of the game
                        guessCounter = 0  # Reset guessCounter to be 0 for a new round of the game
                        currentGuess = "----"
                        lettersGuessed = " "
                    flag = False
                    print("@@\n")
                    input("Press any key to continue... ")
                    if input == "":
                        break


                elif option == "q":
                    status.append("Gave up")
                    wrongLetterCount.append(letterCounter)
                    badGuesses.append(guessCounter)
                    scores.append(0.00)
                    flag = False
                    condition = False

                else:
                    option = input("\nInvalid option. Please re-enter: ")

        if len(scores) > 1:
            for x in scores:
                scoreSum = scoreSum + round(x, 2)
        return counter, wordGen, status, badGuesses, wrongLetterCount, scores, scoreSum




