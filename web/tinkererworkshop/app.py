from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random

app = Flask(__name__)

title = "SKYSEC CTF 2023 - Kurabiye Dükkanı"
words = ["emission", "alliance", "offense", "scientist", "series", "counter", "depression", "emotion", "call",
         "correspondent", "salmon", "acceptance", "step", "pc", "leather", "ritual", "awareness", "cause", "hook",
         "breath", "wife", "ethics", "library", "cell", "excitement", "competitor", "text", "beat", "figure", "fighter",
         "relation", "critic", "revolution", "alarm", "opponent", "criticism", "humanity", "portion", "assessment",
         "tree", "background", "square", "anxiety", "teaspoon", "rating", "historian", "heights", "discrimination",
         "fiber", "officer"]

app.secret_key = random.choice(words)


@app.route("/")
def main():
    if session.get("owner"):
        check = session["owner"]
        if check == "blank":
            return render_template("index.html", title=title)
        else:
            return redirect("/display")
    else:
        session["owner"] = "blank"
        return redirect("/")


@app.route("/idenify", methods=["GET", "POST"])
def idenify():
    if "name" in request.form and request.form["name"] in words:
        session["owner"] = request.form["name"]
        return redirect("/display")
    else:
        session["owner"] = "blank"
        return redirect("/")


@app.route("/reset")
def reset():
    session.pop("owner", None)
    return redirect("/")


@app.route("/workshop", methods=["GET"])
def workshop():
    if session.get("owner"):
        check = session["owner"]
        if check == "tinkerer":
            resp = make_response(render_template("hff.html", title=title))
            return resp
        print("Almost There...")
        return render_template("no-hff.html", title=title, cookie_name=session["owner"])
    else:
        session["owner"] = "blank"
        return redirect("/")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=54236)
