import smtplib
import keyring
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage


# Open connection to server
# using credentials stored
# via keyring lib
def openConnection():
	smtpObj = smtplib.SMTP()
	smtpObj.connect(keyring.get_password('RPIemail', 'SMTP-URL'), int(keyring.get_password('RPIemail', 'SMTP-Port')))
	smtpObj.ehlo()
	smtpObj.login(keyring.get_password('RPIemail', 'emailFrom'), keyring.get_password('RPIemail', 'emailPass'))

	return smtpObj

# Create the email message
# and attach the photo
# taken with the camera module
def createMessage(inputFile):
	# Compose email
	msg = MIMEMultipart()
	msg['From'] = keyring.get_password('RPIemail', 'emailFrom')
	msg['To'] = keyring.get_password('RPIemail', 'emailTo')
	msg['Subject'] = 'Raspberry Spy '+ datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
	message = 'Photo is attached'
	msg.attach(MIMEText(message))
	
	# Attach file
	fp = open(inputFile, 'rb')
	img = MIMEImage(fp.read())
	fp.close()
	msg.attach(img)
	
	return msg

# Send the message with
# attached file
def sendMessage(inputFile):
	smtpObj = openConnection()
	msg = createMessage(inputFile)

	try:
		smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
		print "Successfully sent email"

		# Sever connection
		smtpObj.quit()
	except:
		print "Unable to send email"