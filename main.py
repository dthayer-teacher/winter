import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)



t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor("snow1")
t_ground.fillcolor('snow1')
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.fillcolor('springgreen')
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.fillcolor('brown4')
# t.pencolor('brown4')
# t.penup()
#
# t.goto(-150,0)
#
# t.pendown()
# t.begin_fill()
# t.forward(250)
# t.right(90)
# t.forward(150)
# t.right(90)
# t.forward(250)
# t.right(90)
# t.forward(150)
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.penup()
# t.goto(-150,0)
# t.pendown()
# t.goto(-25,100)
# t.goto(100,00)
# t.goto(-150,0)
#
# t.fillcolor('gold')
# t.pencolor('gold')
# t.penup()
# t.goto(-135,85)
# t.pendown()
# t.begin_fill()
# t.goto(-125,110)
# t.goto(-115,85)
# t.goto(-140,100)
# t.goto(-110,100)
#
# t.goto(-135,85)
# t.end_fill()
#
# t.end_fill()
# t.penup()
# t.pencolor('blue')
# t.goto(-150,-150)
# t.setheading(0)
# t.pendown()
# t.pensize(10)
# x = -150
# for i in range(15):
#
#     # t.penup()
#     #
#     # t.goto(-150,-150+i*10)
#     # t.pencolor('black')
#     # t.pendown()
#     # t.forward(250)
#     t.pencolor('blue')
#     t.penup()
#     if i %2 ==0:
#         t.penup()
#
#         t.goto(x, -150 + i * 10)
#         t.pencolor('tan3')
#         t.pendown()
#         t.forward(250)
#         t.penup()
#         t.pencolor('tan4')
#         t.goto(x, -150 + i * 10+2)
#         t.pendown()
#         t.forward(250)
#
#     else:
#         t.penup()
#
#         t.goto(x + 5, -150 + i * 10)
#         t.pencolor('tan3')
#         t.pendown()
#         t.forward(240)
#         t.penup()
#         t.pencolor('saddlebrown')
#         t.goto(x+5, -150 + i * 10 + 2)
#         t.pendown()
#         t.forward(240)
#
#
#     t.pendown()
#
#
t.penup()
t.pensize(10)
t.goto(200,50)
t.pendown()
t.pencolor('red')
t.goto(200,150)
t.setheading(90)
t.circle(25,180)
for i in range(9):
    t.penup()
    if i%2 ==0:
        t.pencolor('red')
    else:
        t.pencolor('white')

    t.pensize(10)
    t.goto(200,50+i*10)
    t.pendown()
    t.goto(200,60+(i+1)*10)

scale = .5
s = turtle.Turtle()
s.speed(0)
s.pensize(8)
s.penup()
s.goto(-200,-200)
s.pendown()
s.goto(-100,-200)
s.goto(-100,-150)
s.goto(0,-150)
s.goto(-60,-100)
s.goto(-100,-150)
s.goto(-40,-220)
s.goto(-40,-300)
s.penup()
s.goto(0,-150)
s.pendown()
s.goto(0,-220)
s.penup()
s.goto(0,-150)
s.setheading(270)
s.pendown()
s.circle(25)

s.penup()
s.goto(-125,-125)
s.pendown()
s.goto(75,-300)
s.goto(125,-300)
#
#
#

import random



move_up_down = -150
move_mantle = move_up_down + 35
move_left_right = -200

t = turtle.Turtle()
colors = ['firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', ]
t.speed(0)
bump = 0
adjust_x = -100
adjust_y = 100
x = -100
y = move_up_down
size_x = 40
brick_x = 8
brick_y = 2.25
scale = size_x / brick_x
size_y = scale * brick_y
t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_mantle - 2 * size_y + adjust_y)
t.end_fill()
x_beg = -20
y_beg = 0
for x in range(15):
    x_beg = x * 20 - 8
    t.penup()
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.pendown()
    col = random.choice(colors)
    t.fillcolor(col)
    t.begin_fill()
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x + 20, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + size_y + adjust_y)
    t.goto(move_left_right + x_beg + adjust_x, move_up_down - y_beg + adjust_y)
    t.end_fill()

for j in range(12):
    move_y = j * size_y
    if j % 2 == 0:
        bump = 0
    else:
        x = 0
        bump = size_x / 2
        t.penup()
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.pendown()
        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        t.goto(move_left_right + x + bump + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + x + bump + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()
    for i in range(7):
        x = i * size_x
        if x + bump + size_x > 280:
            size_x = size_x / 2
        else:
            size_x = 40

        start_x = x + bump
        end_x = x + bump + size_x

        t.penup()
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.pendown()

        col = random.choice(colors)
        t.fillcolor(col)
        t.begin_fill()
        if j >= 3 and j <= 9:
            if end_x > 100 and start_x < 180:
                end_x = 80

                start_x = 200
                t.penup()
                size_x = 40

        t.goto(move_left_right + end_x + adjust_x, y - move_y + adjust_y)
        t.goto(move_left_right + end_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y - size_y + adjust_y)
        t.goto(move_left_right + start_x + adjust_x, y - move_y + adjust_y)
        t.penup()
        t.end_fill()

t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.fillcolor('black')
t.begin_fill()
t.goto(move_left_right + 205 + adjust_x, move_up_down - 35 + adjust_y)
t.goto(move_left_right + 205 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 115 + adjust_y)
t.goto(move_left_right + 80 + adjust_x, move_up_down - 35 + adjust_y)
t.end_fill()

t.fillcolor('tan')
t.penup()
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.pendown()
t.begin_fill()
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 + adjust_y)
t.goto(move_left_right + 296 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 - 2 * size_y + adjust_y)
t.goto(move_left_right + -16 + adjust_x, move_up_down - 135 + adjust_y)
t.end_fill()

turtle.done()




#this is the last line of code
turtle.done()