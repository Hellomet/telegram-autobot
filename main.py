from flask import Flask, request
import requests

TOKEN = 'ใส่-BOT-TOKEN-ของคุณ'
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

app = Flask(__name__)  # <-- บรรทัดสำคัญที่ทำให้ gunicorn หาเจอ

@app.route('/')
def home():
    return '🤖 Bot is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        reply = f"คุณพิมพ์ว่า: {text}\\n🤖 ตอบกลับอัตโนมัติ!"
        requests.post(API_URL, data={'chat_id': chat_id, 'text': reply})
    return 'ok'

if __name__ == '__main__':
    app.run()
