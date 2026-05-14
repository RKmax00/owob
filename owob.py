from flask import Flask, redirect
import itertools

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
    return redirect(next(images), code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
