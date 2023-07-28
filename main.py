from flask import Flask, render_template

app = Flask(__name__)

#criar a primeira página = first route
@app.route("/")
def index():
    return render_template("index.html")

#rodar aplicativo
app.run()