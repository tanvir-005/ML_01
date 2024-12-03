import turtle

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle cursor
t.hideturtle()

# Lift the pen up
t.penup()

# Move to starting position
t.goto(-50, 0)

# Put the pen down
t.pendown()

# Write the text
t.write("Tanvir", font=("Arial", 24, "normal"))

# Keep the window open
turtle.done()
