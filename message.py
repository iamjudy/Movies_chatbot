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

def Carousel_Template_Action():
    message = TemplateSendMessage(
        alt_text='Action 動作類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://2.bp.blogspot.com/-dV1ZUcm5s24/WUb-pLm0A7I/AAAAAAAAP00/yR4Tu87gesEPqn1Ud3VgedgbcLIwXRKeACLcBGAs/s1600/Sfdhgkhyjuop3.jpg',
                    title='Spider-Man 3',
                    text='我說的是 2007版本，沒有 Tom Holland。',
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
                    text='瘋狂麥斯：憤怒道（ 反烏托邦題材！)',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Mad Max: Fury Road'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://ethan55.com/wp-content/uploads/86a6b2d8da6417803bf2f1a89e957f78.jpg',
                    title='Skyfall',
                    text='主題曲是 Adele 唱的，James Bond!',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Skyfall'
                        )
                    ]
                )
            ]
        )
    )
    return message


def Carousel_Template_Horror():
    message = TemplateSendMessage(
        alt_text='Horror 恐怖類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://d32qys9a6wm9no.cloudfront.net/images/movies/backdrop/56/5e7a21c11d8d291a88fef7731939218e_706x397.jpg?t=1576182172',
                    title='The Witch',
                    text='《后翼棄兵》女主演的，黑暗又抑鬱。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='The Witch'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.shopify.com/s/files/1/1416/8662/products/aliens_1986-french-original_film_art_1200x.jpg?v=1615492948',
                    title='Aliens',
                    text='1986年的美國科幻恐怖片，導演是James Cameron！',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Aliens'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://keithandthemovies.files.wordpress.com/2013/01/mama-poster.jpg',
                    title='Mama',
                    text='台灣翻《母侵》，大陸翻《媽媽》ㄛ',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Mama'
                        )
                    ]
                )
            ]
        )
    )
    return message


def Carousel_Template_Horror():
    message = TemplateSendMessage(
        alt_text='Animation 動畫類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.slashfilm.com/wp/wp-content/images/spirited-away-3-e1614356820324.jpg',
                    title='Spirited Away',
                    text='神隱少女，一部警惕我們不要貪吃的故事。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Spirited Away'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.newmobilelife.com/wp-content/uploads/2015/08/InsideOut556500e6a2be0-2040.0.jpg',
                    title='Inside Out',
                    text='Who is the best in every way, and wants to sing this song to say Bing Bong, Bing Bong!',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Inside Out'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://gonewiththetwins.com/new/wp-content/uploads/2016/06/ratatouille.jpg',
                    title='Ratatouille',
                    text='其實這部電影叫：普羅旺斯雜燴。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Ratatouille'
                        )
                    ]
                )
            ]
        )
    )
    return message