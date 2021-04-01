from tkinter import *
def update():
    root.geometry(f"{widthval.get()}x{heightval.get()}")

root = Tk()
root.geometry("666x333")
root.title("Change window size")

Label(root, text="Width : ", font=("times", 18, "bold")).grid(row=0, column=0)
Label(root, text="Height : ", font=("times", 18, "bold")).grid(row=1, column=0)

widthval =StringVar()
heightval =StringVar()

Entry(root, textvariable=widthval).grid(row=0, column=1)
Entry(root, textvariable=heightval).grid(row=1, column=1)

Button(root, text="Apply", command=update).grid(row=2, column=1)
root.mainloop()