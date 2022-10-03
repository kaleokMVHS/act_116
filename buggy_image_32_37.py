#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.speed(0)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1


leg_spacing = 30
leg_length = 50


for leg in range(6):
  ladybug.speed(0)
  ladybug.pu()
  ladybug.goto(0, -30)
  if (leg > 2):
    ladybug.setheading((leg * leg_spacing) + 60)
  else:
    ladybug.setheading((leg*leg_spacing -30))
  ladybug.forward(40)
  ladybug.pd()
  ladybug.forward(20)
  ladybug.pu()

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
