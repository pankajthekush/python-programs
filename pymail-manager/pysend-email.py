
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





def Connection_Status(isSuccess) :
    if isSuccess == True:
        lbl_login_password = tk.Label(text="Connection Successful")
        lbl_login_password.grid(row=2,column=3)
    elif isSuccess == False :
        lbl_login_password = tk.Label(text="Connection Failed")
        lbl_login_password.grid(row=2,column=3)


def Create_Session() :
    _session = smtplib.SMTP('smtp.gmail.com',587)
    _session.starttls()


    uname = str(ent_Login_Email.get())
    pwd = str(ent_Login_Password.get())



    try :
        _session.login(uname,pwd)
    except(smtplib.SMTPAuthenticationError) as e:
        print("Username Password Incorrect")
        print(str(e))
        Connection_Status(False)
    else:
        print("Connection Successful")
        Connection_Status(True)
    finally:
        _session.quit()
        




#INITIALIZE WINDOW
window = tk.Tk()

window.title("Email Sender")
window.geometry("400x500")

#TITLE
title = tk.Label(text="Email Sender Tool")
title.grid(column=0,row=0);


#Label For Email Text Field
lbl_Login_Email = tk.Label(text="User Name")
lbl_Login_Email.grid(column=0,row=1)


#Login Email Text Field
ent_Login_Email = tk.Entry()
ent_Login_Email.grid(column=1,row=1)


#Label for Passwod Test Field
lbl_login_password = tk.Label(text="Password")
lbl_login_password.grid(row=2,column=0)

#Password Entry Field
ent_Login_Password = tk.Entry(show="*")
ent_Login_Password.grid(row=2,column=1)


btnProcess = tk.Button(text="Login", command=Create_Session)
btnProcess.grid(column=1,row=3)




window.mainloop()
