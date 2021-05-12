from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from message import *


import tempfile, os
import datetime
import time

Default='感謝您的訊息！\n很抱歉，本帳號沒有那麼聰明QQ，請輸入神秘的 keyword 開啟對話。'

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('iYDxt8AjWwpiBlgXM54EYUQkY9/luGnQ5pHFAb8bDE3i3qLE0SxmmJSOrM1E30Tg+SNQPh8J8CCIuFwXsEkLvgA5qH0+D/y3PeFJikgvuQG1DpvpUmJHDi24xUwuHzhpzXovODZDglXmNfaC7sk2gAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e77911630a2ea8108ba8a8354f2773e7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '我想看電影' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '蛤～還有勒' in msg:
        message = buttons_message2()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我都不要看！' in msg:
        message = TextSendMessage(text='那...那我也沒辦法。')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Action' in msg:
        message = Carousel_Template_Action()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=Default)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
