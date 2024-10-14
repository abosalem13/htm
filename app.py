import os
from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

# إعداد بيانات البريد الإلكتروني
SMTP_SERVER = "smtp.mailersend.net"
SMTP_PORT = 587
SENDER_ADDRESS = "MS_fLonPd@trial-351ndgw2mvqgzqx8.mlsender.net"
SENDER_PASS = "53rvL5nt4mwfRmdG"
RECEIVER_ADDRESS = "imobilejo@outlook.com"

# الدالة الرئيسية لإرسال البريد
def send_email():
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_ADDRESS, SENDER_PASS)
            message = f"Subject: Test Email\n\nThis is a test email from your Flask app."
            server.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# المسار الرئيسي الذي يرسل البريد الإلكتروني
@app.route('/')
def index():
    success = send_email()
    if success:
        return "Email sent successfully!"
    else:
        return "Failed to send email.", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # المنفذ المتاح من Render
    app.run(host='0.0.0.0', port=port)
