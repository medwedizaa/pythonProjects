import smtplib
from hidden_config_file import my_email, password

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    message = "Subject:Hello\n\nThis is the whole body of my email."
    connection.sendmail(from_addr=my_email, to_addrs="al_t26@yahoo.com", msg=message)
