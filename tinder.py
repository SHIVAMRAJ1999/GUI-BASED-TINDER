
from tkinter import *

class GUIhelper:
    def __init__(self,f,g):
        self._root=Tk()
        self._root.title("Tinder Login")
        self._root.minsize(150,450)
        self._root.configure(background="#FC4F67")
        
        label1=Label(self._root,text="Tinder",bg="#FC4F67",fg="#fff")
        label1.configure(font=("Verdana",20,"bold","italic"))
        label1.pack(pady=(30,20))
        
        self.label2=Label(self._root,text="Kindly Long In to process",bg="#FC4F67",fg="#fff")
        self.label2.configure(font=("Verdana",10,"bold","italic"))
        self.label2.pack(pady=(10,20))
        
        label3=Label(self._root,text="Email",bg="#FC4F67",fg="#fff")
        label3.configure(font=("Verdana",10,"bold"))
        label3.pack(pady=(10,5))
        self._emailInput=Entry(self._root)
        self._emailInput.pack(ipadx=40,ipady=8,pady=(2,20))
        
        label4=Label(self._root,text="Password",bg="#FC4F67",fg="#fff")
        label4.configure(font=("Verdana",10,"bold"))
        label4.pack(pady=(10,5))
        self._passwordInput=Entry(self._root)
        self._passwordInput.pack(ipadx=40,ipady=8,pady=(2,30))
        
        btn1=Button(self._root,text="Sign In",bg="#fff",fg="#FC4F67",command=lambda:f())
        btn1.configure(width=30,height=2)
        btn1.pack(pady=(1,10))
        
        label5=Label(self._root,text="Not a member:Sign Up now!",bg="#FC4F67",fg="#fff")
        label5.configure(font=("Verdana",10))
        label5.pack(pady=(1,5))
        
        btn2=Button(self._root,text="Sign Up",bg="#fff",fg="#FC4F67",command=lambda:g())
        btn2.pack(pady=(2,1))
        
        self._root.mainloop()
        
    def regWindow(self,f):
        self._root.destroy()
        self._root=Tk()
        self._root.title("Register for Tinder")
        
        self._root.minsize(300,550)
        self._root.configure(background="#fd5068")
        
        label1=Label(self._root, text="Tinder", bg="#fd5068",fg="#fff")
        label1.configure(font=("Constantia", 24, "bold","italic","underline"))
        label1.pack(pady=(10,10))
        
        self.label2=Label(self._root, text="Fill the form to register", bg="#fd5068",fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5,10))
        
        label3=Label(self._root, text="Name", bg="#fd5068",fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5,5))
        
        self._nameInput=Entry(self._root)
        self._nameInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label4=Label(self._root, text="Email", bg="#fd5068",fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5,5))
        
        self._emailInput=Entry(self._root)
        self._emailInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label8=Label(self._root, text="Password", bg="#fd5068",fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5,5))
        
        self._passwordInput=Entry(self._root)
        self._passwordInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label5=Label(self._root, text="Gender", bg="#fd5068",fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5,5))
        
        self._genderInput=Entry(self._root)
        self._genderInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label6=Label(self._root, text="Age", bg="#fd5068",fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5,5))
        
        self._ageInput=Entry(self._root)
        self._ageInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label7=Label(self._root, text="City", bg="#fd5068",fg="#fff")
        label7.configure(font=("Verdana", 12, "bold"))
        label7.pack(pady=(5,5))
        
        self._cityInput=Entry(self._root)
        self._cityInput.pack(ipadx=50,ipady=7,pady=(1,15))
        
        btn1=Button(self._root, text="Sign Up" ,fg="#fd5068",bg="#fff", command=lambda :f())
        btn1.configure(width=25,height=2, font=("verdana", 10, "bold"))
        btn1.pack()
        
        self._root.mainloop()
    def mainWindow(self,other,data,mode,num=0):
        self.clear()
        self._root.title('My Profile')
        self._root.minsize(400,500)
        self._root.configure(background="#fff")
                             
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile",command=lambda:other.loadProfile())
        filemenu.add_command(label="Edif Profile",command=lambda:other.editProfile())
        filemenu.add_command(label="View Users",command=lambda:other.viewProfile(num))
        filemenu.add_command(label="Logout",command=lambda:other.logout())

        
        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals",command=lambda:other.proposals(num))
        helpmenu.add_command(label="My Requests",command=lambda:other.requests(num))
        helpmenu.add_command(label="My Matches",command=lambda:other.matches(num))
        
        from PIL import Image,ImageTk
        
        imageUrl="img/" + data[0][-1]
        load = Image.open(imageUrl)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()
        
        name="Name : "+data[0][1]
        label1=Label(self._root,text=name,bg="#fff",fg="#000")
        label1.configure(font=("Verdana",10,"bold"))
        label1.pack(pady=(10,5))
        
        gender="Not intrested in : "+data[0][4]
        label2=Label(self._root,text=gender,bg="#fff",fg="#000")
        label2.configure(font=("Verdana",10,"bold"))
        label2.pack(pady=(10,5))
        
        age="Age : "+str(data[0][5])
        label3=Label(self._root,text=age,bg="#fff",fg="#000")
        label3.configure(font=("Verdana",10,"bold"))
        label3.pack(pady=(10,5))
        
        city="From : "+data[0][6]
        label4=Label(self._root,text=city,bg="#fff",fg="#000")
        label4.configure(font=("Verdana",10,"bold"))
        label4.pack(pady=(10,5))
        if mode==2:
            frame=Frame(self._root)
            frame.pack()
        
            btn1=Button(frame,text="Previous",bg="#fff",fg="#FC4F67",command=lambda:other.viewProfile(num-1))
            btn1.pack(side=LEFT)
            
            btn2=Button(frame,text="Propose",bg="#fff",fg="#FC4F67",command=lambda:other.propose(data[0][0]))
            btn2.pack(side=LEFT)
            
            btn3=Button(frame,text="Next",bg="#fff",fg="#FC4F67",command=lambda:other.viewProfile(num+1))
            btn3.pack(side=LEFT)
        if mode==3:
            frame=Frame(self._root)
            frame.pack()
            
            btn1=Button(frame,text="Previous",bg="#fff",fg="#FC4F67",command=lambda:other.proposals(num-1))
            btn1.pack(side=LEFT)
        
            btn2=Button(frame,text="Accept",bg="#fff",fg="#FC4F67",command=lambda:self.connectaller(data[0][0],num,other))
            btn2.pack(side=LEFT)
            
            btn3=Button(frame,text="Reject",bg="#fff",fg="#FC4F67",command=lambda:self.rejectcaller(data[0][0],num,other))
            btn3.pack(side=LEFT)
            
            btn4=Button(frame,text="Next",bg="#fff",fg="#FC4F67",command=lambda:other.proposals(num+1))
            btn4.pack(side=LEFT)
        if mode==4:
            frame=Frame(self._root)
            frame.pack()
            
            btn1=Button(frame,text="Previous",bg="#fff",fg="#FC4F67",command=lambda:other.requests(num-1))
            btn1.pack(side=LEFT)
            
            btn3=Button(frame,text="Cancel proposal",bg="#fff",fg="#FC4F67",command=lambda:self.cancelRequest(data[0][0],num,other))
            btn3.pack(side=LEFT)
            
            btn4=Button(frame,text="Next",bg="#fff",fg="#FC4F67",command=lambda:other.requests(num+1))
            btn4.pack(side=LEFT)
        if mode==5:
            frame=Frame(self._root)
            frame.pack()
            
            btn1=Button(frame,text="Previous",bg="#fff",fg="#FC4F67",command=lambda:other.matches(num-1))
            btn1.pack(side=LEFT)
            
            btn3=Button(frame,text="Cancel proposal",bg="#fff",fg="#FC4F67",command=lambda:self.unmatchCaller(data[0][0],num,other))
            btn3.pack(side=LEFT)
            
            btn4=Button(frame,text="Next",bg="#fff",fg="#FC4F67",command=lambda:other.matches(num+1))
            btn4.pack(side=LEFT)
            
                
        self._root.mainloop()
    
    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()
    def message(self,title,text):
        from tkinter import messagebox
        messagebox.showinfo(title,text)
    def connectaller(self,data,num,other):
        other.connect(data)
        other.proposals(num)
    def rejectcaller(self,data,num,other):
        other.reject(data)
        other.proposals(num)
    def cancelRequest(self,data,num,other):
        other.deleteRequest(data)
        other.requests(num)
    def unmatchCaller(self,data,num,other):
        other.unmatch(data)
        other.matches(num)
