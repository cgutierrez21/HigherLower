import art
import game_data
import game_funcs as gf
import os

os.system("clear")
game_on = True
wins = 0

while game_on:
    people = game_data.data

    print(art.logo)

    person_a, followers_a = gf.choose_person("A")

    print(art.vs)

    person_b, followers_b = gf.choose_person("B", person_a)

    unacceptable_guess = True

    while unacceptable_guess:
        guess = gf.player_guess()

        if guess == "A":
            wins = gf.guess_a(person_a, followers_a, person_b, followers_b, wins)
            unacceptable_guess = False

        elif guess == "B":
            wins = gf.guess_b(person_a, followers_a, person_b, followers_b, wins)
            unacceptable_guess = False

        else:
            print("Incorrect imput.\nTry again.\n")

    game_on = gf.continue_play()

    os.system("clear")
    
print("Thank you for playing.")
print(f"You guessed correctly a total of {wins} times.")
