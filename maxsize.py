import tkinter
import sys

top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="lightblue", height=500, width=500)
canvas.pack()
eddig=5
max=0
min=sys.maxsize
y=30
for i in range(eddig):
   
    beker=int(input('irjon be egy szamot:  '));
    if beker<min:
        min=beker
    elif beker>max:
        max=beker
    if min>max:
        max=min
    canvas.create_text(110, y, text="min= "+ str(min) +" max= "+ str(max) ,font="Arial 20 bold")
    y=y+30
