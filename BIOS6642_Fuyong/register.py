from tkinter import *
def Register_User():
    username_info=usernames.get()
    password_info=password.get()
    file=open(account_code+".csv", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registeration Success", fg="green", front=("Calibri", 11)).pack()

def Register():
    screem1 = Topelevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    userentry=Entry(screen1, textvariable = username)
    userentry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry=Entry(screen1, textvariable = password)
    passwor_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user). pack()

def Screen():
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(screen, text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screen, text = "").pack
    Button(screen, text = "Login", width = "30", height = "2", command = Login).pack
    Label(screen, text = "Creat Account").pack()
    Button(screen, text = "Login", width = "30", height = "2", command = Register).pack
    screen.mainloop()

Screen()
