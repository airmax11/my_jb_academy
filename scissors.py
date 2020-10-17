# Write your code here

from random import choice

WIN_LOST_OPTION = ["rock", "scissors", "paper"]
comp = "Sorry, but the computer chose"
user = "Well done. The computer chose <option> and failed"
draw = "Sorry, but the computer chose"


map_win = {"Rock": ["Fire", "Scissors", "Snake", "Human", "Tree", "Wolf", "Sponge"],
           "Fire": ["Scissors", "Snake", "Human", "Tree", "Wolf", "Sponge", "Paper"],
           "Scissors": ["Snake", "Human", "Tree", "Wolf", "Sponge", "Paper", "Air"],
           "Snake": ["Human", "Tree", "Wolf", "Sponge", "Paper", "Air", "Water"],
           "Human": ["Tree", "Wolf", "Sponge", "Paper", "Air", "Water", "Dragon"],
           "Tree": ["Wolf", "Sponge", "Paper", "Air", "Water", "Dragon", "Devil"],
           "Wolf": ["Sponge", "Paper", "Air", "Water", "Dragon", "Devil", "Lightning"],
           "Sponge": ["Paper", "Air", "Water", "Dragon", "Devil", "Lightning", "Gun"],
           "Paper": ["Air", "Water", "Dragon", "Devil", "Lightning", "Gun", "Rock"],
           "Air": ["Water", "Dragon", "Devil", "Lightning", "Gun", "Rock", "Fire"],
           "Water": ["Dragon", "Devil", "Lightning", "Gun", "Rock", "Fire", "Scissors"],
           "Dragon": ["Devil", "Lightning", "Gun", "Rock", "Fire", "Scissors", "Snake"],
           "Devil": ["Lightning", "Gun", "Rock", "Fire", "Scissors", "Snake", "Human"],
           "Lightning": ["Gun", "Rock", "Fire", "Scissors", "Snake", "Human", "Tree"],
           "Gun": ["Rock", "Fire", "Scissors", "Snake", "Human", "Tree", "Wolf"]}


def win_lost_draw(user_select, comp_select):
    if user_select == comp_select:
        print(f"There is a draw ({comp_select})")
        return 50
    elif comp_select.capitalize() in map_win[user_select.capitalize()]:
        print(f"Well done. The computer chose {comp_select} and failed")
        return 100
    else:
        print(f"Sorry, but the computer chose {comp_select}")
        return 0


def option():
    game_option = input().split(sep=",")
    print("Okay, let's start")
    if len(game_option) > 1:
        return game_option
    return WIN_LOST_OPTION


def user_name():
    print("Enter your name: ", end="")
    name_1 = input()
    print("Hello,", name_1)
    return name_1


def read_file(name):
    file_name = open("rating.txt", "r+")
    for count in file_name:
        if count.split(" ")[0] == name:
            return int(count.split(" ")[1])
    return 0


name = user_name()
game_opt = option()
score = read_file(name)

while True:
    inp = input()
    c_choice = choice(game_opt)
    if inp == "!exit":
        print("Bye!")
        break
    if inp == "!rating":
        print("Your rating: ", score)
        continue
    if inp not in game_opt:
        print("Invalid input")
        continue
    score += win_lost_draw(inp, c_choice)
