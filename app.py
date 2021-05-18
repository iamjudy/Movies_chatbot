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

Before='1：Me You and Five Bucks \n2：The Great Gatsby \n3：Lolita \n4：The Shipping News\n5：Atonement'
Begin='1：Down & Out With The Dolls \n2：Me You and Five Bucks \n3：There is Always Woodstock \n4：Along the Roadside\n5：Just Like Heaven'
Holiday='1：Bridget Jones Diary \n2：Me You and Five Bucks \n3：What Women Want \n4：Bridget Jones: The Edge of Reason\n5： The Sweetest Thing'

Black='1：Men in Black \n2：Men in Black 3 \n3：Wild Wild West \n4：Bad Boys II\n5： Charlies Angels: Full Throttle'
Inception='1：Looper \n2：Premium Rush \n3：Timecop \n4：The One\n5：Surrogates'
Avatar='1：Clash of the Titans \n2：The Mummy: Tomb of the Dragon Emperor \n3：The Monkey King 2 \n4：G-Force\n5： The Time Machine'

Godfather='1：The Godfather: Part III \n2：The Godfather: Part II \n3：Amidst the Devils Wings \n4：The Son of No One\n5： Apocalypse Now'
Redemption='1：Dark Blue \n2：Witness \n3： Amidst the Devils Wings \n4：Dead Man Walking\n5：The Hudsucker Proxy'
Imitation='1：The Duchess \n2：The Fifth Estate\n3：Milk \n4： A Dangerous Method\n5： The Railway Man'

OK ='謝謝你的滿意～\n還想看其他電影類型推薦的話，\n可以再次輸入「我想看電影」唷！'
NONO ='收到了QQ。\n這只是我們的一小步，\n請期待後續的改良和進步！'


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
    elif 'Romance' in msg:
        message = Carousel_Template_Romance()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'fiction' in msg:
        message = Carousel_Template_fiction()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Drama' in msg:
        message = Carousel_Template_Drama()
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Spider' in msg:
        message1 = TextSendMessage(text=Spider)
        message2 = Confirm_Template()
        message = [message1, message2]
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
    elif 'Before' in msg:
        message = TextSendMessage(text=Before)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Begin' in msg:
        message = TextSendMessage(text=Begin)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Holiday' in msg:
        message = TextSendMessage(text=Holiday)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Black' in msg:
        message = TextSendMessage(text=Black)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Inception' in msg:
        message = TextSendMessage(text=Inception)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Avatar' in msg:
        message = TextSendMessage(text=Avatar)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif 'Godfather' in msg:
        message = TextSendMessage(text=Godfather)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Redemption' in msg:
        message = TextSendMessage(text=Redemption)
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Imitation' in msg:
        message = TextSendMessage(text=Imitation)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    elif '可以唷' in msg:
        #message1 = TextSendMessage(text=OK)
        message = {
            'type': '8525',
            'packageId': '1',
            'stickerId': '16581296'
        }
        #message = [message1, message2]
        line_bot_api.reply_message(event.reply_token, message)
    elif 'No' in msg:
        message = TextSendMessage(text=NONO)
        line_bot_api.reply_message(event.reply_token, message)
    ###
    else:
        message = TextSendMessage(text=Default)
        line_bot_api.reply_message(event.reply_token, message)

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
