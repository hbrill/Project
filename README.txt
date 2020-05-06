PROJECT SUMMARY by Heather Brillant

The purpose of my project was creating a game, based on user decision and input. The original game contains some Tkinter(though it does not move forward with buttons, as I initially planned on doing). Most of the original game is based on if statements and variables. However, I included a minigame within it to make the coding for this project more interesting for me. Even though the visuals are very basic, pygame offered more of a challenge than Tkinter, so I decided to use pygame to create the minigame that the user would be able to play only if they make certain choices. 
I had never worked with pygame before, so I faced some challenges.

1. Understanding how to build the program and the gameloop function. Mostly because the variables that I used for position had to be decleared inside gameloop, even though I had created the functions prior to that.
2. Some commands, like pygame.display.update or pygame.time.Clock. This helped me understand FPS and how it affects your game display.
3. Rectangle collision. I thought that just by overlapping the rectangles some way would
+-+ give me the results I wanted, but I had to analyze and understand how position works.
4. Overall, I was not familiar with pygame commands so I had to look at some tutorials online.

As I worked through it I was able to insert my own ideas into this project, and there are some other things that I would have added if I had more time:

1. Some sound effects, throughout the game, when the user shoots and when winning the game
2. More boundaries, obstacles. Maybe something that gets in the player's way as they try to get the opponent 
3. A pause button and a timer
4. A similar game for the criminal gameplay
5. A bullet limit, something like a bulletCount variable and a loop that checks how many bullets the player has left until they run out, then it's game over.

The modules needed to run this game are:
- Tkinter
- time
- pygame
- Not modules, but some PNG files need to be downloaded as well. 

Note: The minigame code contains some variables that aren't necessarily referred throughout the code. Those are there because of the other ideas that I am trying to add to this game but due to time limitations, won't be able to pass in with the whole project.

Once the minigame executes, the controlls are basically just right and left arrow to move the character, spacebar to shoot.

