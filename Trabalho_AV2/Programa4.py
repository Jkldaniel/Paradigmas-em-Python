###################################
#Daniel Soares Oliveira da Silva  #
#202102410241                     #
#Programa 4                       #
###################################

from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("Usuário :", username.get())
	print("Senha :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('260x120')  
tkWindow.title('Programa4')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Usuário").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Senha").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Entrar", command=validateLogin).grid(row=5, column=1)  

tkWindow.mainloop()