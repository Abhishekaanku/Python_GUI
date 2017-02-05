from tkinter import *
class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.set_widget()
    def set_widget(self):
        Label(self,text="Welcome to HALLEKHALLE calculator."
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="Enter First number"
              ).grid(row=1,column=0,sticky=W)
        self.ent1=Entry(self)
        self.ent1.grid(row=1,column=1,sticky=W)
        Label(self,text="Enter second number"
              ).grid(row=2,column=0,sticky=W)
        self.ent2=Text(self,width=15,height=1,wrap=CHAR)
        self.ent2.grid(row=2,column=1,sticky=W)
        self.operation=StringVar()
        self.operation.set(None)
        Radiobutton(self,text="Add",
                    variable=self.operation,
                    value="add",
                    command=self.display
                    ).grid(row=3,column=0,sticky=W)
        Radiobutton(self,text="Subtract",
                    variable=self.operation,
                    value="sub",
                    command=self.display
                    ).grid(row=3,column=1,sticky=W)
        Radiobutton(self,text="Divide\t\t\t",
                    variable=self.operation,
                    value="div",
                    command=self.display
                    ).grid(row=3,column=2,sticky=W)
        Radiobutton(self,text="Multiply",
                    variable=self.operation,
                    value="mul",
                    command=self.display
                    ).grid(row=3,column=3,sticky=W)
        Label(self,text="Result"
              ).grid(row=4,column=0,sticky=E)
        self.ent3=Entry(self)
        self.ent3.grid(row=4,column=1,columnspan=2,sticky=W)
    def display(self):
        self.msg=self.operation.get()
        num1=float(self.ent1.get())
        num2=float(self.ent2.get(0.0,END))
        try:
            if self.msg=="add":
                self.result=str(num1+num2)
            elif self.msg=="sub":
                self.result=str(num1-num2)
            elif self.msg=="div":
                self.result=str(num1/num2)
            elif self.msg=="mul":
                self.result=str(num1*num2)
        except ZeroDivisionError:
            self.result="can't divide by zero"
        self.ent3.delete(0,END)
        self.ent3.insert(0,self.result)
root=Tk()
root.title("Calculator")
root.geometry("480x300")
app=App(root)
root.mainloop()
        
        
        
        
        





































        
        

        
