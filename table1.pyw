import random
from tkinter import *
class App1(Frame):
    def __init__(self,master):
        super(App1,self).__init__(master)
        self.grid(row=0,column=0,sticky=W)
        self.master=master
        self.set_widget()
    def set_widget(self):
        Label(self,text="DHANPAT'S TABLE LEARNING APP.\nYour kids' best friend and teacher!"
              ).grid(row=0,column=2,rowspan=2,columnspan=2,sticky=W)
        Label(self,text="Select Your Age (in years):"
              ).grid(row=2,column=0,columnspan=2,sticky=W)
        self.age=StringVar()
        self.age.set(None)
        Radiobutton(self,
                    text=" 4-5 ",
                    variable=self.age,
                    value="4-5",
                    command=self.display,
                    ).grid(row=3,column=0,sticky=W)
        Radiobutton(self,
                    text=" 6-8 ",
                    variable=self.age,
                    value="6-8",
                    command=self.display,
                    ).grid(row=3,column=1,sticky=W)
        Radiobutton(self,
                    text=" 9-12 ",
                    variable=self.age,
                    value="9-12",
                    command=self.display,
                    ).grid(row=3,column=2,sticky=W)
    def display(self):
        self.app2=App2(self.master)
class App2(Frame):
    def __init__(self,master):
        super(App2,self).__init__(master)
        self.grid(row=1,column=0,sticky=W)
        self.master=master
        self.set_widget()
    def set_widget(self):
        Label(self,text="Let's Begin . . . ."
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="You would like to give test of following table - "
              ).grid(row=1,column=0,columnspan=4,sticky=W)
        if app1.age.get()=="4-5":
            self.num=2
        elif app1.age.get()=="6-8":
            self.num=8
        elif app1.age.get()=="9-12":
            self.num=14
        num_=self.num
        self.t1=BooleanVar()
        Checkbutton(self,
                    text=" "+str(num_)+" ",
                    variable=self.t1,
                    ).grid(row=2,column=0,sticky=W)
        self.t2=BooleanVar()
        num_+=1
        Checkbutton(self,
                    text=" "+str(num_)+"   ",
                    variable=self.t2,
                    ).grid(row=2,column=1,sticky=W)
        self.t3=BooleanVar()
        num_+=1
        Checkbutton(self,
                    text=" "+str(num_)+"   ",
                    variable=self.t3,
                    ).grid(row=2,column=2,sticky=W)
        self.t4=BooleanVar()
        num_+=1
        Checkbutton(self,
                    text=" "+str(num_)+"   ",
                    variable=self.t4,
                    ).grid(row=2,column=3,sticky=W)
        self.t5=BooleanVar()
        num_+=1
        Checkbutton(self,
                    text=" "+str(num_)+"     ",
                    variable=self.t5,
                    ).grid(row=2,column=4,sticky=W)
        self.t6=BooleanVar()
        num_+=1
        Checkbutton(self,
                    text=" "+str(num_)+"  ",
                    variable=self.t6,
                    ).grid(row=2,column=5,sticky=W)
        Button(self,
               text=" Submit ",
               command=self.display
               ).grid(row=3,column=0,sticky=W)
    def display(self):
        app1.app3=App3(self.master)
class App3(Frame):
    def __init__(self,master):
        super(App3,self).__init__(master)
        self.grid(row=2,column=0,sticky=W)
        self.master=master
        self.trial=0
        self.multiple=[]
        self.index=0
        self.set_widget()
    def set_widget(self):
        self.num__=app1.app2.num
        self._num=[]
        if app1.app2.t1.get():
            self._num.append(self.num__)
        if app1.app2.t2.get():
            self._num.append(self.num__+1)
        if app1.app2.t3.get():
            self._num.append(self.num__+2)
        if app1.app2.t4.get():
            self._num.append(self.num__+3)
        if app1.app2.t5.get():
            self._num.append(self.num__+4)
        if app1.app2.t6.get():
            self._num.append(self.num__+5)
        self.test()
    def test(self):
        Label(self,text="\t\t\t\t\t\t\t\t\t"
              ).grid(row=2,column=0,columnspan=6,sticky=W)
        if self.trial%4==0 and self.trial!=0:
            Label(self,text="Congrats !! You have learned the table of "+str(self.num_)+"."
                  ).grid(row=2,column=0,columnspan=4,sticky=W)
            if self.index<len(self._num):
                self.index+=1
            if self.index==len(self._num):
                Label(self,text="Bravo!! You have learned all the tables of the series you have selected."
                      ).grid(row=2,column=0,columnspan=5,sticky=W)
                Button(self,
                       text=" Quit ",
                       command=self.master.destroy
                       ).grid(row=1,column=3,sticky=W)
                app1.display()
            self.multiple=[]
        self.num_=self._num[self.index]
        Label(self,text="Lets practice the table of "+str(self.num_)+"."
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        self.num=random.randint(2,9)
        while self.num in self.multiple:
            self.num=random.randint(2,9)
        self.multiple.append(self.num)
        Label(self,text=str(self.num_)+" x "+str(self.num)+" = "
              ).grid(row=1,column=0,columnspan=2,sticky=E)
        self.ent1=Entry(self)
        self.ent1.grid(row=1,column=2,sticky=W)
        self.click=0
        Button(self,
               text="  Ok   ",
               command=self.check
               ).grid(row=1,column=3,sticky=W)
    def check(self):
        ans=self.num_*self.num
        res=int(self.ent1.get())
        if ans==res:
            self.trial+=1
            Label(self,text="Wow! Your response is correct . . . Go ahead\t"
                  ).grid(row=2,column=0,columnspan=4,sticky=W)
            Button(self,text=" Next ",command=self.erase
                   ).grid(row=1,column=3,sticky=W)
        else:
            self.click+=1
            if self.click==1:
                self.trial=0
                self.multiple=[]
                root1=Tk()
                root1.title("Remember Window")
                root1.geometry("290x227")
                app4=App4(root1)
                root1.mainloop()
    def erase(self):
        Label(self,text="\t\t\t\t\t\t"
              ).grid(row=2,column=0,columnspan=4,sticky=W)
        self.test()
class App4(Frame):
    def __init__(self,master):
        super(App4,self).__init__(master)
        self.grid(row=2,column=0,sticky=W)
        self.master=master
        self.set_widget()
    def set_widget(self):
        Label(self,text="Oops you got it wrong\nLets repeat together.."
              ).grid(row=1,column=0,sticky=E)
        self.txt=Text(self,width=35,height=10,wrap=WORD)
        self.txt.grid(row=2,column=0,columnspan=2,sticky=W)
        self.txt.delete(0.0,END)
        text=""
        for i in range(1,11,1):
            text+=str(app1.app3.num_)+" x "+str(i)+" = "+str(app1.app3.num_*i)+"\n"
        self.txt.insert(0.0,text)
        Button(self,text="I remembered it",command=self.close
               ).grid(row=4,column=0,sticky=W)
    def close(self):
        self.master.destroy()
        app1.app3.test()
root=Tk()
root.title("Learning Table")
root.geometry("500x350")
app1=App1(root)
root.mainloop()
            
                
            
        
                
                
         
        
        
        
    
        
        
            
        
        
        

            
        























        
        
                    
                    
        
