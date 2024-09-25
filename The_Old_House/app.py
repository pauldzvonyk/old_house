from flask import Flask, request, render_template, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Contact form route
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Send email using SMTP (you can use a service like Gmail, SendGrid, etc.)
    send_email(name, email, subject, message)

    # Return a success response (you can handle this with AJAX in the front-end)
    return jsonify({'message': 'Email sent successfully!'})

# Email sending function
def send_email(name, email, subject, message):
    sender_email = "your-email@example.com"
    receiver_email = "contact@example.com"
    password = "your-email-password"

    # Creating the email content
    msg = MIMEText(f"From: {name}\nEmail: {email}\n\n{message}")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Sending the email
    with smtplib.SMTP_SSL('smtp.example.com', 465) as server:  # Use your email provider's SMTP settings
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)
