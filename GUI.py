from tkinter import *
from tkinter import messagebox  
window=Tk()
window.title("GUI")
window.geometry('1000x1000')

def main():
    print("1.LABEL 2.CHECKBOX 3.RADIO 4.TEXTBOX 5.CUSTOM DIALOGUE BOX")
    ch = int(input("ENTER YOUR CHOICE:"))
	
    if(ch==1):
       Label1()
    elif(ch==2):
       Checkbox()
    elif(ch==3):
       Radio();
    elif(ch==4):
       Textbox();
    elif(ch==5):
       CustomD();
    else:
       print("please make valid choice")

def Label1():
    w=Label(window,text="HELLO WORLD!",font=("Arial Bold",15))
    w.pack()
    window.geometry("350x200")


def Checkbox():
    var1 = IntVar()
    Label(window,text='LANGUAGES:',font=("Arial Bold",10)).grid(row=0)
    Checkbutton(window, text="JAVA", variable=var1).grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(window, text="PYTHON", variable=var2).grid(row=2, sticky=W)
    var3 = IntVar()
    Checkbutton(window, text="C PROGRAMMING", variable=var3).grid(row=3, sticky=W)
    var4 = IntVar()
    Checkbutton(window, text="C++ PROGRAMMING", variable=var4).grid(row=4, sticky=W)
    var5 = IntVar()
    Checkbutton(window, text="NONE OF THE ABOVE", variable=var5).grid(row=5, sticky=W)	 
		 
def Radio():
    Label(window,text='GENDERS:',font=("Arial Bold",10)).grid(row=0)
    rad1=Radiobutton(window,text='FEMALE',value=1)
    rad2=Radiobutton(window,text='MALE',value=2)
    rad3=Radiobutton(window,text='OTHERS',value=3)
    rad1.grid(column=0,row=1)
    rad2.grid(column=0,row=2)
    rad3.grid(column=0,row=3)  	 
		 
def Textbox():
    Label(window,text='DETAILS:',font=("Arial Bold",10)).grid(row=0)
    Label(window,text='FIRST NAME:').grid(row=1)
    Label(window,text='LAST NAME:').grid(row=2)
    Label(window,text='ADDRESS:').grid(row=3)
    entry1=Entry(window).grid(row=1,column=1)
    entry2=Entry(window).grid(row=2,column=1)
    entry3=Entry(window).grid(row=3,column=1)
		  
def CustomD():
    window.withdraw()
    messagebox.askquestion("Confirm","Are you sure you want to quit?")
		  
main()
		  
		  
		  
		  
		  
		  
		  
		  
		  
		  
