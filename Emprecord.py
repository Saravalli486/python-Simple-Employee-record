
from tkinter import *
from tkinter import messagebox
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(Ename.get(),Eid.get(),contact.get(),Address.get(),mailid.get()):
        list1.insert(END,row)

def add_command():
    print(var.get())
    validation(contact.get())
    backend.insert(Ename.get(),Eid.get(),contact.get(),Address.get(),mailid.get())
    list1.delete(0,END)
    list1.insert(END,(Ename.get(),Eid.get(),contact.get(),Address.get(),mailid.get()))
def validation(mob):
    if mob.isdigit() and len(mob)==10:
        pass
    else:
        messagebox.showerror(title=None, message="Enter a valid mobile no")
    
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],Ename.get(),Eid.get(),contact.get(),Address.get(),mailid.get())
def selection():
    choice = var.get()
    '''if choice == 1:
        m = 'Male'
    elif choice == 2:
        m = 'Female'''
    #Label.config(text=choice)
    return choice
window=Tk()

window.wm_title("Employee Record")
window.configure(width=1500,height=600)
window.geometry('500x400')


l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="ID")
l2.grid(row=1,column=0)

l3=Label(window,text="Mob No")
l3.grid(row=2,column=0)

l4=Label(window,text="Address")
l4.grid(row=3,column=0)

l5=Label(window,text="MailId")
l5.grid(row=4,column=0)

Ename=StringVar()
e1=Entry(window,textvariable=Ename)
e1.grid(row=0,column=1)

Eid=StringVar()
e2=Entry(window,textvariable=Eid)
e2.grid(row=1,column=1)

contact=StringVar()
e3=Entry(window,textvariable=contact)
e3.grid(row=2,column=1)

Address=StringVar()
e4=Entry(window,textvariable=Address)
e4.grid(row=3,column=1)
mailid=StringVar()
e5=Entry(window,textvariable=mailid)
e5.grid(row=4,column=1)
var=StringVar()
Radiobutton(window, text='male', variable=var,value="Male",command=selection).grid(row=5,column=0)
Radiobutton(window, text='Female', variable=var,value="Female",command=selection).grid(row=5,column=1)

list1=Listbox(window, height=6,width=35)
list1.grid(row=6,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=6,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
