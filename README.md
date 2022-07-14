# Pong
A simple pong game made with Python and Raylib Python.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```
```
python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                  (project root folder)
+-- game              (source code for game with specific game classes)
  +-- casting         (various actor classes)
  +-- directing       (director and scene manager classes)
  +-- scripting       (various action classes)
  +-- services        (various service classes)
+-- __main__.py       (entry point for program)
+-- constants.py      (game constants)
+-- README.md         (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Nikita Wong (iamspecial19@gmail.com)
* Stephanie Clark (sclark@inventoryshield.com)
* Kaden Brown (bro22001@byui.edu)

## Contribution
---
* Nikita Wong - Create new classes for ball, paddle, and line, but it didn't work.
* Stephanie Clark - Modify the paddle to make it work.
* Kaden Brown - Make the scores for both players and fix the collide borders action.