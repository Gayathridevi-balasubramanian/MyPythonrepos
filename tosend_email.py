import smtplib

def send_email(reciever_email, subject, body):
    message = f'subject: {subject}\n{body}'
    user = input("Please enter the user name:")
    passwords = input("Please enter the password")
    with smtplib.SMTP( 'smtp.gmail.com', 587) as server:  # also try using smtp.office365.com instead of the smtp.gmail.com
        server.starttls()
        server.login(user,passwords)
        server.sendmail(user,reciever_email,message)

try:
    send_email('manoj2.g@gmail.com','Hallo', 'there is something else ')
    print("Successfully sent")
except Exception as e:
    print(f"Error : {e}")


