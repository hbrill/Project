from tkinter import *
from tkinter import messagebox

print("Rules: Choose a role, detective or criminal, and try to accomplish your goals before losing all of your merit")
print("Merit: Your score throughout the game. You will have an initial 10. Depending on your choices, you will lose or win merit")
print("Once you lose all merit, you lose the game. You will only win the game once you've accomplished your goal")

###
# The next few lines will create two buttons, one for Detective, one for Criminal. This will just display a message box. It won't necessarily affect the game
###

# The next function will be called when creating the buttons for each option

def detective():
    msg = messagebox.showinfo("Detective", "You're the detective. Solve the case!")
def criminal():
    msg = messagebox.showinfo("Criminal", "You're the criminal. Get away!")
    
top = Tk()
top.geometry("200x200") # This command will create the window with the dimensions 200x200 for height and width

### The next lines will create the two buttons and then execute it all when calling top.mainloop() ###
B = Button(top, text="Detective", command=detective) 
B.place(x=25, y=100)
A = Button(top, text="Criminal", command=criminal)
A.place(x = 120, y=100)
top.mainloop()


### Then I created gameOver and goalMeet.
# gameOver will just end the game regardless of whether the player won or lost.
### goalMeet will determine whether the player did either. If goalMeet == Success then the player will win. If it's == Failed then the player loses.

gameOver = False
goalMeet = " "

choice = str(input("What character do you want to play as before we begin? Enter C for Criminal or D for Detective: "))

if choice == "D" or choice == "d":
    print("You've arrived to the crime scene. There has been a robbery and many valuable items are missing. What do you want to do first?")
    print("a) Check surveillance cameras in the back of the building", "               b) Examine the crime scene in looks for any physical evidence")
    choice = str(input())
    if choice == "a":
        print("You go to the backroom. There are multiple screens but none of the cameras are working. They seem to have been shut down prior to the robbery.")
        print("You hear a sound coming from the front of the building. What do you do?")
        print("a) Go to the direction the sound came from                              b) Go on the opposite direction")  
        choice = str(input())
        if choice == "a":
            print("It was a distraction and you fell for it. The criminal has escaped. You lose.")
            gameOver = True
            goalMeet = "Failed"
        elif choice == "b":
            print("The criminal has tried to escape but you've caught them right on time. Good job! You win!")
            goalMeet = "Success"
    elif choice == "b":
        print("As you examine it, you hear a loud thud resonate in the room. It's coming from the opposite side from where you at. What do you do?")
        print("a) Go outside and check if there's someone                    b) Hide behind the counter to see what happens and call for backup")
        choice = str(input())
        if choice == "a" or choice == "A":
             print("Catch the criminal before they get away!")
             print("Use left and right arrows to move your character around. Use barspace to shoot. If you get the opponent, you win!")
             import mods.py ### mods.py imports the minigame I created with pygame especifically for this option ###
        elif choice == "b" or choice == "B":
             print("You hear a sound and when you go outside, the criminal is running out the window. Catch them before they get away!")
             print("Use left and right arrows to move your character around. Use barspace to shoot. If you get the opponent, you win!")
             import mods.py
             
elif choice == "C" or choice == "c":
    print("You're in the store. There are some expensive rings in one side of the room and a gold watch on the left side. What direction do you want to go in?")
    print("a) Left            b)Right")
    choice = str(input())
    if choice == "a" or choice == "A":
        print("You go to the left side of the store and take some goods, but as you do you hear footsteps outside. What do you do?")
        print("a)Sneak out through the window              b)Stay there and hide from whoever is coming inside")
        choice = str(input())
        if choice == "a" or choice == "A":
            print("You've sneaked out, but you make a loud sound while doing so. The detective comes to the back and arrests you. You lose!")
            gameOver = True
            goalMeet = "Failed"
        elif choice == "b" or choice == "B":
            print("You hide behind the counter. Someone comes in the store, they look like a police officer and they're examining the scene.")
            print("a) Stay quiet, they won't notice your presence         b) Try to leave by the front door")
            choice = str(input())
            if choice == "a" or choice == "A":
                print("The officer goes to the back of the room. While they're at it, you sneak out of the store using the window and you manage to escape. Great job!") 
                gameOver = True
                goalMeet = "Success"
            elif choice == "b" or choice == "B":
                print("You try to escape by using the front door, but the officer has called for backup and on your way out, you're surrounded by two police cars.")
                print("You got arrested. You lose.")
                gameOver = True
                goalMeet = "Failed"
              
    elif choice == "b" or choice == "B":
         print("You go to the right side. The rings looks very expensive, but you won't be able to take them without making some noise.")
         print("a) Take them nonetheless, you're alone            b) Be wary, you might not be alone. Wait a couple minutes.")
         choice = str(input())
         if choice == "a" or choice ==  "A":
              print("You try to take the rings but someone goes inside the store. What is the best thing to do now?")
              print("a) Stay where you are, they probably didn't hear a thing                      b) Sneak out with what you have")
              if choice == "a" or choice == "A":
                  print("You were wrong. The person inside heard the noise and they followed it. Now you've been arrested. You lose.")
                  gameOver = True
                  goalMeet = "Failed"
              elif choice == "b" or choice == "B":
                  print("You escape trhough the window. You made some noise on your way out. Now you have to take the best route to lose the cop")
                  print("a) Run towards the woods       b) Hide somewhere near the building        c)Run around the streets, hiding in between the houses")
                  choice = str(input())
                  if choice == "a" or choice == "A":
                      print("You took the most obvious path. The officer and some backup follow after you and soon they catch up. You're arrested. You lose.")
                      gameOver = True
                      goalMeet = "Failed"
                  elif choice == "b" or choice == "B":
                      print("The cops think you ran either to the streets or to the woods and they split into two teams.")
                      print("You take advantage of that and manage to sneak out using a hidden shortcut. Great job!")
                      gameOver = True
                      goalMeet = "Success"
                  elif choice == "c" or choice == "C":
                      print("As you run around those houses while being chased by the cops, you spot a bycycle. Do you want to try it or keep running?")
                      print("a) Keep running, I'll lose the cops eventually         b) Try getting on the bycycle, is faster")
                      if choice == "a" or choice == "A":
                            print("You run into a dark alley, but there's no way out. You're now surrounded by the cops. You get arrested. You lose!")
                            gameOver = True
                            goalMeet = "Failed"
                      elif choice == "b":
                            print("You never learned how to ride a bycycle, so you fall on the floor and the cops catch up with you. You lose!")
                            gameOver = True
                            goalMeet = "Failed"
         elif choice == "b" or choice == "b":
              print("After a couple minutes, someone comes inside too, but they go to the back of the building. Do you want to go for the rings now?")
              print("a)Yes, let's take a chance              b) No, let me leave with what I have collected, I will get caught")
              choice = str(input())
              if choice == "a" or choice == "A":
                  print("You try going for the rings, but the person came back to the main room. You have no time to escape")
                  print("Shortly, backup arrives at the scene. You're now surrounded by multiple police officers. You failed!")
                  gameOver = True
                  goalMeet = "Failed"
              elif choice == "b" or choice == "B":
                  print("Great choice. You manage to slip out of the crime scene and are now on your way to your boss. You sure will get a good pay after this succesful mission. Congratulations!")
                  gameOver = True
                  goalMeet = "Success"

if (gameOver == True) and (goalMeet == "Success"):
    print("Winner Winner Chicken Dinner!")
elif (gameOver == True) and (goalMeet == "Failed"):
    print("Loser Loser Get a Rooster")
