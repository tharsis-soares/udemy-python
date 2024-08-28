from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
    data = response.json()
    print(data)
    return render_template('index.html', json_data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)