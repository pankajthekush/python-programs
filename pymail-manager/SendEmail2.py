from Forms import Forms
from EmailApi import LoginToGmail
lg = LoginToGmail()

frm = Forms(lg)
frm.LoginForm()
