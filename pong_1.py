from tkinter import *
import random
import time

#Labda tulajdonsagok, funkciok
class Ball:
    def __init__(self, canvas, color, size, paddle, paddle2):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 360, w/2)
        self.xspeed = random.randrange(-3,3)
        self.yspeed = random.randrange(-2,2)
#        self.xspeed = -1.3
#        self.yspeed = -2
        self.paddle = paddle
        self.paddle2 = paddle2
        while(self.yspeed==0):
            self.yspeed = random.randrange(-1,1)
        self.hit_topbottom = False
        

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.hit_topbottom = True
        if pos[3] >= h:
            self.hit_topbottom = True
        if pos[0] <= 0:
            self.xspeed = 2
        if pos[2] >= w:
            self.xspeed = -2
        if pos[1]>h/2-250 and self.hit_paddle(pos,paddle) == True:
            self.yspeed = -2
            self.xspeed = random.randrange(-2,2)
        if pos[1]<h/2+250 and self.hit_paddle2(pos,paddle2) == True:
                self.yspeed = 2
                self.xspeed = random.randrange(-2,2)

    def hit_paddle(self, pos, paddle):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def hit_paddle2(self, pos, paddle2):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[1] >= paddle2_pos[1] and pos[1] <= paddle2_pos[3]:
                return True
        return False

#Uto tulajdonsagok, funkciok
class Paddle:
    def __init__(self, canvas, color, height, player):
        self.canvas = canvas
        self.height = height
        self.id = canvas.create_rectangle(0,0, 100, 15, fill=color)
        self.canvas.move(self.id, (w/2)-50, height)
        self.xspeed = 0
        self.player=player
        if player==1:
            self.canvas.bind_all('<KeyPress-Left>', self.move_left)
            self.canvas.bind_all('<KeyPress-Right>', self.move_right)
            self.canvas.bind_all('<KeyPress-Down>', self.stop)
#            label = canvas.create_text(5, h/2-105, anchor=NW, text="0",fill="white", font=("Ani",50))
        elif player==2:
            self.canvas.bind_all('<KeyPress-a>', self.move_left)
            self.canvas.bind_all('<KeyPress-d>', self.move_right)
            self.canvas.bind_all('<KeyPress-s>', self.stop)
#            label = canvas.create_text(5, h/2, anchor=NW, text="0",fill="white",font=("Ani",50))

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= w:
            self.xspeed = 0

    def move_left(self, evt):
        self.xspeed = -2
    def move_right(self, evt):
        self.xspeed = 2
    def stop(self, evt):
        self.xspeed = 0


# Ablak letrehozasa
tk = Tk()
tk.title("PoNG")
w=480
h=640
canvas = Canvas(tk, width=w, height=h, bd=0, bg='black')
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'White',h-15,1)
paddle2= Paddle(canvas, 'White',0,2)
ball = Ball(canvas, 'white', 25, paddle, paddle2)
canvas.create_line(0,h/2+2,w,h/2+2,fill="white",width=4, dash=(2, 4))

# Animacio inditasa
while ball.hit_topbottom == False:
#canvas.create_line(0,h/2+2,w,h/2+2,fill="white",width=4, dash=(2, 4))
    ball.draw()
    paddle.draw()
    paddle2.draw()
#    canvas.itemconfig(label, text="Score: "+str(ball.score))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# Game Over
go_label = canvas.create_text(w/2,h/2,text="GAME OVER",font=("Cantarell Ultra-Bold",40), fill="White")
tk.update()
