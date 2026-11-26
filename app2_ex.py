from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    nome=None
    email=None
    idade=None
    curso=None

    if request.method=="POST":
        nome=request.form.get("nome")
        email=request.form.get("email")
        idade=request.form.get("idade")
        curso=request.form.get("curso")

    return render_template("2ex_form.html", nome=nome, email=email, idade=idade, curso=curso)

if __name__ == "__main__":
    app.run(debug=True)