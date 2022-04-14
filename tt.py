# import tkinter

# window = tkinter.Tk()
# btn1 = tkinter.Button(window,text="hello",width=50,command=window.destroy)
# btn1.pack()
# window.mainloop()


# from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.title("Registration Form")

Registration = tk.Label(root, text="Registration form",width=20,font=("bold", 20))
Registration.place(x=90,y=53)


FullName = tk.Label(root, text="FullName",width=20,font=("bold", 10))
FullName.place(x=80,y=130)

entry_1 = tk.Entry(root)
entry_1.place(x=240,y=130)

Email = tk.Label(root, text="Email",width=20,font=("bold", 10))
Email.place(x=68,y=180)

entry_2 = tk.Entry(root)
entry_2.place(x=240,y=180)

Gender = tk.Label(root, text="Gender",width=20,font=("bold", 10))
Gender.place(x=70,y=230)
var = tk.IntVar()
tk.Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
tk.Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

Age = tk.Label(root, text="Age:",width=20,font=("bold", 10))
Age.place(x=70,y=280)


entry_2 = tk.Entry(root)
entry_2.place(x=240,y=280)

tk.Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()
print("registration form  seccussfully created...")