from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("1ex1index.html")

@app.route("/aluno/<nome>")
def aluno(nome):
    return render_template("1ex1aluno.html", nome=nome)

@app.route("/aluno")
@app.route("/aluno/<nome>")
def exibir_nome(nome="Visitante"):
    return render_template("1ex1aluno.html", nome=nome)

@app.route("/curso/<curso>")
def curso(curso):
    return render_template("1ex1curso.html", curso=curso)

@app.route("/curso")
@app.route("/curso/<curso>")
def exibir_curso(curso="Não informado"):
    return render_template("1ex1curso.html", curso=curso)

@app.route("/aluno/<nome>/<curso>")
def aluno_curso(nome, curso):
    return render_template("1ex1include.html", nome=nome, curso=curso)

if __name__ == "__main__":
    app.run(debug=True)
