from flask import Flask, send_file
import requests
import itertools
from io import BytesIO

app = Flask(__name__)

images = itertools.cycle([
    "https://files.catbox.moe/c0asdk.gif",
    "https://files.catbox.moe/85wmoy.gif",
    "https://files.catbox.moe/348isi.gif",
    "https://files.catbox.moe/looo1r.gif",
    "https://files.catbox.moe/ac041w.gif",
    "https://files.catbox.moe/ux1syg.gif"
])

@app.route("/")
def rotate():
    url = next(images)

    response = requests.get(url)

    return send_file(
        BytesIO(response.content),
        mimetype="image/gif"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
