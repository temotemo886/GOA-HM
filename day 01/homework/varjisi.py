from turtle import *

speed(4)
width(6)

#კედლები სახლის
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#სახურავი
penup()
goto(0, 200)
pendown()

left(150)
forward(200)
right(120)
forward(200)

#ფანჯარა 1 (მარცხენა)
penup()
goto(20, 140)
pendown()

left(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)


#ფანჯარა 2 (მარჯვენა)
penup()
goto(140, 140)
pendown()

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

#კარები
penup()
goto(72, 0)
pendown()

left(180)
forward(90)
right(90)
forward(55)
right(90)
forward(90)

exitonclick()