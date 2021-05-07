import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'pedro.meiodia@hotmail.fr'
email['to'] = 'pedro.meiodia@hotmail.fr'
email['subject'] = 'Give thanks!'
email.set_content('You did it, Brother')

with smtplib.SMTP(host='outlook-emeacenter3.office365.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('pedro.meiodia@hotmail.fr', 'Qazwsx387')
	smtp.send_message(email)
