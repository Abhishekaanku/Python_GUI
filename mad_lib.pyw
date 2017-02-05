from tkinter import *
class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.set_widget()
        self.master=master
    def set_widget(self):
        Label(self,text="Enter information for a new story."
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="Person:"
              ).grid(row=1,column=0,sticky=W)
        self.ent1=Entry(self)
        self.ent1.grid(row=1,column=1,columnspan=2,sticky=W)
        Label(self,text="Plural Noun:"
              ).grid(row=2,column=0,sticky=W)
        self.ent2=Entry(self)
        self.ent2.grid(row=2,column=1,columnspan=2,sticky=W)
        Label(self,text="Verb:"
              ).grid(row=3,column=0,sticky=W)
        self.ent3=Entry(self)
        self.ent3.grid(row=3,column=1,columnspan=2,sticky=W)
        Label(self,text="Adjective(s):"
              ).grid(row=4,column=0,sticky=W)
        self.is_adjective1=BooleanVar()
        Checkbutton(self,text="itchy",
                    variable=self.is_adjective1
                    ).grid(row=4,column=1,sticky=W)
        self.is_adjective2=BooleanVar()
        Checkbutton(self,text="joyous",
                    variable=self.is_adjective2
                    ).grid(row=4,column=2,sticky=W)
        self.is_adjective3=BooleanVar()
        Checkbutton(self,text="electric",
                    variable=self.is_adjective3
                    ).grid(row=4,column=3,sticky=W)
        Label(self,text="Body Part"
              ).grid(row=5,column=0,sticky=W)
        self.body_part=StringVar()
        self.body_part.set(None)
        Radiobutton(self,text="bellybutton",
                    variable=self.body_part,
                    value="bellybutton"
                    ).grid(row=5,column=1,sticky=W)
        Radiobutton(self,text="big toe",
                    variable=self.body_part,
                    value="big toe"
                    ).grid(row=5,column=2,sticky=W)
        Radiobutton(self,text="medulla oblongata",
                    variable=self.body_part,
                    value="medulla oblongata"
                    ).grid(row=5,column=3,sticky=W)
        Button(self,text="Click for story",command=self.display
               ).grid(row=6,column=0,sticky=W)
        self.txt=Text(self,width=68,height=14,wrap=WORD)
        self.txt.grid(row=7,column=0,rowspan=4,columnspan=6,sticky=W)
        Button(self,text="  Quit  ",command=self.close
               ).grid(row=11,column=0,sticky=W)
    def display(self):
        message="The famous explorer "
        name=self.ent1.get()
        message+=name+" had nearly given up a life-long quest to find the lost city of "
        city=self.ent2.get()
        verb=self.ent3.get()
        message+=city+" when one day,"+name+" found "+city+" "+verb+"ing. A strong,"
        if self.is_adjective1.get():
            message+=" itchy,"
        if self.is_adjective2.get():
            message+=" joyous,"
        if self.is_adjective3.get():
            message+=" electric,"
        part=self.body_part.get()
        message+=" peculiar feeling overwhelmed the explorer.After all this time ,the quest was finally over. A tear came to "
        message+=name+"'s "+part+". And then,"
        message+=city+" devoured "+name+ "."
        message+="The moral of story?\nBe careful what you dance for."
        self.txt.delete(0.0,END)
        self.txt.insert(0.0,message)
    def close(self):
        self.master.destroy()
root=Tk()
root.title("Mad Lib")
root.geometry("540x415")
app=App(root)
root.mainloop()
        
        
























        


























                      
        
