import tkinter as tk
from EmailApi import LoginToGmail


class Forms:


    #lg.Login("derrickhoffman0012","test")


    def LoginForm(self):

        root = tk.Tk()
        root.title("Login Form")
        root.geometry("300x100")

        lbl_username = tk.Label(text="User Name")
        lbl_password = tk.Label(text="Password")

        txt_Username = tk.Entry()
        txt_Password = tk.Entry()
        print("Here")

        lbl_username.grid(row=1,column=0)
        lbl_password.grid(row=2,column=0)

        txt_Password.grid(row=1,column=1)
        txt_Username.grid(row=2,column=1)


        btn_Login = tk.Button(text="Login",command=self.sendLogin())
        btn_Login.grid(row=3,column=1)

        root.mainloop()

    def sendLogin():
        lg = LoginToGmail()
        lg.Login("test","tet")
