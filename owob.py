from flask import Flask, send_file
import itertools
import os

app = Flask(__name__)

gif_cycle = itertools.cycle([
    "1.gif",
    "2.gif",
    "3.gif",
    "4.gif",
    "5.gif",
    "6.gif",
])

@app.route("/battle.gif")
def battle_gif():
    gif = next(gif_cycle)
    path = os.path.join("gifs", gif)

    return send_file(
        path,
        mimetype="image/gif",
        cache_timeout=0
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
