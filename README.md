# Snake

## Content

This code is an implementation of the classic _Snake_ game in Python, utilizing the turtle graphical module. Initially, essential modules are imported: **turtle** for creating and manipulating game graphics, **time** for controlling delays, which allows for regulating the speed of the snake, and random for randomly placing the snake's food. Then, basic game parameters are set, such as the delay between updates (_delay_), the distance the snake moves (_dist_), and the dimensions of the game screen (width and height).

The code then proceeds to configure the visual setup of the game, creating a screen object using **turtle.Screen()** and configuring its title, background color, and dimensions. Turning off automatic screen updates with **wn.tracer(0)** allows for manual refreshing, which is essential for smooth animations. Following this, the main game object, the snake's head, is created, as well as additional elements like the snake's food (represented by the dot object) and the snake's body (the corpus list).

The core part of the game is the while _True_ main loop, which handles the game state updates. Within this loop, the snake's movements, responses to key presses, eating of food, adding new segments to the snake, and handling collisions with the screen edges and its own body are managed. Each iteration of the loop ends with a brief delay (**time.sleep(delay)**), ensuring that the game runs at an appropriate speed.

## How run the game

### Downloading the repository

1. Install Git on your computer (if you haven't already).
2. Open the terminal (Git Bash for Windows, standard terminal for macOS/Linux).
3. Type in the terminal: `git clone https://github.com/WiolaWysopal/Snake.git`.

### Running the game

1. Launch your IDE (e.g., PyCharm, Visual Studio Code).
2. Open or import the downloaded game repository.
3. Ensure you have Python installed and configured in the IDE.
4. Find the main game file (e.g., `main.py`) in the project.