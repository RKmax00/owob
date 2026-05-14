from flask import Flask, redirect

app = Flask(__name__)

images = [
    "https://files.catbox.moe/c0asdk.gif",
    "https://files.catbox.moe/85wmoy.gif",
    "https://files.catbox.moe/348isi.gif",
    "https://files.catbox.moe/looo1r.gif",
    "https://files.catbox.moe/ac041w.gif",
    "https://files.catbox.moe/ux1syg.gif"
]

counter = 0

@app.route("/")
def rotate():
    global counter

    url = images[counter]

    counter = (counter + 1) % len(images)

    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
