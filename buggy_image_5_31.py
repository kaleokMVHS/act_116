#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()

# draw body
painter.pensize(40)
painter.circle(20)

# configure leg vars
leg_num = 8
leg_length = 70
leg_angle = 180 / leg_num
painter.pensize(5)

# iterate to draw legs 
leg = 0
while (leg < leg_num):
  painter.goto(0,20)
  if ( leg < 4):
    painter.setheading(leg_angle*leg - 45)
  else:
    painter.setheading(leg_angle * leg + 45)
  painter.forward(leg_length)
  leg = leg + 1
painter.pu()

painter.pencolor('red')
painter.fillcolor('red')
painter.pensize(1)

painter.goto(-10, 10)
painter.begin_fill()
painter.circle(5)
painter.end_fill()


painter.goto(10, 10)
painter.begin_fill()
painter.circle(5)
painter.end_fill()

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
