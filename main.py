from flask import Flask, request
import requests

TOKEN = '7528347229:AAH_sM9kOBvoL1gHbqOVo5YK0GrV5FiLU8o'
API_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

app = Flask(__name__)

@app.route('/')
def home():
    return '🤖 Bot is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        reply = f"คุณพิมพ์ว่า: {text}\n🤖 นี่คือการตอบกลับอัตโนมัติ!"
        payload = {
            'chat_id': chat_id,
            'text': reply
        }
        requests.post(API_URL, data=payload)
    return 'ok'

if __name__ == '__main__':
    app.run()
