import turtle as t    #化简turtle
t.speed(0)
#----移动函数-----方便移动画笔
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#-----画脸------
t.setheading(90)
t.color('black','yellow')
t.begin_fill()
t.circle(200,360)
t.circle(-200,360)
t.end_fill()
#-----画眼睛------
move(-250,100)
t.color('black','white')
t.begin_fill()
t.circle(50,360)
move(-50,100)
t.circle(50,360)
move(250,100)
t.circle(-50,360)
move(50,100)
t.circle(-50,360)
t.end_fill()


move(-300,50)
t.color('black','black')
t.setheading(0)
t.begin_fill()
t.circle(25,360)
move(-100,50)
t.circle(25,360)
move(100,50)
t.circle(25,360)
move(300,50)
t.circle(25,360)
t.end_fill()

#-----画嘴巴------
move(200,-150)
t.circle(200,-45)
t.setheading(0)
move(200,-150)
t.circle(200,45)

t.setheading(0)
move(-200,-50)
t.circle(-200,-45)
t.setheading(0)
move(-200,-50)
t.circle(-200,45)

