from flask import Flask, redirect

app = Flask(__name__)

# Image 1
@app.route("/")
def image1():
    return redirect(
        "https://static.wikia.nocookie.net/owobot/images/4/42/Great_Sword.png/revision/latest?cb=20191128112429",
        code=302
    )

# Image 2
@app.route("/a")
def image2():
    return redirect(
        "https://static.wikia.nocookie.net/owobot/images/7/77/Defender%27s_Aegis.png/revision/latest?cb=20191128112427",
        code=302
    )

# GIF 1
@app.route("/b")
def image3():
    return redirect(
        "https://media.discordapp.net/attachments/1469338751296733378/1504449534896640060/download.gif?ex=6a070750&is=6a05b5d0&hm=ed5e12987e0917f3dc29dee61359405e2bc47da8a9575e7f8b7b7957fb704dbd&=&width=625&height=465",
        code=302
    )

# GIF 2
@app.route("/c")
def image4():
    return redirect(
        "https://media.discordapp.net/attachments/1469338751296733378/1504449534036541521/posted_by_ernoticon_on_Tumblr.gif?ex=6a070750&is=6a05b5d0&hm=f2fa37a9f3fc7a4be76203d93d5d68b29c70e00e9004f7f5495ff8255ff43269&=&width=625&height=345",
        code=302
    )

# GIF 3
@app.route("/d")
def image5():
    return redirect(
        "https://media.discordapp.net/attachments/1469338751296733378/1504449533466251294/Gif_aesthetic_anime.gif?ex=6a070750&is=6a05b5d0&hm=0d7a5b8b4bfa7c21a456f621d1d4592ccf30b5367d6b6322d42ab4b8b7f16ae2&=&width=675&height=380",
        code=302
    )

# GIF 4
@app.route("/e")
def image6():
    return redirect(
        "https://media.discordapp.net/attachments/1469338751296733378/1504449532975648859/09b902d11b569df1225ad2e8a91572e3_gif_500279.gif?ex=6a07074f&is=6a05b5cf&hm=e9b8532eaa813e3ea5a00e9f0719327bf685ded9ca92aadd94e51bb526af0682&=&width=625&height=349",
        code=302
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
