import math
import time
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title("模拟时钟")

# 创建画布
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# 绘制表盘
for i in range(60):
    if i % 5 == 0:
        length = 15
    else:
        length = 5
    angle = math.radians(i * 6 - 90)
    x1 = 250 + math.cos(angle) * 140
    y1 = 250 + math.sin(angle) * 140
    x2 = 250 + math.cos(angle) * (140-length)
    y2 = 250 + math.sin(angle) * (140-length)
    canvas.create_line(x1, y1, x2, y2, width=2)

# 计算圆心坐标
center_x = 250
center_y = 250
radius = 140 + 10  # 半径为表盘半径加上圆的半径

# 绘制圆
for i in range(360):
    angle = math.radians(i - 90)
    x = center_x + math.cos(angle) * radius
    y = center_y + math.sin(angle) * radius
    canvas.create_oval(x-1, y-1, x+1, y+1, fill="black")

# 绘制时针、分针、秒针
hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - 60, width=6, fill="black")
minute_hand = canvas.create_line(center_x, center_y, center_x, center_y - 90, width=4, fill="black")
second_hand = canvas.create_line(center_x, center_y, center_x, center_y - 110, width=2, fill="black")

# 更新时钟
def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # 计算角度
    hour_angle = math.radians((hour % 12 + minute / 60) * 30 - 90)
    minute_angle = math.radians((minute + second / 60) * 6 - 90)
    second_angle = math.radians(second * 6 - 90)

    # 旋转时针、分针、秒针
    canvas.coords(hour_hand, center_x, center_y, center_x + math.cos(hour_angle) * 60, center_y + math.sin(hour_angle) * 60)
    canvas.coords(minute_hand, center_x, center_y, center_x + math.cos(minute_angle) * 90, center_y + math.sin(minute_angle) * 90)
    canvas.coords(second_hand, center_x, center_y, center_x + math.cos(second_angle) * 110, center_y + math.sin(second_angle) * 110)

    # 循环调用
    window.after(1000, update_clock)

# 启动时钟
update_clock()

# 运行窗口
window.mainloop()
