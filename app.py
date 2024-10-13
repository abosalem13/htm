import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

# استخدام المتغيرات من البيئة
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # القيمة الافتراضية 587
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')
SENDER_PASS = os.getenv('SENDER_PASS')
RECEIVER_ADDRESS = os.getenv('RECEIVER_ADDRESS')

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
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_ADDRESS, SENDER_PASS)
            server.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, msg.as_string())
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='192.168.100.67', port=port, debug=True)
