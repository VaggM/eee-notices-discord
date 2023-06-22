from MailSender import MailSender

# Email configuration

sender_email = "vaggtester@gmail.com"  # Your Gmail address
password = "fyqwmdipdshmlium"  # Your Gmail password

sender = MailSender(sender_email, password)

receiver_email = "vagosmitikas@gmail.com"  # Recipient's email address

# Email content
subject = "Hello from Python!"
message = "Hi, this is a test email."

sender.send(receiver_email, subject, message)

print("Email sent successfully!")
