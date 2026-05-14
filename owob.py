from flask import Flask, redirect

app = Flask(__name__)

images = [
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449532388311090/Not_sure_where_this_is_from_but_I_find_it_calming_and_pleasing_to_look_at___.gif",

    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449533466251294/Gif_aesthetic_anime.gif",

    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449534036541521/posted_by_ernoticon_on_Tumblr.gif",

    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449534896640060/download.gif",

    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449532975648859/09b902d11b569df1225ad2e8a91572e3_gif_500279.gif"
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
