from flask import Flask, Response
import requests
import itertools

app = Flask(__name__)

images = itertools.cycle([
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449534896640060/download.gif",
    
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449534036541521/posted_by_ernoticon_on_Tumblr.gif",
    
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449533466251294/Gif_aesthetic_anime.gif",
    
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449532975648859/09b902d11b569df1225ad2e8a91572e3_gif_500279.gif",
    
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449532388311090/Not_sure_where_this_is_from_but_I_find_it_calming_and_pleasing_to_look_at___.gif",
    
    "https://cdn.discordapp.com/attachments/1469338751296733378/1504449531834794115/beyond_the_other_side.gif"
])

@app.route("/")
def rotate_image():
    url = next(images)

    r = requests.get(url)

    return Response(
        r.content,
        content_type=r.headers["Content-Type"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
