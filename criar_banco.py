import sqlite3 

conn = sqlite3.connect("alunos.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        curso TEXT NOT NULL
    )
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")