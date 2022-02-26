import GuessGame
from GuessGame import *
import Score


def welcome():
    name = str(input('What is your name'))
    print("Hello " + name + " and welcome to the World of Games ( WoG )\nHere you can find many cool games to play.")

    list_of_games = ["1 . Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
                     "2 . Guess Game - guess a number and see if you chose like the computer",
                     "3 . Currency Roulette - try and guess the value of a random amount of USD in ILS"]
    for games in list_of_games:
        print(games)
    # Score.get_player_name(name)
    load_game(name)
    return name


def load_game(name):
    print("Which Game You Want To Play ? \n")
    game_choice = int(input(''))
    print(game_choice)

    if game_choice == 1:
        print("Memory Game , Nice Choice ! ")
    elif game_choice == 2:
        print("Guess Game , Nice Choice ! ")
    elif game_choice == 3:
        print("Currency Roulette , Nice Choice ! ")

    print("Please choose game difficulty from 1 to 5: ? \n")
    difficulty = int(input(''))
    print(difficulty)

    if difficulty == 1:
        print("Difficulty Level : Easier Than Easy ! ")
    elif difficulty == 2:
        print("Difficulty Level : Beginner ! ")
    elif difficulty == 3:
        print("Difficulty Level : Standard ! ")
    elif difficulty == 4:
        print("Difficulty Level : Hard ! ")
    elif difficulty == 5:
        print("Difficulty Level : Expert ! ")

    if game_choice == 2:
        GuessGame.play(difficulty)
        Score.add_score(difficulty)
    return game_choice, difficulty
