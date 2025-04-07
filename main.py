import json
from wsgiref.simple_server import make_server
from app import Frameworkapp

app = Frameworkapp()

def load_user():
    with open("user.json", "r") as file:
        user = json.load(file)

    return user

@app.route("/Boburbek")
def boburbek(request, response):
    response.text = "yoshi: 17, yili: 2008"


@app.route("/home")
def home():
    text = "<h2>Hi you are in the home page!</h2>"
    return text


@app.route("/about")
def about():
    text2 = "<h2>This page is localhost page for waitress theme!</h2>"
    return text2


@app.route("/u/id")
def get_info(request, response, id):
    users = load_user()
    user = users.get(id, "Bunday user yoq!")

    response.text = json.dumps(user)


@app.route("/")
def index():
    return """
    <h1>Asosiy Sahifa</h1>
    <ul style="font-size: 20px;">
        <li><a href="/home">🏠 Home</a></li>
        <li><a href="/about">ℹ️ About</a></li>
        <li><a href="/muhammadyusuf">👤 astro</a></li>
        <li><a href="/abdulloh">👤 abdulloh</a></li>
        <li><a href="/u/123">🆔 Foydalanuvchi ID (misol: 123)</a></li>
    </ul>
    """

"""
    "/home" : home,
    "/about" : about,
    "/u/bobur" : user,  
    "/u/abdulloh" : user
"""


@app.route("/muhammadyusuf")
def astro():
    img_tag = '<img src="/muhammadyusuf/image" alt="Muhammad Yusuf rasmi" width="300"><br>'

    info = """
        <h2>G'aybullayev Muhammad Yusuf</h2>
        <p>Yoshi: 17 da<br>
        Qiziqish: Video o'yinlar<br>
        Hobby: Kod yozish va o'rganish<br>
        Yoqtirgan kasbim: Dasturchilik<br>
        Height: 185 cm<br>
        His book: Strong Feelings, Strong Views</p>
        """
    return img_tag + info

@app.route("/muhammadyusuf/image")
def astro_image():
    try:
        image_path = r"C:\Users\user\Desktop\muhammadyusuf2.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

@app.route("/abdulloh")
def abu():
    img_tag2 = '<img src="/abdulloh/image" alt="Abdulloh rasmi" width="300"><br>'

    info2 = """
        <h2>Arslonov Abdulloh</h2>
        <p>Yoshi: 17 da<br>
        Hobby: Cycling<br>
        Main task: Teaching<br>
        Zodiac sign: Mountain Goat<br>
        Height: 185 cm<br>
        His book: Strong Feelings, Strong Views</p>
        """
    return img_tag2 + info2


@app.route("/abdulloh/image")
def abu_image():
    try:
        image_path = r"C:\Users\user\Desktop\Abdulloh2.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
