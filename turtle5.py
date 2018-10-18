from turtle import*
def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    left(36)
    for i in range(5):
        forward(length)
        left(144)
    mainloop()
draw_star(0,0,150)