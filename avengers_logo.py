# on VS code you have to compile or run by (without debugging or by shortcut "ctrl + f5"). 

# importing header files 
import turtle
# display style
turtle.Screen().bgcolor("white")
t = turtle.Turtle()
t.speed(10)
t.pensize(20)
t.penup()

# making 1st circle
def draw_circle():
    t.setposition(0,-280)
    t.pendown()
    t.begin_fill()
    t.color('black')
    t.pencolor("black")
    t.circle(300)
    t.end_fill()
    t.penup()

 # making 2nd circle
def draw_circle2():
    t.pensize(2)
    t.setposition(0,-230)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.circle(250)            
    t.end_fill()
    t.penup()

# writing A
def draw_A():
    t.setposition(30,-110)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.pensize(10)
    t.pencolor("black")
    t.forward(23)
    t.backward(123)
    t.left(60)
    t.backward(220)
    t.right(60)
    t.backward(100)
    t.right(117)
    t.backward(710)
    t.right(63)
    t.backward(110)
    t.right(90)
    t.backward(510)
    t.right(90)
    t.backward(100)
    t.right(90)
    t.backward(70)
    t.end_fill()
    t.penup()

# making triangle
def draw_triangle():
    t.pensize(10)
    t.setposition(53,-40)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.pencolor("black")
    t.right(90)
    t.forward(100)
    t.right(115)
    t.forward(250)
    t.right(157)
    t.forward(227)
    t.end_fill()

# making arrow
def draw_arraow():
    t.backward(80)
    t.left(42)
    t.forward(147)
    t.right(83)
    t.forward(140)

# recalling the tags
draw_circle()
draw_circle2()
draw_A()
draw_triangle()
draw_arraow()
turtle.done
