import tkinter as tk
from tkinter import *
import random
import os
#from PIL import Image, ImageTk

game = tk.Tk()
game.configure(bg="light blue")
game.geometry("650x550")
game.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,20)
result.set("Guess a number between 1 to 20 ")
chances.set(7)
chances1.set(chances.get())

def fun():
  chances1.set(chances.get())
  if chances.get()>0:

    if choice.get() > 20 or choice.get()<0:
      result.set("You just lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("Congratulation YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was too low: Guess a number higher ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set(
          "Your guess was too High: Guess a number Lower ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set(
         "Game Over You Lost")

def restart():
  no=random.randint(1,20)
  result.set("Guess a number between 1 to 20 ")
  chances.set(7)
  chances1.set(chances.get())

ent1 = Entry(game, textvariable=choice, width=3,
             font=('Ubuntu', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(game, textvariable=result, width=50,
             font=('Courier', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(game, text=chances1, width=2,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(game, text='Guess a number between 1 to 20 ',
            font=("Courier", 25), relief=GROOVE)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(game, text='Remaninig Chances',
             font=("Courier", 25), relief=GROOVE)
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(game, width=8, text='TRY', font=(
    'Courier', 25), command=fun, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = tk.Button(game, text='stop', width=40, command=game.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)

reset = tk.Button(game, text='Restart', width=40, command=restart,
                 bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)

game.mainloop()