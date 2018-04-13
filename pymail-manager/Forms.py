import tkinter as tk
from tkinter import *


class Forms:

    def __init__(self,loginAPiClass):
        self.root = tk.Tk()
        #self.root.resizable(False, False)
        self.lbl_username = tk.Label(text="User Name")
        self.lbl_password = tk.Label(text="Password")
        self.txt_Username = tk.Entry()
        self.txt_Password = tk.Entry(show="*")
        self.loginAPiClass  = loginAPiClass
        self.sender_email_id = None
        self.status = False
        self.msgSenDTo
        self.msgBody


    def LoginForm(self):

        self._login_status = False
        self.root.title("Login Form")
        self.root.geometry("300x100")

        self.lbl_username.grid(row=1,column=0)
        self.lbl_password.grid(row=2,column=0)

        self.txt_Username.grid(row=1,column=1)
        self.txt_Password.grid(row=2,column=1)


        btn_Login = tk.Button(text="Login",command=self.sendLogin)

        btn_Login.grid(row=3,column=1)

        self.root.mainloop()

    def sendLogin(self):
        uname = str(self.txt_Username.get())
        pwd =   str(self.txt_Password.get())


        _status = self.loginAPiClass.Login(uname,pwd)

        if _status != True:
            self.msgbox("Error While Logging In","Error")
        else:
             self.status = True
             self.sender_email_id = uname + "@gmail.com"
             self.root.destroy()

    def msgbox(self,MessageString,titleString):

            top = tk.Toplevel()
            top.geometry("200x100")
            top.title(titleString)

            msg = tk.Message(top, text=MessageString)
            msg.pack()
            button = tk.Button(top, text="Dismiss", command=top.destroy)
            button.pack()

        # lbl_ErrorString = tk.Label(text=MessageString)
        # #lbl_ErrorString.place(msgroot,relx=.5, rely=.5, anchor="center")
        # lbl_ErrorString.grid(msgroot,row=0,column=0)
        # msgroot.mainloop()

    def SendEmail(self):


        self.root.title("Send And Email")
        self.root.geometry("568x500")
        for rw in range(10):
            self.root.rowconfigure(rw,weight=1)

        for cl in range(5):
            self.root.columnconfigure(cl,weight=1)


        frame_email_info = tk.Frame(bg="red")
        frame_email_info.grid(row = 0, column = 0, rowspan = 1, columnspan = 3, sticky = W+E+N+S)


        blank_Cell_receiver = tk.Label(frame_email_info,text="self.root")
        #NOW PUT THE SENDER EMAIL AND RECEIVER EMAIL FIELD IN THIS FRAME

        #ADDING LABLES and textboxes

        #sender
        blank_Cell_sender = tk.Label(frame_email_info,text="        ") #TO KEEP THE SPACING BETWEEN THE COLUMNS , BECAUSE THE DEFAULT CELL SIZE IS 0

        lbl_senderEmail = tk.Label(frame_email_info,text="Sender Email")
        lbl_senderEmail.grid(row=0,column=0)


        txt_sender = tk.Entry(frame_email_info)
        txt_sender.grid(row=0,column=3)
        blank_Cell_sender.grid(row=0,column=2)

        #RECEIVER

        blank_Cell_Receiver = tk.Label(frame_email_info,text="        ") #TO KEEP THE SPACING BETWEEN THE COLUMNS , BECAUSE THE DEFAULT CELL SIZE IS 0

        lbl_receiveremail = tk.Label(frame_email_info,text="Sender Email")
        lbl_receiveremail.grid(row=1,column=0)


        txt_receiver = tk.Entry(frame_email_info)
        txt_receiver.grid(row=1,column=3)
        blank_Cell_Receiver.grid(row=1,column=2)

        #NOW THE EMAIL BODY

        Frame_TextBody = tk.Frame(bg="red")
        Frame_TextBody.grid(row = 1, column = 0, rowspan = 3, columnspan = 4, sticky = W+E+N+S)



        txt_Email_Body = tk.Text(Frame_TextBody,height=30, width=80)
        #SCROLLBAR
        self.root.rowconfigure(1, weight=3)

        scroll = Scrollbar(self.root, command=txt_Email_Body.yview)
        txt_Email_Body.configure(yscrollcommand=scroll.set)
        txt_Email_Body.grid(row=0,column=0)
        scroll.grid(row=1,column=10,sticky='NS')


        #SEND EMAIL Button

        btn_send_Email = tk.Button(self.root,text="Send Email")
        btn_send_Email.grid(row=4,column=0)

        self.msgSenDTo = 
        self.root.mainloop()
