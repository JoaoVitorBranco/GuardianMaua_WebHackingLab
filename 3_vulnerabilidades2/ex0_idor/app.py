# app.py

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Nota
class Nota:
    def __init__(self, id, titulo, conteudo, autor: str = "myself"):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor = autor
        
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "conteudo": self.conteudo,
            "autor": self.autor
        }

# Lista de notas (simulada)
notas = [
    Nota(0, "hacked.txt", "Parabéns, você concluiu o exercício de IDOR 🚪!", "admin"),
    Nota(1, "todo.txt", "CTF do THM chamado BoilerCTF, Continuar a IC e Ir na academia", "caiogomes"),
    Nota(2, "Tarefa hacker", "Tente acessar uma nota do perfil do administrador"),
]

@app.route('/')
def index():
    return render_template('index.html', notas=[nota.to_dict() for nota in notas])

@app.route('/nota/<int:nota_id>')
def ver_nota(nota_id):
    nota = next((nota for nota in notas if nota.id == nota_id), None)
    if nota:
        return render_template('nota.html', nota=nota.to_dict())
    return 'Nota não encontrada', 404

@app.route('/criar_nota', methods=['GET', 'POST'])
def criar_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        nova_nota = Nota(len(notas), titulo, conteudo)
        notas.append(nova_nota)
        return redirect(url_for('index'))
    return render_template('criar_nota.html')

if __name__ == '__main__':
    app.run(debug=True)
