import random


word_list = []

with open('four_letters.txt', 'r') as file:
    for line in file:
        for word in line.split():
            word_list.append(word)

def randomWord():
    return random.choice(word_list)

