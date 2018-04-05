import tkinter as tk



class Forms:

    def __init__(self,loginAPiClass):
        self.root = tk.Tk()
        self.lbl_username = tk.Label(text="User Name")
        self.lbl_password = tk.Label(text="Password")
        self.txt_Username = tk.Entry()
        self.txt_Password = tk.Entry()
        self.loginAPiClass  = loginAPiClass

    def LoginForm(self):


        self.root.title("Login Form")
        self.root.geometry("300x100")

        print("Here")

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

        print(uname)
        print(pwd)
        _status = self.loginAPiClass.Login(uname,pwd)
        print(_status)

        if _status != True:
            self.msgbox("Error While Logging In","Error")


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
    
