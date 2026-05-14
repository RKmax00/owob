from flask import Flask, redirect
import time
import random

app = Flask(__name__)

images = [
    "https://static.wikia.nocookie.net/owobot/images/4/42/Great_Sword.png/revision/latest?cb=20191128112429",
    "https://static.wikia.nocookie.net/owobot/images/7/77/Defender%27s_Aegis.png/revision/latest?cb=20191128112427"
]

@app.route("/")
def rotate():

    current = int(time.time() // 14) % len(images)

    unique = random.randint(100000, 999999)

    return redirect(
        f"{images[current]}&dynamic={unique}",
        code=302
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
