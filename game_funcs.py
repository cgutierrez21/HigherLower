import game_data
import random

def choose_person(choice, person=" "):
    people = game_data.data
    index_num = random.randint(0,49)

    name = people[index_num]['name']
    description = people[index_num]['description']
    country = people[index_num]['country']
    print(f"Person/Organization {choice}: {name}, {description}, from {country}")

    if name == person:
        choose_person(choice, person)

    return name, people[index_num]["follower_count"]


def player_guess():
    print("Who has more more followers?")
    return input("Type A or B: ").upper()


def guess_a(person_a, followers_a, person_b, followers_b, games_won):
    if followers_a > followers_b:
        print("\nCorrect!")
        print(f"{person_a} has {followers_a} million followers and {person_b} has {followers_b} million followers.\n")
        games_won += 1
        return games_won

    else:
        print("\nWrong!")
        print(f"{person_a} has {followers_a} million followers and {person_b} has {followers_b} million followers.\n")
        return games_won


def guess_b(person_a, followers_a, person_b, followers_b, games_won):
    if followers_a > followers_b:
        print("\nWrong!")
        print(f"{person_a} has {followers_a} million followers and {person_b} has {followers_b} million followers.\n")
        return games_won

    else:
        print("\nCorrect!")
        print(f"{person_a} has {followers_a} million followers and {person_b} has {followers_b} million followers.\n")
        games_won += 1
        return games_won


def continue_play():
    print("Continue playing?")
    answer = input("Type y for yes or n for no: ").lower()
    if answer == "n":
        return False

    return True

