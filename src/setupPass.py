import keyring
import getpass

# Currently set to use
# the keyring lib exclusively
# to hold credentials
def setEmailPassword():
	print "Enter your email"
	emailSending = raw_input("> ")
	print "Enter your email's password"
	emailPass = getpass.getpass()
	print "Enter the email you are sending to"
	emailReceiving = raw_input("> ")
	print "Enter your SMTP URL"
	smtpUrl = raw_input("> ")
	print "Enter the SMTP port number"
	smtpPort = raw_input("> ")


	keyring.set_password('RPIemail', 'emailFrom', emailSending)
	keyring.set_password('RPIemail', 'emailPass', emailPass)
	keyring.set_password('RPIemail', 'emailTo', emailReceiving)
	keyring.set_password('RPIemail', 'SMTP-URL', smtpUrl)
	keyring.set_password('RPIemail', 'SMTP-Port', smtpPort)

# Check for existed archive
# TO DO: Check connection
# and ask if user needs to
# reset credential
def archiveCheck():
	checkedArchive = keyring.get_password('RPIemail', 'emailFrom')

	if checkedArchive == None:
		setEmailPassword()