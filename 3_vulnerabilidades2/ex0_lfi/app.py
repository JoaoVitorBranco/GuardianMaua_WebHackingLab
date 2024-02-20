from flask import Flask, render_template, send_from_directory, redirect, url_for, request
import os


app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__)) + '\\livros'

@app.route('/')
def index():
    livros = os.listdir(path)
    return render_template('index.html', livros=livros)

@app.route('/livros')
def ler_livro():
    livro = request.args.get('livro')
    if livro:
        return send_from_directory('livros', livro)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
