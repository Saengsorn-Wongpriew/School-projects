import time
import tkinter
import sys

animacio = tkinter.Tk()
canvas = tkinter.Canvas(animacio, bg="lightblue", height=500, width=500)
canvas.pack()
x=200
y=200


def kocsi(x,y):
    canvas.create_rectangle(x-20,y,x+70,y+50,fill='yellow')
    canvas.create_rectangle(x-10,y+10,x+60,y+40,fill='blue')
    canvas.create_rectangle(x-50,y+50,x+100,y+100,fill='yellow')
    canvas.create_oval(x-30,y+90,x,y+120,fill='black')
    canvas.create_oval(x+50,y+90,x+80,y+120,fill='black')

vege = time.time() + 14
while time.time() < vege:
    if vege< time.time() + 10:
        canvas.delete("all")
        time.sleep(0.005)
        kocsi(x,y)
        x=x-1
        animacio.update()
    elif vege> time.time() + 10:
        canvas.delete("all")
        time.sleep(0.005)
        kocsi(x,y)
        x=x+1
        animacio.update()
