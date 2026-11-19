import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # FIX: query parametrizada. O '?' é substituído seguramente
    # pelo driver sqlite3, sem interpretação do conteúdo de
    # usuario/senha como parte do comando SQL.
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"

    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado."
