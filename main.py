import requests
from flask import Flask, render_template

# --------- Global Vars
BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

# --------- Create Flask App
app = Flask(__name__)

# --------- Fetch Blogs
response = requests.get(BLOG_URL)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=all_posts)


@app.route('/post/<blog_id>')
def blog_post(blog_id):
    return render_template("post.html", blog=all_posts[int(blog_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)
