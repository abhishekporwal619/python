import random

print("hangman\n")
text=["hero","zero","nero","kero"]
random_text=random.choice(text)


choice = ["_","_","_","_"]
a=0
game_over = False
lives=24
while not game_over:
    a = 0
    
    user_letter=input("enter letter:").lower()
    for letter in random_text:
        
        if letter == user_letter:
            choice[a] = letter
        
            print("right")
        
        else:
            lives -=1
        
        
        a=a+1
    print(choice)

    if "_" not in choice:
        game_over = True
        print("You win")
    if lives < 0:
        game_over = True
        print("You Lose")