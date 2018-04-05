import smtplib

class LoginToGmail:
    def Login(self,usrname,password):
        _session = smtplib.SMTP('smtp.gmail.com','587')
        _session.starttls()

        try:
            _session.login(usrname,password)
        except(smtplib.SMTPAuthenticationError) as e:
            print("Username Password Incorrect")
            print(str(e))
        finally:
            _session.quit


# lg = LoginToGmail()
# lg.Login("derrickhoffman0012","playagain@786")
