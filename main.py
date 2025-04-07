from wsgiref.simple_server import make_server
from app import Frameworkapp

app = Frameworkapp()

@app.route("/home")
def home(request, response):
    response.text = "Home pagedan uyquli salom!"

@app.route("/about")
def about(request, response):
    response.text = "Abdulazizga salm!"

from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h2>Sleepy greetings from the home page!</h2>"

@app.route("/about")
def about():
    return "<h2>Greetings to Abdulaziz!</h2>"

@app.route("/astro")
def astro():
    img_tag2 = '<img src="/static/astro.jpg" alt="astro rasmi" width="300"><br>'
    info2 = """
        <h2>G'aybullayev Muhammadyusuf</h2>
        <p>Yoshi: 17 da<br>
        Qiziqish: Video o'yinlar<br>
        Hobby: Kod yozish va o'rganish<br>
        Yoqtirgan kasbim: Dasturchilik<br>
        Height: 185 cm<br>
        His book: Strong Feelings, Strong Views</p>
        """
    return img_tag2 + info2

@app.route("/astro/image")
def astro_image():
    try:
        image_path2 = r"C:\Users\user\Desktop\astro.jpg"
        return send_file(image_path2, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

@app.route("/abdulloh")
def abdulloh():
    img_tag = '<img src="/static/Abdulloh2.jpg" alt="Abdulloh rasmi" width="300"><br>'
    info = """
        <h2>Arslonov Abdulloh</h2>
        <p>Yoshi: 17 da<br>
        Hobby: Cycling<br>
        Main task: Teaching<br>
        Zodiac sign: Mountain Goat<br>
        Height: 185 cm<br>
        His book: Strong Feelings, Strong Views</p>
        """
    return img_tag + info

@app.route("/abdulloh/image")
def abdulloh_image():
    try:
        image_path = r"C:\Users\user\Desktop\Abdulloh2.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
