#hungman game
import random
words=["Apple","Mango","Kite","Python","Java"]
secret_word=random.choice(words).lower()
display=[]
for letter in secret_word:
    display.append("_")
print(display)
lives=6
print("Welcome to Hangman!")
print("Word:"," ".join(display))
while "_" in display and lives>0:
    guess=input("Guess a letter:").lower()
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                display[i]=guess
    else:
        lives-=1
        print("Wrong guess! Lives left:",lives)

print("Word:"," ".join(display))
if "_" not in display:
    print("You won the word was:",secret_word)
else:
    print("You lost.The word was:",secret_word)