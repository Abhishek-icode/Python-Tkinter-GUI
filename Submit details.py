from tkinter import *
import time
def getvals():
    with open("record.txt", "a") as f:
        f.write(f"The candidate information :- ({time.asctime()})\nName => {namevalue.get()}\nMobile number => {mobilevalue.get()}\nemail => {emailvalue.get()}\nAge => {agevalue.get()}\nGender => {gendervalue.get()}\nfood service => {foodvalue.get()}\n\n")
        print(f"The candidate information :-({time.asctime()})\nName => {namevalue.get()}\nMobile number => {mobilevalue.get()}\nemail => {emailvalue.get()}\nAge => {agevalue.get()}\nGender => {gendervalue.get()}\nfood service => {foodvalue.get()}")

root = Tk()
root.title("form details")
root.geometry("888x444")
Label(root, text="Welcome to flytravals", font=("times", 22, "bold"), pady=11).grid(row=0, column=2)
name = Label(root, text="Name : ")
mobile = Label(root, text="Mobile no. : ")
email = Label(root, text="email : ")
age = Label(root, text="Your age : ")
gender = Label(root, text="Your gender : ")

name.grid(row=1, column=1)
mobile.grid(row=2, column=1)
email.grid(row=3, column=1)
age.grid(row=4, column=1)
gender.grid(row=5, column=1)

namevalue= StringVar()
mobilevalue= StringVar()
emailvalue= StringVar()
agevalue= StringVar()
gendervalue= StringVar()
foodvalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
mobilentry = Entry(root, textvariable=mobilevalue)
emailentry = Entry(root, textvariable=emailvalue)
ageentry = Entry(root, textvariable=agevalue)
genderentery = Entry(root, textvariable=gendervalue)

nameentry.grid(row=1, column=2)
mobilentry.grid(row=2, column=2)
emailentry.grid(row=3, column=2)
ageentry.grid(row=4, column=2)
genderentery.grid(row=5, column=2)

foodser = Checkbutton(text="Do you want to book meals", variable=foodvalue)
foodser.grid(row=6, column=2)

Button(text="submit now", command=getvals).grid(row=7, column=2)

root.mainloop()