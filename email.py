from email.message import EmailMessage
import ssl
import smtplib

# Sender's email credentials
email_sender = "xxxyyy@gmail.com"
email_password = "16 Digit 2 factor auth. code."

# List of email recipients
email_receivers = ["yyyxxx@gmail.com", "zzzttt@gmail.com"]

# Email content
subject = "Subject (HEADER)"
body = "Body (The main message)"

# Create SSL context for secure connection
context = ssl.create_default_context()

# Iterate through each recipient and send an individual email
for receiver_email in email_receivers:
    # Create a new email message for each recipient
    email = EmailMessage()

    # Set sender and recipient addresses, subject, and body
    email["From"] = email_sender
    email["To"] = receiver_email
    email["Subject"] = subject
    email.set_content(body)

    # Establish a secure connection and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver_email, email.as_string())

    # Print a message indicating that the email has been sent
    print(f"Email sent to {receiver_email}")