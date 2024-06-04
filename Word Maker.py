#Modded Word Maker
import random

def vow():
    global word
    word += vowels[random.randint(1, len(vowels)) - 1]
def con():
    global word
    word += consonants[random.randint(1, len(consonants)) - 1]
letters = ['b', 'c', 'd', 'd', 'd', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'j', 'k', 'j', 'k', 'j', 'k', 'l', 'm', 'n', 'n', 'p', 'q', 'r', 's', 't', 't', 't', 't', 'v', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'a', 'a', 'e', 'e', 'i', 'i', 'i', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def makeWord():
    global word
    word = letters[random.randint(1, len(letters)) - 1]
    choice = 0
    for i in range(10):
        if word[i] in vowels:
            if len(word) > 1 and word[i - 1] in vowels:
                con()
            else:
                choice = random.randint(1, 2)
                if choice == 1:
                    vow()
                else:
                    con()
        else:
            if len(word) > 1 and word[i - 1] in consonants:
                vow()
            else:
                choice = random.randint(1, 5)
                if choice == 1:
                    con()
                else:
                    vow()
        if random.randint(3, 12 - i) < 4 and len(word) > 2:
            break
    print(word)
    
while True:
    input()
    makeWord()