from flask import Flask, render_template, request, redirect, url_for
from banco import conectar

app = Flask(__name__)

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    conn = conectar()

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        curso = request.form["curso"]

        conn.execute("""
            UPDATE alunos
            SET nome = ?,
                email = ?,
                curso = ?
            WHERE id = ?
        """, (nome, email, curso, id))
        
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    aluno = conn.execute("""
        SELECT *
        FROM alunos
        WHERE id = ?
    """, (id)).fetchone()

    conn.close()

    return render_template(
        "editar.html",
        aluno=aluno
    )

@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):

    conn = conectar()

    conn.execute("""
        DELETE FROM alunos
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)