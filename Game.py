from tkinter import *
from PIL import Image, ImageTk
import random
root = Tk()
root.config(bg="skyblue")
image_references = {}

def reset_game():
    clear_frame(frame3)
    clear_frame(frame4)
    Label_end.config(text="Select Your Choice", fg="purple")
    enable_btn()

def enable_btn():
    btn1.config(state=NORMAL, bg="pink", fg="purple")
    btn2.config(state=NORMAL, bg="pink", fg="purple")
    btn3.config(state=NORMAL, bg="pink", fg="purple")

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def compute(choice1, comp_choice):
    if choice1 == comp_choice:
        Label_end.config(text="Tie", fg="purple")
    elif((choice1 == "rock" and comp_choice == "scissors") or (choice1 == "paper" and comp_choice == "rock") or (choice1 == "scissors" and comp_choice =="paper")):
        Label_end.config(text="You Won", fg="purple")
    else:
        Label_end.config(text="Computer Won", fg="purple")
def comp_choice_rock():
    image1 = Image.open("rock-small-image.jpg")
    p1 = ImageTk.PhotoImage(image1)
    image_rock = Label(frame4, image=p1)
    image_rock.grid()
    image_references['comp_rock'] = p1
    return "rock"

def comp_choice_paper():
    image2 = Image.open("paper-small-image.jpg")
    p2 = ImageTk.PhotoImage(image2)
    image_paper = Label(frame4, image=p2)
    image_paper.grid()
    image_references['comp_paper'] = p2
    return "paper"

def comp_choice_scissors():
    image3 = Image.open("scissors-small-image.jpg")
    p3 = ImageTk.PhotoImage(image3)
    image_scissors = Label(frame4, image=p3)
    image_scissors.grid()
    image_references['comp_scissors'] = p3
    return "scissors"

def choice_rock():
    choice1 = "rock"
    btn1.config(bg="green", fg="white")
    image1 = Image.open("rock-small-image.jpg")
    p1 = ImageTk.PhotoImage(image1)
    image_rock = Label(frame3, image=p1)
    image_rock.grid()
    image_references['user_rock'] = p1
    comp_choice = comp_chance()
    disable_btn()
    compute(choice1, comp_choice)

def choice_paper():
    choice1 = "paper"
    btn2.config(bg="green", fg="white")
    image2 = Image.open("paper-small-image.jpg")
    p2 = ImageTk.PhotoImage(image2)
    image_paper = Label(frame3, image=p2)
    image_paper.grid()
    image_references['user_paper'] = p2
    comp_choice = comp_chance()
    disable_btn()
    compute(choice1, comp_choice)

def choice_scissor():
    choice1 = "scissors"
    btn3.config(bg="green", fg="white")
    image3 = Image.open("scissors-small-image.jpg")
    p3 = ImageTk.PhotoImage(image3)
    image_scissor = Label(frame3, image=p3)
    image_scissor.grid()
    image_references['user_scissors'] = p3
    comp_choice = comp_chance()
    disable_btn()
    compute(choice1, comp_choice)

def disable_btn():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)

def comp_chance():
    arr = ["rock", "paper", "scissors"]
    choice = random.choice(arr)
    if choice == "rock":
        return comp_choice_rock()
    elif choice == "paper":
        return comp_choice_paper()
    else:
        return comp_choice_scissors()

root.geometry("555x444")
frame1 = Frame(root, bg="skyblue")
frame1.pack(fill=X, pady=20)
label1 = Label(frame1, text="Rock-Paper-Scissors", bg="skyblue", fg="purple", font=("Arial",20,"bold")).pack()
frame2 = Frame(root)
frame2.pack(fill=Y)

img1 = Image.open("rock-small-image.jpg")
photo1 = ImageTk.PhotoImage(img1)
rock_img = Label(frame2, image=photo1)
rock_img.grid(row=0, column=0, padx=20, pady=20)

img2 = Image.open("paper-small-image.jpg")
photo2 = ImageTk.PhotoImage(img2)
paper_img = Label(frame2, image=photo2)
paper_img.grid(row=0, column=1, padx=20, pady=20)

img3 = Image.open("scissors-small-image.jpg")
photo3 = ImageTk.PhotoImage(img3)
scissor_img = Label(frame2, image=photo3)
scissor_img.grid(row=0, column=2, padx=20, pady=20)

btn1 = Button(frame2, text="Rock", bg="pink", fg="purple", activebackground="green",
              activeforeground="white", padx=20, font=("Arial", 15, "bold"),
              command=choice_rock)
btn1.grid(row=2, column=0, padx=10, pady=10)
btn2 = Button(frame2, text="Paper", bg="pink", fg="purple", activebackground="green", activeforeground="white", padx=20,
              font=("Arial", 15, "bold"), command=choice_paper)
btn2.grid(row=2, column=1, padx=10, pady=10)
btn3 = Button(frame2, text="Scissors", bg="pink", fg="purple", activebackground="green", activeforeground="white",
              padx=20, font=("Arial", 15, "bold"), command=choice_scissor)
btn3.grid(row=2, column=2, padx=10, pady=10)

you_label = Label(frame2, text="You", fg="purple", font=("Arial", 30, "bold"))
you_label.grid(row=3, column=0, padx=10, pady=10)
comp_label = Label(frame2, text="Comp", fg="purple", font=("Arial", 30, "bold"))
comp_label.grid(row=3, column=2, padx=10, pady=10)


frame3 = Frame(frame2, height=100, width=100, background="pink")
frame3.grid(row=4, column=0, padx=10, pady=20)
frame4 = Frame(frame2, height=100, width=100, background="pink")
frame4.grid(row=4, column=2, padx=10, pady=20)

Label_end = Label(frame2, text="Select Your Choice", bg="pink", fg="purple",
                  font=("Arial", 20), padx=15, pady=10)
Label_end.grid(row=5, column=1, padx=10, pady=20)
restart_btn = Button(frame2, text="Restart", fg="blue", font=("Arial", 15), command=reset_game)
restart_btn.grid(row=6, column=1,padx=10,pady=10)

root.mainloop()
