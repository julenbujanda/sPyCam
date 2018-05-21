from guizero import App, Text, Picture, PushButton
from twython import Twython
from autenticacion import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

def tweetear():
    #message = Text(app, "Text")
    twitter.update_status(status='Nuevo Tweet 2')



app = App("The All Seeing Pi", 800, 480)
new_pic = PushButton(app, tweetear, text="Nuevo Tweet")
app.display()
