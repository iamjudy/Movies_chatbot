#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='看電影前，先聊個天',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/Mfs13Tf.jpg",
            title='今晚，我想來看點？',
            text='選個電影種類，讓我更好推薦你！',
            actions=[
                MessageTemplateAction(
                    label='Action 動作',
                    text='Action 動作'
                ),
                MessageTemplateAction(
                    label='Horror 恐怖',
                    text='Horror 恐怖'
                ),
                MessageTemplateAction(
                    label='Animation 動畫',
                    text='Animation 動畫'
                ),
                MessageTemplateAction(
                    label="蛤～還有勒",
                    text="蛤～還有勒"
                )
            ]
        )
    )
    return message

def buttons_message2():
    message = TemplateSendMessage(
        alt_text='那這些呢',
        template=ButtonsTemplate(
            thumbnail_image_url="https://i.imgur.com/Ucf3cqF.jpg",
            title='今晚，我想來看點？',
            text='選個電影種類，讓我更好推薦你！',
            actions=[
                MessageTemplateAction(
                    label='Darma 劇情',
                    text='Darma 劇情'
                ),
                MessageTemplateAction(
                    label='Science fiction 科幻',
                    text='Science fiction 科幻'
                ),
                MessageTemplateAction(
                    label='Romance 浪漫',
                    text='Romance 浪漫'
                ),
                MessageTemplateAction(
                    label="我都不要看！",
                    text="我都不要看！"
                )
            ]
        )
    )
    return message


#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='Action 動作類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://2.bp.blogspot.com/-dV1ZUcm5s24/WUb-pLm0A7I/AAAAAAAAP00/yR4Tu87gesEPqn1Ud3VgedgbcLIwXRKeACLcBGAs/s1600/Sfdhgkhyjuop3.jpg',
                    title='Spider-Man 3',
                    text='我說的是2007版本，沒有Tom Holland。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Spider-Man 3'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/9/92/Mad_Max_Fury_Road_Soundtrack.jpg',
                    title='Mad Max: Fury Road',
                    text='瘋狂麥斯：憤怒道(反烏托邦題材！)',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Mad Max: Fury Road'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        )
                    ]
                )
            ]
        )
    )
    return message

#TemplateSendMessage - ImageCarouselTemplate(圖片旋轉木馬)
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例