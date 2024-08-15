import os
from Guess import Guess
import requests
import smtplib

class Game:
    result = 0

    def __init__(self):
        pass

    

    def play_report(self):
        index = 0
        game = Guess()
        counter, wordGen, status, badGuesses, wrongLetterCount, scores, scoreSum = game.play_mode()
        os.system('clear')

        print("++")
        print("++ Game Report")
        print("++\n")
        print("Game        Word        Status        Bad Guesses        Missed Letters        Score")
        print("----        ----        ------        -----------        --------------        -----")

        while index < len(counter) - 1:
            print(str(counter[index]).ljust(12), end="")
            print(wordGen[index].ljust(12), end="")
            print(status[index].ljust(14), end="")
            print(str(badGuesses[index]).ljust(19), end="")
            print(str(wrongLetterCount[index]).ljust(22), end="")
            print("{:.2f}".format(scores[index], 2))
            index += 1

        result = "{:.2f}".format(scoreSum)
        print("\nFinal Score: ", end="")
        print(result)

        # Send SMS
        my_email = os.environ.get("email_From")
        userPassword = os.environ.get("password")
        email_To = os.environ.get("email_To")
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            subject = "Score report"
            body = f"The final score is {result}"
            message = f"Subject: {subject}\n\n{body}"
            connection.starttls()
            connection.login(user = my_email, password = userPassword)
            connection.sendmail(from_addr = my_email, 
                                to_addrs = email_To, 
                                msg = message)





    def test_report(self):
        index = 0
        game = Guess()
        counter, wordGen, status, badGuesses, wrongLetterCount, scores, scoreSum = game.test_mode()
        os.system('clear')

        print("++")
        print("++ Game Report")
        print("++\n")
        print("Game        Word        Status        Bad Guesses        Missed Letters        Score")
        print("----        ----        ------        -----------        --------------        -----")

        while index < len(counter) - 1:
            print(str(counter[index]).ljust(12), end="")
            print(wordGen[index].ljust(12), end="")
            print(status[index].ljust(14), end="")
            print(str(badGuesses[index]).ljust(19), end="")
            print(str(wrongLetterCount[index]).ljust(22), end="")
            print("{:.2f}".format(scores[index], 2))
            index += 1

        result = "{:.2f}".format(scoreSum)
        print("\nFinal Score: ", end="")
        print(result)


        # Send SMS
        my_email = os.environ.get("email_From")
        userPassword = os.environ.get("password")
        email_To = os.environ.get("email_To")
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            subject = "Score report"
            body = f"The final score is {result}"
            message = f"Subject: {subject}\n\n{body}"
            connection.starttls()
            connection.login(user = my_email, password = userPassword)
            connection.sendmail(from_addr = my_email, 
                                to_addrs = email_To, 
                                msg = message)

    

    