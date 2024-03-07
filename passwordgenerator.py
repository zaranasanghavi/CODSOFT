from tkinter import *
import string
import random

root = Tk()
root.geometry("500x500")
root.title("Password Generator App ")

def gen():
    n = int(e1.get())
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    p= []

    p.extend(list(s1))
    p.extend(list(s2))
    p.extend(list(s3))
    p.extend(list(s4))
    random.shuffle(p)
    pwd = p[0: n]
    l4 = Label(root, text="Password",fg= "dark blue", font="time 17 bold ")
    l4.place(x=190, y=230)
    l5 = Label(root, text = pwd, font="time 17 bold ")
    l5.place(x=120, y=290)


l1 = Label(root , text="Generate Password",fg= "dark blue" , font="time 17 bold ")
l1.place(x = 130 , y = 50)
l2 = Label(root , text="Enter password length:", fg= "dark blue" ,font="time 12")
l2.place(x = 155 , y = 100)
e1 = Entry(root, width= 30 , bd = 2, font= "time 15 bold")
e1.place(x = 80 , y = 130)
button = Button(root , text="Click Here!", fg="dark blue", bg="pink", font= "time 15 bold", width= 25 ,command= gen)
button.place(x = 90, y = 172)

root.mainloop()