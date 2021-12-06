from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

root.title("Endless Pokemon Card Game")
root.geometry("600x600")

root.configure(background = "orange")

img1 =ImageTk.PhotoImage(Image.open ("Daco_4381838.png"))

img2 =ImageTk.PhotoImage(Image.open ("PngItem_240626.png"))

img3 =ImageTk.PhotoImage(Image.open ("PngItem_845879.png"))

pokemon_ball =ImageTk.PhotoImage(Image.open ("pokeball-png-45330.png"))

image_list = [img1, img2, img3]
pokemon_power_list = ["300", "250", "160"]

player1 = Label(root, text = "Player 1", bg = "red", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = "red", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "royal blue", fg = "white") 
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "royal blue", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

player1_score = ""

def player1():
    global player1_score
    random_no = random.randint(0, 2)
    random_pokemon = ([image_list],[random_no])
    label["image"] = random_pokemon
    
    random_pokemon_score = (["pokemon_power_list"],[random_no])
    player1_score = player1_score + random_pokemon_score
    player1_score_label["text"] = str(player1_score)

btn1 = Button(root, image = pokemon_ball, command = player1)
btn1.place(relx = 0.1, rely = 0.8, anchor = CENTER)

player2_score = ""

def player2():
    global player2_score
    random_no2 = random.randint(0, 2)
    random_pokemon2 = (["image_list"],[random_no2])
    label["image"] = random_pokemon2
    
    random_pokemon_score2 = (["pokemon_power_list"],[random_no2])
    player2_score = player2_score + random_pokemon_score2
    player2_score_label["text"] = str(player2_score)

btn2 = Button(root, image = pokemon_ball, command = player2)
btn2.place(relx = 0.9, rely = 0.8, anchor = CENTER)

root.mainloop()