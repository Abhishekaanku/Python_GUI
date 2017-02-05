from tkinter import *
class App1(Frame):
    def __init__(self,master):
        super(App1,self).__init__(master)
        self.grid(row=0,column=0,rowspan=5,sticky=W)
        self.set_widget()
        self.master=master
    def set_widget(self):
        Label(self,text="HEALTHCARE APP"
              ).grid(row=0,column=1,sticky=W)
        Label(self,text="We care about your health."
              ).grid(row=1,column=1,columnspan=2,sticky=W)
        self.fvrt=StringVar()
        self.fvrt.set(None)
        Radiobutton(self,text="Heartbeat\t\t\t",
                    variable=self.fvrt,
                    value="heartbeat",
                    command=self.run,
                    ).grid(row=2,column=0,sticky=E)
        Radiobutton(self,text="Temperature\t\t\t",
                    variable=self.fvrt,
                    value="temperature",
                    command=self.run,
                    ).grid(row=2,column=1,sticky=E)
        Radiobutton(self,text="Breathing",
                    variable=self.fvrt,
                    value="breathing",
                    command=self.run,
                    ).grid(row=2,column=2,sticky=W)
    def run(self):
        app2=App2(self.master)
class App2(Frame):
    def __init__(self,master):
        super(App2,self).__init__(master)
        self.grid(row=5,column=0,rowspan=5,sticky=W)
        self.set_widget()
        root.geometry("455x350")
    def set_widget(self):
        if app1.fvrt.get()=="heartbeat":
            root.title("Health Care (Heartbeat mode)")
            Label(self,text="Place your thumb near your wrist and count number of pulse in a small interval.\t\t"
              ).grid(row=0,column=0,columnspan=7,sticky=W)
            Label(self,text=" Number of beat(s)    "
                  ).grid(row=1,column=0,sticky=W)
            self.ent1=Entry(self)
            self.ent1.grid(row=1,column=1,sticky=W)
            Label(self,text="Period (in second)"
                  ).grid(row=2,column=0,sticky=W)
            self.ent2=Entry(self)
            self.ent2.grid(row=2,column=1,sticky=W)
            Button(self,text=" Submit ",command=self.display_h_tip
                   ).grid(row=3,column=0,sticky=W)
        elif app1.fvrt.get()=="temperature":
            root.title("Health Care (Temperature mode)")
            Label(self,text="Insert a thermometer under your tongue and remove after a couple of minute.\t\t"
              ).grid(row=0,column=0,columnspan=7,sticky=W)
            Label(self,text="Thermometer reading"
                  ).grid(row=1,column=0,sticky=W)
            self.ent1=Entry(self)
            self.ent1.grid(row=1,column=1,sticky=W)
            self.temp=StringVar()
            self.temp.set(None)
            Radiobutton(self,text="Celsius",
                        value="celsius",
                        variable=self.temp
                        ).grid(row=2,column=0,sticky=E)
            Radiobutton(self,text="Fahrenheit",
                        value="fahrenheit",
                        variable=self.temp
                        ).grid(row=2,column=1,sticky=E)
            Button(self,text=" Submit ",command=self.display_temp_tip
                   ).grid(row=3,column=0,sticky=W)
        elif app1.fvrt.get()=="breathing":
            root.title("Health Care (Breathing mode)")
            Label(self,text="Count number of complete breath (one exhale and one inhale) in a small interval."
                  ).grid(row=0,column=0,columnspan=7,sticky=W)
            Label(self,text=" Number of breaths   "
                  ).grid(row=1,column=0,sticky=W)
            self.ent1=Entry(self)
            self.ent1.grid(row=1,column=1,sticky=W)
            Label(self,text="Period (in second)"
                  ).grid(row=2,column=0,sticky=W)
            self.ent2=Entry(self)
            self.ent2.grid(row=2,column=1,sticky=W)
            Button(self,text=" Submit ",command=self.display_breath_tip
                   ).grid(row=3,column=0,sticky=W)
        self.txt=Text(self,width=40,height=11,wrap=WORD)
        self.txt.grid(row=4,column=0,rowspan=3,columnspan=9,sticky=W)
    def display_h_tip(self):
        beat=float(self.ent1.get())
        period=float(self.ent2.get())
        pulse_rate=(beat/period)*60
        if pulse_rate<70:
            message="Oops!Your pulse rate is "+str(int(pulse_rate))+" which is low.\nTake regular exercise."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        elif pulse_rate<74:
            message="Your pulse rate is "+str(int(pulse_rate))+" which is normal.\nCheers!!"
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        else:
            message="Oops!Your pulse rate is "+str(int(pulse_rate))+" which is high.\nUse low cholestrol diet."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
    def display_temp_tip(self):
        temp=float(self.ent1.get())
        if self.temp.get()=="celsius":
            temp=32+9*temp/5
        if temp<94:
            message="Invalid temperature!!\nMeasure again."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
            print("\a\a")
        elif temp<=98.8:
            message="Your temperature is normal.\nCheers!!"
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        elif temp<=99.3:
            message="You have slight fever.\nTake rest."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        elif temp>99.3:
            message="Oops!!You have a fever.\nTake Paracetamol."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
    def display_breath_tip(self):
        breath=float(self.ent1.get())
        period=float(self.ent2.get())
        breath_rate=(breath/period)*60
        if breath_rate<15:
            message="Oops!Your breath rate is "+str(int(breath_rate))+" which is low.\nTake regular exercise."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        elif breath_rate<=17:
            message="Your breath rate is "+str(int(breath_rate))+" which is normal.\nCheers!!"
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
        else:
            message="Oops!Your breath rate is "+str(int(breath_rate))+" which is high.\nTake energy rich diet."
            self.txt.delete(0.0,END)
            self.txt.insert(0.0,message)
root=Tk()
root.title("Health Care")
root.geometry("455x140")
app1=App1(root)
root.mainloop()
        
        
