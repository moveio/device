from sense_hat import SenseHat
from flask import Flask
import pygame

pygame.mixer.init()
pygame.mixer.music.load("m.mp3")

bashCommand = "omxplayer -o local m.mp3"
process = None

app = Flask(__name__)
sense = SenseHat()

lightOn = False
playing = False

@app.route("/left", methods=['GET', 'POST'])
def turn_on():
    global lightOn
    if lightOn:
        sense.clear()
        lightOn = False
    else:
        sense.clear(0, 255, 0)
        lightOn = True

    return "Turning off!"

@app.route("/right", methods=['GET', 'POST'])
def turn_off():
    sense.show_message("Right")
    
    return "Turning off!"

@app.route("/top", methods=['GET', 'POST'])
def play_pause():
    global process
    global bashCommand
    global playing

    if playing:
	pygame.mixer.music.fadeout(2000)
        playing = False
    else:
	pygame.mixer.music.play()
        playing = True

    return "Playing!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
