from guizero import App, Text, Picture, PushButton
from twython import Twython
from picamera import PiCamera
from overlay_functions import *
from time import gmtime, strftime

from autenticacion import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
camera = PiCamera()
camera.resolution(800, 480)
camera.hflip = True
camera.start_preview(alpha=128)
output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())

def sacar_foto():
    camera.capture(output)
    camera.stop_preview()

def tweetear():
    # message = Text(app, "Text")
    twitter.update_status(status='Iván cállate ya')

def next_overlay():
    global overlay
    overlay = next(all_overlays)
    preview_overlay(camera, overlay)



app = App("The All Seeing Pi", 800, 480)
new_pic = PushButton(app, tweetear, text="Nuevo Tweet")
app.display()
