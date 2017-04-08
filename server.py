from sense_hat import SenseHat
from flask import Flask

app = Flask(__name__)
sense = SenseHat()

@app.route("/left")
def turn_on():
    sense.show_message("Left")
    return "Turning on!"

@app.route("/right")
def turn_off():
    sense.show_message("Right")
    return "Turning off!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
