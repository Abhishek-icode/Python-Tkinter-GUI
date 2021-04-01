from tkinter import *
def getvals():
    print(f"Name of the candidate is {namevalue.get()}")
    print(f"Password of the candidate is {passvalue.get()}")
root = Tk()
root.geometry("888x444")
root.title("Log in")

Label(root, text="Log in here :- ", font=("times", 33, "bold")).grid(row=0, column=1)
Label(root, text="Name : ", font=("times", 15, "bold")).grid(row=1, column=1)
Label(root, text="Password : ", font=("times", 15, "bold")).grid(row=2, column=1)

namevalue = StringVar()
passvalue = StringVar()

nameentry = Entry(root, textvariable=namevalue).grid(row=1, column=2)
passentry = Entry(root, textvariable=passvalue).grid(row=2, column=2)

Button(text="submit now", command=getvals).grid(row=3, column=2)

root.mainloop()