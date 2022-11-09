# solution to coding challenge 1.1

import turtle

window = turtle.Screen()
t = turtle.Turtle()

# move into position for the R
t.penup()
t.right(90)
t.forward(150) # down
t.right(90)
t.forward(200) # left

# draw the R
t.pendown()
t.right(90) # up
t.forward(300)
t.right(90) # right
t.forward(150)
t.right(90) # down
t.forward(150)
t.right(90) # left
t.forward(150)
t.left(135) # diagonal down/right
t.forward(212)

# move into position for the F
t.penup()
t.left(45)
t.forward(100)

# draw the F
t.pendown()
t.left(90)
t.forward(300)
t.right(90)
t.forward(150)
t.left(180)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)

t.penup()

window.mainloop()
