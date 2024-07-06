from turtle import*

#we went to paint a house
#step 1: draw a square 
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square
#drawing a door
speed(30)



forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("purple")
penup()
goto(0,0)
pendown()

left(210)
forward(170)
color("brown")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
penup()
goto(200,200)
pendown()
left(90)
forward(80)
color("brown")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick()



