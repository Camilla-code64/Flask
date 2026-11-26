from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    nome=None
    email=None
    curso=None

    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        curso = request.form.get("curso")

        return redirect(url_for("home"))
    
    return render_template("2form_aluno.html", nome=nome, email=email, curso=curso) 

'''nome=None

    if request.method=="POST":
        nome = request.form.get("nome")
    return render_template("2form.html", nome=nome)'''

if __name__ == "__main__":
    app.run(debug=True)