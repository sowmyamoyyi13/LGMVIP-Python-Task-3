from tkinter import *
from PIL import Image, ImageTk
from random import randint

image_path = 'User_scissor.png'

# main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img = ImageTk.PhotoImage(Image.open('User_rock.png'))
paper_img = ImageTk.PhotoImage(Image.open('User_paper.png'))
scissor_img = ImageTk.PhotoImage(Image.open('User_scissor.png'))
rock_img_comp = ImageTk.PhotoImage(Image.open('rock.png'))
paper_img_comp = ImageTk.PhotoImage(Image.open('paper.png'))
scissor_img_comp = ImageTk.PhotoImage(Image.open('scissor.png'))

image = Image.open('User_scissor.png')
user_scissor_img = ImageTk.PhotoImage(image)

# insert picture
user_label = Label(root, image=user_scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
playerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)

# update messages
def update_Message(x):
    msg["text"] = x

# update user score
def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

# update Computer score    
def updateComputerScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)
    
    # check Winner
    checkWin(player_choice, compChoice)

# check Winner
def checkWin(player, computer):
    if player == computer:
        update_Message("It's a tie! Try again.")
    elif player == "rock":
        if computer == "paper":
            update_Message("You lose! Paper covers rock.")
            updateComputerScore()
        else:
            update_Message("You win! Rock crushes scissors.")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            update_Message("You lose! Scissors cut paper.")
            updateComputerScore()
        else:
            update_Message("You win! Paper covers rock.")
            updateUserScore()
    elif player == "scissors":
        if computer == "rock":
            update_Message("You lose! Rock breaks scissors.")
            updateComputerScore()
        else:
            update_Message("You win! Scissors cuts rock.")
            updateUserScore()
    else:
        pass

choices = ["rock", "paper", "scissors"]

# updating choices
def update_choice(x):
    global player_choice
    player_choice = x
    
    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)

# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: update_choice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: update_choice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white", command=lambda: update_choice("scissor"))

rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

root.mainloop()
