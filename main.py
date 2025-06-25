
from flask import Flask, request
from bot import handle_update
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running.'

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    return handle_update(update)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
