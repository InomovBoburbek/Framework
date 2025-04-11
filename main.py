import json
from wsgiref.simple_server import make_server
from app import Frameworkapp
import mimetypes

app = Frameworkapp()


def load_user():
    with open("user.json", "r") as file:
        return json.load(file)

def load_home():
    with open("bobur.json", "r") as file:
        data = json.load(file)

    return data
cnt = load_home()

@app.route("/home")
def home(request, response):
    global cnt
    cnt += 1
    with open
    response.content_type = "text/html"
    response.text = f"<h2>Hi you are in the home page!</h2> {cnt}"



@app.route("/about")
def about(request, response):
    response.content_type = "text/html"
    response.text = "<h2>This page is localhost page for waitress theme!</h2>"


@app.route("/u/id")
def get_info(request, response, id):
    users = load_user()
    user = users.get(id, "Bunday user yo‘q!")
    response.text = json.dumps(user)


@app.route("/admin/id")
def get_admin(request, response, admin_id):
    users = load_user()
    user = users.get(admin_id, "Bunday user yo‘q!")
    response.text = json.dumps(user)


@app.route("/muhammadyusuf")
def astro(request, response):
    response.content_type = "text/html"
    response.text = """
        <img src="/muhammadyusuf/image" width="300"><br>
        <h2>G'aybullayev Muhammad Yusuf</h2>
        <p>Yoshi: 17 da<br>
        Qiziqish: Video o'yinlar<br>
        Hobby: Kod yozish<br>
        Kasb: Dasturchi<br>
        Kitobi: Strong Feelings, Strong Views</p>
    """


@app.route("/muhammadyusuf/image")
def astro_image(request, response):
    try:
        path = r"C:\Users\user\Desktop\muhammadyusuf2.jpg"
        with open(path, "rb") as f:
            content = f.read()
        response.body = content
        response.content_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
    except FileNotFoundError:
        response.status = 404
        response.text = "Rasm topilmadi."


@app.route("/abdulloh")
def abu(request, response):
    response.content_type = "text/html"
    response.text = """
        <img src="/abdulloh/image" width="300"><br>
        <h2>Arslonov Abdulloh</h2>
        <p>Yoshi: 17 da<br>
        Hobby: Cycling<br>
        Kasb: Teacher<br>
        Kitobi: Strong Feelings, Strong Views</p>
    """


@app.route("/abdulloh/image")
def abu_image(request, response):
    try:
        path = r"C:\Users\user\Desktop\Abdulloh2.jpg"
        with open(path, "rb") as f:
            content = f.read()
        response.body = content
        response.content_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
    except FileNotFoundError:
        response.status = 404
        response.text = "Rasm topilmadi."


# Serverni ishga tushurish
if __name__ == "__main__":
    with make_server("", 8000, app) as server:
        print("Server is running at http://localhost:8000")
        server.serve_forever()
