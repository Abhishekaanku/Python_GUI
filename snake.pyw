from tkinter import *
import random
class Board():
    def __init__(self):
        self.board=[]
        self.define_board()
    def define_board(self):
        a=0
        jump=["S","L"]
        while a<10:
            start=a*10+1
            stop=start+10
            num1=random.randint(start,stop-1)
            num2=random.randint(1,100)
            num3=random.randint(10,30)
            for i in range(start,stop,1):
                self.board.append("\t ")
                self.board.append(str(i))
                if num1==i and i>6 and i!=100:
                    if num2%2==0:
                        if start>=31:
                            self.board.append(jump[0]+str(i-num3)+"  ")
                        else:
                            self.board.append(jump[1]+str(num3+i)+"  ")
                    else:
                        if start<71:
                            self.board.append(jump[1]+str(num3+i)+"  ")
                        else:
                            self.board.append(jump[0]+str(i-num3)+"  ")
            self.board.append("\n\n\n")
            a+=1
class Player():
    def __init__(self,name,color,is_play=False,position=0):
        self.name=name
        self.pos=0
        self.is_play=is_play
        self.color=color
        self.position=0
class App1(Frame):
    def __init__(self,master):
        super(App1,self).__init__(master)
        self.grid()
        self.turn=None
        self.die=0
        self.ins="Instructions:\n"
        self.is_six=0
        self.master=master
        self.set_widget()
    def set_widget(self):
        Label(self,text="I player's name").grid(row=0,column=0,sticky=W)
        self.ent1=Entry(self)
        self.ent1.grid(row=0,column=1,sticky=W)
        Label(self,text="II player's name").grid(row=1,column=0,sticky=W)
        self.ent2=Entry(self)
        self.ent2.grid(row=1,column=1,sticky=W)
        Label(self,text="Who want to throw first?"
              ).grid(row=2,column=0,columnspan=2,sticky=W)
        self.is_first=StringVar()
        self.is_first.set(None)
        Radiobutton(self,
                    text=" Player I ",
                    variable=self.is_first,
                    command=self.turn_,
                    value="playerI"
                    ).grid(row=3,column=0,sticky=W)
        Radiobutton(self,
                    text=" Player II ",
                    variable=self.is_first,
                    command=self.turn_,
                    value="playerII"
                    ).grid(row=3,column=1,sticky=E)
        Label(self,text="I Player's die"
              ).grid(row=4,column=0,sticky=W)
        self.ent3=Entry(self)
        self.ent3.grid(row=4,column=1,sticky=W)
        Label(self,text="II player's die"
              ).grid(row=5,column=0,sticky=W)
        self.ent4=Entry(self)
        self.ent4.grid(row=5,column=1,sticky=W)
        self.txt=Text(self,width=38,height=5,wrap=WORD)
        self.txt.grid(row=6,column=0,columnspan=6,sticky=W)
    def turn_(self):
        if self.is_first.get()=="playerI":
            self.turn=0
        else:
            self.turn=1
        self.start_game()
    def display(self):
        br=""
        for i in self.board.board:
            br+=i
        if self.turn==0:
            name=self.ent1.get()
            if self.ent3.get()!="6":
                self.ent3.delete(0,END)
        elif self.turn==1:
            name=self.ent2.get()
            if self.ent4.get()!="6":
                self.ent4.delete(0,END)
        Label(self,text=br,background="red").grid(row=8,column=0,rowspan=10,columnspan=10,sticky=W)
        self.txt.delete(0.0,END)
        txt=self.ins+name+"! Its your turn now. Click to throw a die"
        self.txt.insert(0.0,txt)
    def start_game(self):
        self.board=Board()
        self.player1=Player(self.ent1.get(),"$Y$")
        self.player2=Player(self.ent2.get(),"@G*")
        self.display()
        Button(self,text=" Throw a die ",command=self.generate
               ).grid(row=7,column=1,sticky=W)
    def game(self,player,ent,player_):
        if player.position>0:
            point=int(ent.get())
            if player.pos>0 and player.pos+point<=100 and point!=6:
                index_=self.board.board.index(player.color)
                if self.is_six>0:
                    self.board.board[index_]=str(player.pos-6*self.is_six)
                    self.is_six=0
                else:
                    self.board.board[index_]=str(player.pos)
            if player.pos+point<=100:
                player.pos+=point
                if point!=6:
                    try:
                        index=self.board.board.index(str(player.pos))
                        self.board.board[index]=player.color
                        check=self.board.board[index+1]
                        while "L" in check or "S" in check:
                            jump=int(check[1])*10+int(check[2])
                            if "L" in check:
                                self.board.board[index]=str(player.pos)
                                player.pos+=jump-player.pos
                            elif "S" in check:
                                self.board.board[index]=str(player.pos)
                                player.pos-=player.pos-jump
                            index=self.board.board.index(str(jump))
                            self.board.board[index]=player.color
                            check=self.board.board[index+1]
                    except ValueError:
                        index=self.board.board.index(player_.color)
                        self.board.board[index]=player.color
                        player_.pos=0
                        player_.position=0
                        player_.is_play=False
            self.display()
            if player.pos==100:
                msg=player.name+" won the game !! Wel Done.\nThank you for playing te game."
                self.txt.delete(0.0,END)
                self.txt.insert(0.0,msg)
                Button(self,text=".......Quit........",command=self.master.destroy
                       ).grid(row=7,column=1,sticky=W)
            if point==6 and player.pos+point<=100:
                self.is_six+=1
                if self.is_six>2:
                    player.pos-=self.is_six*6
                    self.is_six=0
        else:
            self.display()
    def generate(self):
        if self.turn==0:
            if self.player1.is_play:
                if self.player1.position==0 or self.player1.pos>90:
                    self.die=random.randint(1,5)
                else:
                    self.die=random.randint(1,6)
                self.player1.position+=1
            else:
                self.die=random.randint(1,6)
            self.ent3.delete(0,END)
            self.ent3.insert(0,str(self.die))
            if self.die in [6]:
                self.player1.is_play=True
            else:
                self.turn=1
            self.game(self.player1,self.ent3,self.player2)
        else:
            if self.player2.is_play:
                if self.player2.position==0 or self.player2.pos>90:
                    self.die=random.randint(1,5)
                else:
                    self.die=random.randint(1,6)
                self.player2.position+=1
            else:
                self.die=random.randint(1,6)
            self.ent4.delete(0,END)
            self.ent4.insert(0,str(self.die))
            if self.die in [6]:
                self.player2.is_play=True
            else:
                self.turn=0
            self.game(self.player2,self.ent4,self.player1)
root=Tk()
root.title("Snake and Ladder Game")
root.geometry("650x900")
app1=App1(root)
root.mainloop()

















