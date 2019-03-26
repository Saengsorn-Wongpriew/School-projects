import time
import tkinter
import math
animacio = tkinter.Tk()
canvas = tkinter.Canvas(animacio, bg="lightblue", height=500, width=500)
canvas.pack()

vege=time.time()+30
fok=270
def mutato(szog_fokban):
    szog_radian = szog_fokban * math.pi / 180
    vonal_hossz = 100
    center_x = 250
    center_y = 250
    end_x = center_x + vonal_hossz * math.cos(szog_radian)
    end_y = center_y + vonal_hossz * math.sin(szog_radian)
    return end_x,end_y

while time.time() < vege:
    canvas.delete("all")
    canvas.create_oval(100,100,400,400,fill="lightgreen")
    canvas.create_line((250,250),mutato(fok),width=2,fill="black")
    fok=fok+30
    time.sleep(1)
    animacio.update()
