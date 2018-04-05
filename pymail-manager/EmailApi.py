import smtplib


class LoginToGmail:
    def Login(self,usrname,password):
        _session = smtplib.SMTP('smtp.gmail.com','587')
        _session.starttls()

        try:
            _session.login(usrname,password)
            _status = True
        except(smtplib.SMTPAuthenticationError) as e:
            print("Username Password Incorrect")
            print(str(e))
            _status = False
        finally:
            _session.quit
            return _status

# lg = LoginToGmail()
# lg.Login("derrickhoffman0012","playagain@786")
