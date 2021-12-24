import turtle as t  # as就是取个别名，后续调用的t都是turtle
from turtle import *
import random as r
import time

SLEEPTIME = 2
LINESPACE = 66
WRITETIME = 2
words = (
    "中午做了一个梦",
    "梦里有一只袜子鼓鼓",
    "打开一看",
    "是一只蜷成一团、呼呼大睡的小猪",
    "大概偷了哆啦A梦的缩小枪然后躲了进去",
    "结果被圣诞老人放到了我的枕边",
    "这是收到过最棒的礼物",
    "“圣诞快乐，我的小香猪”",
)


def drawsnow():  # 定义画雪花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(4)  # 定义笔头大小
    for i in range(50):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度


def tree(d, s):  # 开始画树
    if d <= 0:
        return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight()  # 同时调用小彩灯的方法
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)


def drawlight():  # 定义画彩灯的方法
    if r.randint(0, 60) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
        color('tomato')  # 定义第一种颜色
        circle(6)  # 定义彩灯大小
    elif r.randint(0, 30) == 1:
        color('orange')  # 定义第二种颜色
        circle(3)  # 定义彩灯大小
    else:
        color('dark green')  # 其余的随机数情况下画空的树枝


def writeWords():
    t.pu()
    t.sety(250)
    t.setx(0)
   # print("LOGING turtle pos", t.xcor(), t.ycor())
    t.color("lemonchiffon")
    for s in words:
        t.pd()
        # print("LOGING turtle pos", t.xcor(), t.ycor())
        t.write(s, align="center", font=("Comic Sans MS", 22, "bold"))
        t.pu()
        t.sety(t.ycor()-LINESPACE)
        if t.ycor() < -300:
            t.clear()
            t.sety(300)
        time.sleep(WRITETIME)


n = 80.0
pensize(4)
hideturtle()
speed(10)  # 定义速度
delay(0)
title("圣诞快乐")
screensize(800, 600, bg="lemonchiffon")  # 定义背景颜色，可以自己换颜色
# screensize(bg="navy")  # 定义背景颜色，可以自己换颜色
left(90)
forward(3 * n)
color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
begin_fill()
left(126)

for i in range(5):  # 画五角星
    forward(n / 5)
    right(144)  # 五角星的角度
    forward(n / 5)
    left(72)  # 继续换角度
end_fill()
right(126)


backward(n * 4.8)

tree(14, n)
backward(n / 2)


t.color("dark red", "red")  # 定义字体颜色
t.write("Merry Christmas", align="center", font=(
    "Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小
screensize(bg="black")
drawsnow()  # 调用画雪花的方法

time.sleep(SLEEPTIME)
t.clear()
writeWords()


t.done()  # 完成,否则会直接关闭
