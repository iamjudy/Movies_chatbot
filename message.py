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
                    label='Drama 劇情',
                    text='Drama 劇情'
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


def Carousel_Template_Animation():
    message = TemplateSendMessage(
        alt_text='Animation 動畫類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://inmywordz.com/wp-content/uploads/20171128223023_58.png',
                    title='Spirited Away',
                    text='一個警惕我們不要貪吃的故事。',
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
                    text='Bing Bong, Bing Bong!',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Inside Out'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://box8in.files.wordpress.com/2017/12/ratatouillle.jpg',
                    title='Ratatouille',
                    text='原來這部電影英文叫：普羅旺斯雜燴。',
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

def Carousel_Template_Romance():
    message = TemplateSendMessage(
        alt_text='Romance 浪漫類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://variety.com/wp-content/uploads/2016/05/me-before-you-2.jpg',
                    title='Me Before You',
                    text='權力遊戲的女主角演得歐～',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Me Before You'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i0.wp.com/char-lifestyle.com/wp-content/uploads/2020/08/begin-again-movie-poster-2.jpg',
                    title='Begin Again',
                    text='誒，這不是亞當李維嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Begin Again'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://hookedonhouses.net/wp-content/uploads/2009/01/The-Holiday-DVD-cover.jpg',
                    title='The Holiday',
                    text='戀愛沒有假期的 The Holiday。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='The Holiday'
                        )
                    ]
                )
            ]
        )
    )
    return message


def Carousel_Template_fiction():
    message = TemplateSendMessage(
        alt_text='Science fiction 科幻類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://images-na.ssl-images-amazon.com/images/S/pv-target-images/c79cb951b771c38dcfb784da35cb617649f0a7699e20842b119c2e7eace7d47e._RI_V_TTW_.jpg',
                    title='Men in Black II',
                    text='人類大戰外星生物！',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Men in Black II'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://image.presslogic.com/holiday.presslogic.com/wp-content/uploads/2018/08/Inception-8.jpg',
                    title='Inception',
                    text='夢中夢中夢中夢中夢中夢中夢？',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Inception'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.overthinkingit.com/wp-content/uploads/2010/01/Avatar-Sucks.jpg',
                    title='Avatar',
                    text='藍藍的你我他。',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='Avatar'
                        )
                    ]
                )
            ]
        )
    )
    return message


def Carousel_Template_Drama():
    message = TemplateSendMessage(
        alt_text='Drama 劇情類推薦',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.traveltaormina.com/images/escursioni/the-godfather-tour-from-taormina.jpg',
                    title='The Godfather',
                    text='經典黑社會幫派電影！',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='The Godfather'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://media.gq.com.tw/photos/5e4fa1d239abfa00087ac65d/16:9/w_1920,c_limit/FotoJet%20-%202020-02-21T172243.555.jpg',
                    title='The Shawshank Redemption',
                    text='IMDb第一名，我看了至少三遍 ><',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='The Shawshank Redemption'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://www.winwallpapers.net/w1/2015/02/The-Imitation-Game-Wallpapers-10.jpg',
                    title='The Imitation Game',
                    text='他不是 Sherlock，他是Turing！',
                    actions=[
                        MessageTemplateAction(
                            label='推薦類似這部ㄉ',
                            text='The Imitation Game'
                        )
                    ]
                )
            ]
        )
    )
    return message