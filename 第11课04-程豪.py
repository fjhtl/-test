#导入库
import turtle as t
t1=t.Pen()
t2=t.Pen()
t.tracer(0)
#t1.hideturtle()
#t2.hideturtle()
t1.pensize(15)
t2.pensize(15)
#数据
a=[8,12,14]
#模块化设计
def move1(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
def move2(x,y):
    t2.penup()
    t2.goto(x,y)
    t2.pendown()
def home():
    t1.penup()
    t1.home()
#主程序
move1(-250,0)
t1.pencolor('red')
t1.fd(500)
for i in range(3):
    x=-150+150*i
    y=0
    move1(x,y)
    t1.left(90)
    t1.fd(250)
    t1.right(90)   

