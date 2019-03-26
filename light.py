import time
import tkinter

animacio = tkinter.Tk()
canvas = tkinter.Canvas(animacio, bg="black", height=500, width=500)
canvas.pack()
vege = time.time() + 14

while time.time() < vege:
    canvas.delete("all")
    canvas.create_text(250,110,text="fényreklám",font="Arial 50 bold",fill='green')
    animacio.update()
    time.sleep(0.15)
    canvas.delete("all")
    canvas.create_text(250,110,text="fényreklám",font="Arial 50 bold",fill='red')
    animacio.update()
    time.sleep(0.15)
