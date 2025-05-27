import requests

TOKEN = '7528347229:AAH_sM9kOBvoL1gHbqOVo5YK0GrV5FiLU8o'
WEBHOOK_URL = 'https://your-render-app-name.onrender.com/webhook'

url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
res = requests.post(url, data={'url': WEBHOOK_URL})
print(res.json())
