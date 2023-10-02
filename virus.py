import turtle

# Set up the Turtle screen
wd = turtle.Screen()
wd.bgcolor("black")
wd.title("Virus")
wd.screensize(500, 400)

# Create a Turtle object
virus = turtle.Turtle()
virus.speed(0)
virus.hideturtle()
virus.pencolor("cyan")
n = 200

# Main loop
while n > 0:
    virus.forward(n * 2)
    virus.left(n)
    n = n - 1

# Close the Turtle graphics window on click
wd.exitonclick()
