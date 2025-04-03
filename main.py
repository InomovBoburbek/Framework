from wsgiref.simple_server import make_server
from app import Frameworkapp

app = Frameworkapp()

@app.route("/home")
def home(request, response):
    response.text = "Home pagedan uyquli salom!"

@app.route("/about")
def about(request, response):
    response.text = "Abdulazizga salm!"

@app.route("/muhammadyusuf")
def muhammadyusuf(request, response):
    response.text = "yoshi: 16, yili: 2008"

from flask import Flask, send_file, abort

app = Flask(__name__)


@app.route("/abdulloh")
def abdulloh():
    try:
        image_path = r"C:\Users\user\Desktop\Abdulloh2.jpg"
        img_tag = f'<img src="/abdulloh/image" alt="Abdulloh rasmi" width="300"><br>'

        info = """
        <h2>Arslonov Abdulloh</h2>
        <p>Yoshi: 17 da<br>
        Hobbisi: Aylanish<br>
        Asosiy vazifasi: Dars qilish<br>
        Burji: Tog' echkisi<br>
        Bo'yi: 185 sm<br>
        Yozgan kitobi: Kuchli hislar kuchli qarashlar</p>
        """
        return img_tag + info
    except Exception:
        abort(500)


@app.route("/abdulloh/image")
def abdulloh_image():
    try:
        image_path = r"C:\Users\user\Desktop\Abdulloh2.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
