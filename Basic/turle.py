import turtle
import math
# 定义多个点坐标
x1, y1 = 100, 100
x2, y2 = -100, 100
x3, y3 = -100, -100
x4, y4 = 100, -100

# 绘制折线
turtle.penup()
turtle.goto(x1, y1)

turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)
turtle.goto(x1, y1)

#计算起始点和终点的距离
# 它用的是勾股定理，√(x² + y²)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
turtle.write(distance)
turtle.done()