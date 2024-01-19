# pseudocode
# Step 1: Create a snake
# Step 2: Make the snake move forward
# Step 3: Make the snake controlled by arrow keys
# Step 4: collision detection with food
# Step 5: Scoreboard
# step 6: collision detection with wall
# step 7: collision with tail

from turtle import Turtle,Screen

screen = Screen()
screen.setup(600,600) #screen size
screen.title("Snake Game")
screen.bgcolor("Black")

segments = []
starting_positions = [(0,0),(-20,0),(-40,0)]
for segment in range(0,3):
    snake = Turtle("square")
    snake.color("White")
    snake.penup()
    snake.goto(starting_positions[segment])
    segments.append(segment)

screen.exitonclick()