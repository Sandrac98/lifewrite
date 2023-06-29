import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_journals")
def get_journals():
    try:
        journals = mongo.db.journals.find()
        return render_template("journals.html", journals=journals)
    except Exception as e:
        return f"Error connecting to MongoDB: {str(e)}"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in the db
        username = request.form.get("username", "")
        if not username:
            flash("Please provide a username")
            return redirect(url_for("register"))

        existing_user = mongo.db.users.find_one({"username": username.lower()})
        if existing_user:
            flash("Oops, that username is not available")
            return redirect(url_for("register"))

        register = {
            "username": username.lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }

        mongo.db.users.insert_one(register)

        # creates cookie session for new user
        session["user"] = username.lower()
        flash("Welcome to LifeWrite!")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve the username and password from the form
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        # Check if username and password are provided
        if not username or not password:
            flash("Please provide a username and password")
            return redirect(url_for("login"))

        # Retrieve the user from the database based on the username
        existing_user = mongo.db.users.find_one({"username": username.lower()})

        # Check if the user exists and if the password is correct
        if existing_user and check_password_hash(existing_user["password"], password):  # noqa
            # creates cookie session for the user
            session["user"] = username.lower()
            flash("Welcome back, {}!".format(username))
            return redirect(url_for("home"))
        else:
            flash("Oops invalid username or password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
