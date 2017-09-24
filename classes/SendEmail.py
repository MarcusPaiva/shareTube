import smtplib
from email.MIMEText import MIMEText

class SendNotification():

	def sendEmail( self, message, destination, subject ):
        """ Send email

            Args:
                message(String): Email body
                destination(List): Email destination list
                subject(String): Email subject
        """
	
		smtp = smtplib.SMTP( 'smtp.gmail.com', 587 )
		#Start connection to server and protocol port TLS

		smtp.starttls()
		#Start protocol

		smtp.login('edemcare@gmail.com', 'mypasswd')
		#Server authentication

		fromEmail = 'edemcare@gmail.com'
		#Origin email

		msg = MIMEText( '%s'% message, 'html', 'utf-8' )
		#insert into function a message using HTML with charset UTF-8

		msg['Subject'] = subject
		#Adding subject in message

		smtp.sendmail( fromEmail, destination, msg.as_string() )
		#Send email to recipients

		smtp.quit()
#End of function