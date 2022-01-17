import turtle

turtle.Screen().bgcolor("blue")
screen = turtle.Screen()

#screen.screensize(10000, 10000)
screen.setup(width = 1.0, height = 1.0 , startx=None, starty=None)

  #remove close,minimaze,maximaze buttons:
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
skk = turtle.Turtle()
 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('blue')
########################################
#pen = turtle.Turtle()

#while 1:
  #  pen.write("Python is cool", font=("Calibri", 8, "bold"))
##################################################################
    
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)