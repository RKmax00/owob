from flask import Flask, redirect
import time

app = Flask(__name__)

images = [
    "https://cdn.discordapp.com/emojis/572620163434676265.png",

    "https://cdn.discordapp.com/emojis/538196865410138125.png"
]

@app.route("/")
def rotate():

    # Change image every 14 seconds
    current = int(time.time() // 14) % len(images)

    current_image = images[current]

    # Add timestamp to help bypass cache
    separator = "&" if "?" in current_image else "?"

    return redirect(
        f"{current_image}{separator}t={int(time.time())}",
        code=302
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
