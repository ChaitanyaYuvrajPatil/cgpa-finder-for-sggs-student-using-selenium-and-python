from tkinter import *
from cgpa_finder_1 import *
from tkinter.ttk import Combobox
grade1= ''
cgpa1=''
window = Tk()
window.geometry("700x800")
####Functions

def selected() :
    global variable,grade1,cgpa1
    sem = str(variable.get())
    reg_no = Reg_No_e.get()
    Chage(reg_no,sem)
    print(reg_no +"  " +sem)
    grade1,cgpa1 =  main_Fun()
    for k in grade1:
        labelstr = Label(window, text=k, font="times 15 bold ").pack()
        labelstr2 = Label(window, text="  " + grade1[k], font="times 15 bold ").pack()
        # m=m+1
    '''m = 1
    for k in grade1:
        labelstr = Label(window, text=k , font="times 15 bold ").grid(row=5, column=1)
        labelstr2 = Label(window, text= "  "+grade1[k], font="times 15 bold ").grid(row=5, column=2)
        m=m+1'''


###################################################

title= Label(window,text="CGPA for SGGS Students ",font="times 30 bold ")
title.place(x=350,y=50,anchor="center")

Reg_No= Label(window,text="Reg No :  ",font="times 15 bold ")
Reg_No.place(x=200,y=100)

Reg_No_e = Entry(window,width=20,)
Reg_No_e.place(x=300,y=105)

semister_sel = Label(window,text="Semister :  ",font="times 15 bold ")
semister_sel.place(x=200,y=155)

list_of_sem = ['Semister 1','Semister 2','Semister 3','Semister 4','Semister 5','Semister 6','Semister 7','Semister 8']
variable = StringVar()
variable.set(list_of_sem[0])

drop1 = OptionMenu(window,variable,*list_of_sem)
drop1.place(x=300,y=155)

get_result = Button(window,text="Get Result",font="times 15 bold",width = 10,command=selected).place(x=350,y=250,anchor="center")


for k in grade1:
    labelstr = Label(window, text=k , font="times 15 bold ").pack()
    labelstr2 = Label(window, text= "  "+grade1[k], font="times 15 bold ").pack()
    #m=m+1

window.mainloop()


'''semister_sel_drop = Combobox(window, textvariable=variable)
semister_sel_drop['values'] = list_of_sem
semister_sel_drop.place(x=300,y=155)

semister_sel_drop.current()
print(semister_sel_drop.get())'''



