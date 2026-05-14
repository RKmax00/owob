from flask import Flask, send_from_directory
import threading
import time
import shutil

app = Flask(__name__)

gifs = [
    "static/1.gif",
    "static/2.gif",
    "static/3.gif",
    "static/4.gif"
]

current = 0

def rotate_gifs():
    global current

    while True:
        shutil.copyfile(
            gifs[current],
            "static/current.gif"
        )

        current = (current + 1) % len(gifs)

        time.sleep(14)

threading.Thread(
    target=rotate_gifs,
    daemon=True
).start()

@app.route("/")
def serve_gif():
    return send_from_directory(
        "static",
        "current.gif"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
