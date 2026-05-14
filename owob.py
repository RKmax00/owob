from flask import Flask, redirect

app = Flask(__name__)

images = [
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449531834794115/beyond_the_other_side.gif?ex=6a07074f&is=6a05b5cf&hm=a0e27646053a4271b04cebbbae40cab94d81cc724234c96c5b180f6eab7cc571&",

    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449532388311090/Not_sure_where_this_is_from_but_I_find_it_calming_and_pleasing_to_look_at___.gif?ex=6a07074f&is=6a05b5cf&hm=0b35a1d1000167f7051d249cc60ad2c30c2ca0189cd4bf54a222c4af0f4a4176&",

    "https://media.discordapp.net/attachments/1469338751296733378/1504449532975648859/09b902d11b569df1225ad2e8a91572e3_gif_500279.gif?ex=6a07074f&is=6a05b5cf&hm=e9b8532eaa813e3ea5a00e9f0719327bf685ded9ca92aadd94e51bb526af0682&=&width=625&height=349",

    "https://media.discordapp.net/attachments/1469338751296733378/1504449533466251294/Gif_aesthetic_anime.gif?ex=6a070750&is=6a05b5d0&hm=0d7a5b8b4bfa7c21a456f621d1d4592ccf30b5367d6b6322d42ab4b8b7f16ae2&=&width=675&height=380",

    "https://media.discordapp.net/attachments/1469338751296733378/1504449534036541521/posted_by_ernoticon_on_Tumblr.gif?ex=6a070750&is=6a05b5d0&hm=f2fa37a9f3fc7a4be76203d93d5d68b29c70e00e9004f7f5495ff8255ff43269&=&width=625&height=345",

    "https://media.discordapp.net/attachments/1469338751296733378/1504449534896640060/download.gif?ex=6a070750&is=6a05b5d0&hm=ed5e12987e0917f3dc29dee61359405e2bc47da8a9575e7f8b7b7957fb704dbd&=&width=625&height=465"
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
