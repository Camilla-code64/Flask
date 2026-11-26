from flask import Flask, render_template, request, redirect, url_for, flash

from aluno import Aluno
from aluno_repository import AlunoRepository

import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY")

if not app.config["SECRET_KEY"]:
    raise RuntimeError("Defina a variável de ambiente FLASK_SECRET_KEY.")

#Criamos um objeto repositório. Ele será responsável por acessar o SQLite.
repositorio = AlunoRepository()

@app.route("/", methods=["GET", "POST"])
def inicio():
    """Exibe a lista de alunos e processa o formulário de cadastro."""
    if request.method == "POST":
        #Os dados enviados pelo formulário chegam como texto.
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        curso = request.form.get("curso", "").strip()

        #Validação simples no servidor: não confie apenas no atributo required do HTML.
        if not nome or not email or not curso:
            flash("Preencha todos os campos para cadastrar o aluno.", "erro")
            return redirect(url_for("inicio"))

        #Encapsulamos os dados em um objeto da classe Aluno.
        novo_aluno = Aluno(
            id=None, #O banco gera o ID automaticamente.
            nome=nome,
            email=email,
            curso=curso,
        )

        #A rota não executa SQL. Ela delega essa responsabilidade ao repositório.
        repositorio.cadastrar(novo_aluno)
        flash("Aluno cadastrado com sucesso!", "sucesso")
        return redirect(url_for("inicio"))
    
    #Em uma requisição GET, buscamos os registros e os enviamos ao template.
    alunos = repositorio.listar()
    return render_template("index.html", alunos=alunos)

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    """Mostra o formulário de edição (GET) e salva alterações (POST)."""
    aluno = repositorio.buscar_por_id(id)

    #Se não existir registro com esse ID, respondemos com erro 404.
    if aluno is None:
        return render_template("nao_encontrado.html"), 404

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        curso = request.form.get("curso", "").strip()

        if not nome or not email or not curso:
            flash("Preencha todos os campos.", "erro")
            return render_template("editar.html", aluno=aluno)

        #Alteramos os atributos do objeto que foi recuperado do banco.
        aluno.nome = nome
        aluno.email = email
        aluno.curso = curso

        #O repositório converte as alterações em uma instrução UPDATE.
        repositorio.atualizar(aluno)
        flash("Dados do aluno atualizados com sucesso!", "sucesso")
        return redirect(url_for("inicio"))

    return render_template("editar.html", aluno=aluno)

@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    """Exclui um registro. Usamos POST porque a operação modifica os dados,"""

    excluido = repositorio.excluir(id)

    if excluido:
        flash("Aluno excluído com sucesso.", "sucesso")
    else:
        flash("O aluno não foi encontrado.", "erro")

    return redirect(url_for("inicio"))

if __name__ == "__main__":
    #debug=True facilita o desenvolvimento em sala; não use assim em produção.
    app.run(debug=True)