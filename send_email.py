
# need to genrate the app password from https://support.google.com/accounts/answer/185833
import smtplib
from constants import constant

sender = 'malamcsc@gmail.com'
receivers = ['ilhanalam4@gmail.com']
password = constant.password
message = """ you programme is executed.
          """

message = 'Subject: {}\n\n{}'.format("JOB_RESULT", message)


def send_notification():
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, receivers, message)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)

if __name__ == "__main__":
    send_notification()

