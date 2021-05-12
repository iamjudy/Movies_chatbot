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

Default='感謝您的訊息！\n很抱歉，本帳號沒有那麼聰明QQ，請輸入神秘的 keyword 來開啟對話哦。'

Spider='1：Spider-Man 2 \n2：Spider-Man \n3：The Sorcerers Apprentice \n4：Prince of Persia: The Sands of Time\n5：The Mummy: Tomb of the Dragon Emperor'
Mad='1：Damnation Alley \n2：The Blood of Heroes \n3：The Time Machine \n4：Mad Max Beyond Thunderdome\n5：Battle for the Planet of the Apes'
Skyfall='1：Spectre \n2：Quantum of Solace \n3：Mission: Impossible - Rogue Nation \n4：Tomorrow Never Dies\n5：Casino Royale'

Witch='1：Book of Shadows: Blair Witch \n2：The Blair Witch Project \n3：Saw VI \n4：Truth or Dare\n5：The Unborn'
Aliens='1：Alien \n2：Unnatural \n3：The Abyss \n4：The Terminator\n5：Alien: Resurrection'
Mama='1：Gods of Egypt \n2：Headhunters \n3：Lesbian Vampire Killers \n4：American Beast\n5：Teeth and Blood'

Spirited='1：Howls Moving Castle \n2：Oz: The Great and Powerful \n3：The Thief and the Cobbler \n4：Return to Never Land\n5：Princess Mononoke'
Inside='1：Me You and Five Bucks \n2：I Married a Strange Person! \n3：Anywhere But Here \n4：The Cookout\n5：Up'
Ratatouille='1：Meet the Deedles \n2：Alpha and Omega: The Legend of the Saw Tooth Cave \n3：Rugrats in Paris: The Movie \n4：The Nut Job\n5：The Rugrats Movie'




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
    ###
    elif 'Action' in msg:
        message = Carousel_Template_Action()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Horror' in msg:
        message = Carousel_Template_Horror()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Animation' in msg:
        message = Carousel_Template_Animation()
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Spider' in msg:
        message = TextSendMessage(text=Spider)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Mad' in msg:
        message = TextSendMessage(text=Mad)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Skyfall' in msg:
        message = TextSendMessage(text=Skyfall)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Witch' in msg:
        message = TextSendMessage(text=Witch)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Aliens' in msg:
        message = TextSendMessage(text=Aliens)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Mama' in msg:
        message = TextSendMessage(text=Mama)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Spirited' in msg:
        message = TextSendMessage(text=Spirited)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Inside' in msg:
        message = TextSendMessage(text=Inside)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Ratatouille' in msg:
        message = TextSendMessage(text=Ratatouille)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    else:
        message = TextSendMessage(text=Default)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
