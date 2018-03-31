
#IMPORT SMTP LIBERARY
import smtplib
import tkinter as tk

###CREATE SMTP SESSION
##_session = smtplib.SMTP('smtp.gmail.com',587)
##
###START TLS FOR SECURITY
##_session.starttls() 
##
###AUTHENTICATION , IF YOUR ACCOUNT USES 2 STEP VERIFICATION THEN ENTER APP SPESIFIC PASSWORD
###https://myaccount.google.com/u/0/security
##
##_session.login("USERNAME","PASSWORD") 
##
##
##_message = "This Is A Message"
##_session.sendmail("panakjthekush@gmail.com","pankajthekush@gmail.com",_message)
##_session.quit()


#INITIALIZE WINDOW
window = tk.Tk()

window.title("Email Manager")
window.geometry("400x400")

title = tk.Label(text="Email Manager Tool")
title.grid();

btnProcess = tk.Button(text="Process")
btnProcess.grid(column=0,row=50)


window.mainloop()
