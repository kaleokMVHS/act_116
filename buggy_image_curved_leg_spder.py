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
painter.speed(0)
leg = 0
while (leg < leg_num):
  painter.goto(0,20)
  painter.pd()
  if ( leg < 4):
    painter.setheading(leg_angle * leg + 90)
    dir = 1
  else:
    painter.setheading(leg_angle * leg + 110)
    dir = -1
  painter.circle(leg_length, 180 * dir)
  leg = leg + 1
  painter.pu()

# draw head

painter.goto(4, -20)
painter.pd()
painter.color('black')
painter.pensize(30)
painter.circle(4)
painter.pu()

#draw eyes
painter.pencolor('red')
painter.fillcolor('red')
painter.pensize(1)

painter.goto(-5, -20)
painter.begin_fill()
painter.circle(5)
painter.end_fill()


painter.goto(15, -20)
painter.begin_fill()
painter.circle(5)
painter.end_fill()

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
