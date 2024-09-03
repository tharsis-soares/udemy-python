# from flask import Flask, render_template, request
# import smtplib
# import requests

# app = Flask(__name__)

# # USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
# OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
# OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

# @app.route('/')
# def get_all_posts():
#     return render_template("index.html", all_posts=posts)


# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         send_email(data["name"], data["email"], data["phone"], data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)

# def send_email(name, email, phone, message):
#     email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(OWN_EMAIL, OWN_PASSWORD)
#         connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

# @app.route("/post/<int:index>")
# def show_post(index):
#     requested_post = None
#     for blog_post in posts:
#         if blog_post["id"] == index:
#             requested_post = blog_post
#     return render_template("post.html", post=requested_post)


# if __name__ == "__main__":
#     app.run(debug=True)





from flask_mail import Mail, Message 
from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can safely access the environment variables
mail_username = os.environ.get('OWN_EMAIL')
mail_password = os.environ.get('OWN_PASSWORD')


# posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()



app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = mail_username  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = mail_password     # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def home():
    response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
    data = response.json()
    print(data)
    return render_template('index.html', json_data=data)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        # print(data["name"])
        # print(data["email"])
        # print(data["phone"])
        # print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    msg = Message(
        subject='Hello from the other side!', 
        sender=mail_username,  # Ensure this matches MAIL_USERNAME
        recipients=['tharsissoares@hotmail.com']  # Replace with actual recipient's email
    )
    msg.body = "Hey, sending you this email from my Flask app, let me know if it works."
    mail.send(msg)
    return "Message sent!"
    
    # email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(OWN_EMAIL, OWN_PASSWORD)
    #     connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

# @app.route("/contact", methods=['POST', 'GET'])
# def contact():
#     messageInfo = False
#     if request.method == "POST":
#         name = request.form.get('name')
#         phone = request.form.get("phone")
#         message = request.form.get("message")
#         print(f"Name: {name}\nPhone: {phone}\nMessage: {message}")
#         success_message = "Successfully sent your message."
#         messageInfo = True
#     elif request.method == "GET" and request.args:
#         messageInfo = True
#     return render_template('contact.html', success=messageInfo)

# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == 'GET':
#         return render_template("contact.html", form_submitted=False)
#     info = request.form
#     print(info["name"])
#     print(info["email"])
#     print(info["phone"])
#     print(info["message"])
#     form_submitted = True
#     return render_template('contact.html', form_submitted=form_submitted)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

