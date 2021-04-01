from tkinter import *
import time
import tkinter.messagebox as tmsg

def getinfo():
    with open("rate.txt", "a") as f:
        f.write(f"{time.asctime()}\nName => {namevalue.get()}\nPhone => {phonvalue.get()}\nE=mail => {emailvalue.get()}\nRate => {s1.get()}\n\n")

    tmsg.showinfo("Thanks", "Thans for feedback\nWe will see you again")
root = Tk()
root.geometry("1200x700")
root.title("How would you rate us")

l1 = Label(text="Welcome to switz Restaurent", fg="blue", font=("times", 33, "bold"))
l1.grid(row=0, column=2)
l2 = Label(text="Name : ", font=("times", 22, "bold"))
l2.grid(row=1, column=1)
l3 = Label(text="Phon no. : ", font=("times", 22, "bold"))
l3.grid(row=2, column=1)
l4 = Label(text="E-mail : ", font=("times", 22, "bold"))
l4.grid(row=3, column=1)
l5 = Label(text="How much would you rate us", fg="blue", font=("times", 33, "bold"), pady=22)
l5.grid(row=4, column=2)

namevalue = StringVar()
phonvalue = StringVar()
emailvalue = StringVar()

i1 = Entry(root, textvariable=namevalue)
i1.grid(row=1, column=2)
i2 = Entry(root, textvariable=phonvalue)
i2.grid(row=2, column=2)
i3 = Entry(root, textvariable=emailvalue)
i3.grid(row=3, column=2)

s1 = Scale( from_=0, to=10, orient=HORIZONTAL, tickinterval=1)
s1.grid(row=5, column=2)


b1 = Button(root, text="Submit now", fg="blue" , width=77, command=getinfo)
b1.grid(row=6, column=2)



root.mainloop()