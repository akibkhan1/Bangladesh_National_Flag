import turtle

obj=turtle.Turtle()


obj.speed(3)

obj.penup()

obj.goto(-100,200)

obj.pendown()

obj.begin_fill()
obj.fillcolor("green")
obj.color('green')
obj.forward(300)

obj.setheading(270)

obj.forward(180)

obj.setheading(180)

obj.forward(300)

obj.setheading(90)

obj.forward(180)

obj.end_fill()

obj.penup()

obj.goto(0,110)

obj.pendown()


obj.begin_fill()
obj.fillcolor("red")
obj.color('red')
obj.circle(-50)
obj.end_fill()

obj.color('black')

obj.setheading(180)
obj.penup()
obj.forward(100)
obj.pendown()

obj.begin_fill()
obj.fillcolor('gray')



obj.setheading(90)
obj.forward(130)


obj.setheading(180)
obj.forward(15)
obj.setheading(270)
obj.forward(450)

obj.setheading(180)
obj.forward(60)

obj.setheading(270)
obj.forward(15)
obj.setheading(360)
obj.forward(140)

obj.setheading(90)
obj.forward(15)

obj.setheading(180)
obj.forward(65)
obj.setheading(90)
obj.forward(450)
obj.end_fill()

obj.hideturtle()

turtle.done()