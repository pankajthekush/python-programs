from Forms import Forms
from EmailApi import LoginToGmail
lg = LoginToGmail()

frm = Forms(lg)
frm.LoginForm()

if frm.status:
    print("We will Send Email Now")
    frm = None
    frm = Forms(lg)
    frm.SendEmail()
else:
    print("Email Send Module Not Loaded")
