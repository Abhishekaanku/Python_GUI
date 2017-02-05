from tkinter import *
class App1(Frame):
    def __init__(self,master):
        super(App1,self).__init__(master)
        self.grid()
        self.set_widget()
        self.master=master
        self.filename=None
        self.file1=None
        self.file2=None
        self.new=False
        self.open=False
        self.quit_=False
        self._open=True
        self.save_=True
        self.dialog=True
    def set_widget(self):
        Label(self,text="Welcome to my very simplified version of text editor"
              ).grid(row=0,column=2,columnspan=2,sticky=E)
        Button(self,text="Open an existing file",command=self.open_
               ).grid(row=1,column=2,sticky=E)
        Button(self,text="   Open a new file   ",command=self.open_new
               ).grid(row=1,column=3,sticky=W)
        self.txt=Text(self,width=100,
                      height=30,
                      wrap=WORD
                      )
        self.txt.grid(row=3,column=0,columnspan=9,rowspan=5)
        Button(self,text="   Save   ",command=self.save
               ).grid(row=8,column=0,sticky=W)
        Button(self,text=" Save As ",command=self.save_as
               ).grid(row=8,column=0,sticky=E)
        Button(self,text="   Quit   ",command=self.quit
               ).grid(row=8,column=8,sticky=E)
    def open_(self):
        if self._open:
            self.file2=self.txt.get(0.0,END)
            if self.file1!=self.file2 and len(self.file2)>1:
                self.open=True
                self.open_dialog()
            else:
                root3=Tk()
                root3.title("Open")
                root3.geometry("280x130")
                app3=App3(root3)
                root3.mainloop()
    def save_as(self):
        if self.save_:
            root2=Tk()
            root2.title("Save")
            root2.geometry("280x130")
            app2=App2(root2)
            root2.mainloop()
    def save(self):
        try:
            if self.file_name:
                text_file=open(self.file_name,"w")
                file=self.txt.get(0.0,END)
                text_file.write(file)
                text_file.close()
            else:
                self.save_as()
            self.file1=self.txt.get(0.0,END)
        except AttributeError:
            self.save_as()
    def open_new(self):
        if self.dialog:
            self.file2=self.txt.get(0.0,END)
            if self.file1!=self.file2 and len(self.file2)>1:
                self.new=True
                self.open_dialog()
            self.txt.delete(0.0,END)
            self.master.title("Text Editor")
            self.file_name=None
    def quit(self):
        self.quit_=True
        self.file2=self.txt.get(0.0,END)
        if self.file1!=self.file2 and len(self.file2)>1:
            self.open=False
            self.new=False
            self.open_dialog()
        self.master.destroy()
    def open_dialog(self):
        if self.dialog:
            root4=Tk()
            root4.title(" ? ")
            root4.geometry("320x100")
            app4=App4(root4)
            root4.mainloop()
    def select(self):
        if self.new:
            self.open_new()
            self.new=False
            self.open=False
        elif self.open:
            self.open_()
            self.open=False
            self.new=False
        else:
            self.quit()
class App2(Frame):
    def __init__(self,master):
        app1.save_=False
        super(App2,self).__init__(master)
        self.grid()
        self.set_widget()
        self.master=master
    def set_widget(self):
        Label(self,text="Enter the name of the file"
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        self.ent=Entry(self)
        self.ent.grid(row=0,column=3,sticky=W)
        Button(self,text="  Ok  ",command=self.save
               ).grid(row=1,column=0,sticky=W)
    def save(self):
        file_name=self.ent.get()+".txt"
        text_file=open(file_name,"w")
        file=app1.txt.get(0.0,END)
        app1.file1=file
        app1.file_name=file_name
        text_file.write(file)
        text_file.close()
        app1.save_=False
        self.master.destroy()
        if app1.quit_:
                app1.quit()
class App3(Frame):
    def __init__(self,master):
        app1._open=False
        super(App3,self).__init__(master)
        self.grid()
        self.set_widget()
        self.master=master
    def set_widget(self):
        Label(self,text="Enter the name of the file"
              ).grid(row=0,column=0,columnspan=2,sticky=W)
        self.ent=Entry(self)
        self.ent.grid(row=0,column=3,sticky=W)
        Button(self,text="  Ok  ",command=self.open_
               ).grid(row=1,column=0,sticky=W)
    def open_(self):
        try:
            self.file_name=self.ent.get()+".txt"
            text_file=open(self.file_name,"r")
            lines=text_file.read()
            text_file.close()
            app1.txt.delete(0.0,END)
            app1.txt.insert(0.0,lines)
            app1.file1=app1.txt.get(0.0,END)
            app1.master.title("Text Editor : "+self.file_name)
            app1.file_name=self.file_name
            app1._open=True
            self.master.destroy()
        except FileNotFoundError:
            Label(self,text="Given file name doesn't exist!"
                  ).grid(row=2,column=0,columnspan=2,sticky=E)
            self.ent.delete(0,END)
            print("\a\a\a")
class App4(Frame):
    def __init__(self,master):
        app1.dialog=False
        super(App4,self).__init__(master)
        self.grid()
        self.set_widget()
        self.master=master
    def set_widget(self):
        Label(self,text="\tDo you want to save the changes to the file?"
              ).grid(row=0,column=0,columnspan=3,sticky=W)
        print("\a\a\a")
        Button(self,text="   Yes   ",command=self.save
               ).grid(row=2,column=1,sticky=W)
        Button(self,text="   No   ",command=self.quit
               ).grid(row=2,column=1,sticky=E)
    def save(self):
        app1.dialog=True
        self.master.destroy()
        app1.save()
        app1.txt.delete(0.0,END)
        app1.select()
    def quit(self):
        app1.dialog=True
        self.master.destroy()
        app1.txt.delete(0.0,END)
        app1.select()
root=Tk()
root.title("Text Editor")
root.geometry("800x560")
app1=App1(root)
root.mainloop()

        
    
        
        
              





















        
    
        
        
        

        
        
    

