import json
from app import Frameworkapp

app = Frameworkapp()


def load_user():
    with open("user.json", "r") as file:
        return json.load(file)


def load_bobur():
    with open("bobur.json", "r") as file:
        data = json.load(file)
    return data


def save_bobur(data):
    with open("bobur.json", "w") as file:
        json.dump(data, file, indent=4)


@app.route("/home")
def home(request, response):
    data = load_bobur()
    data["bobur"] += 1
    save_bobur(data)
    response.text = f"Home pagedan uyquli salom! - {data['bobur']}"


@app.route("/about")
def about(request, response):
    data = load_bobur()
    data["bobur2"] += 1
    save_bobur(data)
    response.text = f"About paged salom! - {data['bobur2']}"


@app.route("/u/<id>")
def get_info(request, response, id):
    users = load_user()
    user = users.get(id, "Bunday user yo‘q!")

    data = load_bobur()
    if id not in data:
        data[id] = 0
    data[id] += 1
    save_bobur(data)

    response.text = json.dumps(user)


@app.route("/admin/<admin_id>")
def get_admin(request, response, admin_id):
    users = load_user()
    user = users.get(admin_id, "Bunday user yo‘q!")

    data = load_bobur()
    key = f"admin_{admin_id}"
    if key not in data:
        data[key] = 0
    data[key] += 1
    save_bobur(data)

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
        response.content_type = "image/jpeg"
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
        response.content_type = "image/jpeg"
    except FileNotFoundError:
        response.status = 404
        response.text = "Rasm topilmadi."
