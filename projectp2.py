from tkinter import *
from tkinter import messagebox

print("Rules: Choose a role, detective or criminal, and try to accomplish your goals before losing all of your merit")
print("Merit: Your score throughout the game. You will have an initial 10. Depending on your choices, you will lose or win merit")
print("Once you lose all merit, you lose the game. You will only win the game once you've accomplished your goal")



def detective():
    msg = messagebox.showinfo("Detective", "You're the detective. Solve the case!")
def criminal():
    msg = messagebox.showinfo("Criminal", "You're the criminal. Get away!")
top = Tk()
top.geometry("200x200")
B = Button(top, text="Detective", command=detective)
B.place(x=25, y=100)
A = Button(top, text="Criminal", command=criminal)
A.place(x = 120, y=100)

top.mainloop()

character = str(input("What character do you want to play as before we begin? Enter C for Criminal or D for Detective: "))

if character == "D" or character == "d":
    print("You've arrived to the crime scene. There has been a robbery and many valuable items are missing. What do you want to do first?")
    print("a) Check surveillance cameras in the back of the building", "               b) Examine the crime scene in looks for any physical evidence")
    choice = str(input())
    if choice == "a":
          print("You go to the backroom. There are multiple screens but none of the cameras are working. They seem to have been shut down prior to the robbery.")
          print("Time has been wasted. You lost 3 merit.")
          merit = 7
          print("You hear a sound coming from the front of the building. What do you do?")
          print("a) Go to the direction the sound came from                              b) Go on the opposite direction")  
          choice = str(input())
          if choice == "a":
              print("It was a distraction and you fell for it. The criminal has escaped. You lose.")
              merit = 0
    elif choice == "b":
        print("As you examinee it, you hear a loud thud resonate in the room. It's coming from the opposite side from where you at. What do you do?")
        print("a) Stay where you are, waiting to see if someone is coming                     b) Hide behind the counter to see what happens and call for backup                    c)Go torwards the sound")
        choice = str(input())
if merit == 0:
    msg = messagebox.showinfo("Click for result", "YOU LOST")
        
