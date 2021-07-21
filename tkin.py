from tkinter import *
from cgpa_finder_1 import *
grade1= ''
cgpa1=''
window = Tk()
window.geometry("600x800")

top = Frame(window,height=250)
top.pack(fill=X)

bottom = Frame(window,height=550)
bottom.pack(fill=X)

def selected() :
    #labelstr3 = Label(bottom, text="Maths ", font="times 15 bold ").place(x=150,y=50)
    #labelstr4 = Label(bottom, text="B", font="times 15 bold ").place(x=370,y=50)
    global variable,grade1,cgpa1
    for widget in bottom.winfo_children():
        widget.destroy()
    sem = str(variable.get())
    reg_no = Reg_No_e.get()
    Chage(reg_no,sem)
    print(reg_no +"  " +sem)
    grade1,cgpa1 =  main_Fun()
    m=50
    labelstr = Label(bottom, text="Subject ", font="times 15 bold ").place(x=150,y=20)
    labelstr2 = Label(bottom, text="Grades", font="times 15 bold ").place(x=350,y=20)
    for k in grade1:
        labelstr3 = Label(bottom, text=k, font="times 15 bold ").place(x=150,y=m)
        labelstr4 = Label(bottom, text=grade1[k], font="times 15 bold ").place(x=370,y=m)
        m = m + 30

    labelstr4 = Label(bottom, text="CGPA : ", font="times 15 bold ").place(x=150, y=m+10)
    labelstr6 = Label(bottom, text=cgpa1, font="times 15 bold ").place(x=250, y=m+10)


title= Label(top,text="CGPA for SGGS Students ",font="times 30 bold ")
title.place(x=320,y=50,anchor="center")

Reg_No= Label(top,text="Reg No :  ",font="times 15 bold ")
Reg_No.place(x=200,y=100)

Reg_No_e = Entry(top,width=20,)
Reg_No_e.place(x=300,y=105)

semister_sel = Label(top,text="Semister :  ",font="times 15 bold ")
semister_sel.place(x=200,y=155)

list_of_sem = ['Semister 1','Semister 2','Semister 3','Semister 4','Semister 5','Semister 6','Semister 7','Semister 8']
variable = StringVar()
variable.set(list_of_sem[0])

drop1 = OptionMenu(top,variable,*list_of_sem)
drop1.place(x=300,y=155)

get_result = Button(window,text="Get Result",font="times 15 bold",width = 10,command=selected).place(x=320,y=220,anchor="center")

window.resizable(False,False)
window.mainloop()
