from flask import Flask, render_template, send_from_directory, redirect, url_for, request
import os

def path_adaptation(full_path, path_to_find):
    change_back_count = path_to_find.count('../')
    if change_back_count == 0:
        return full_path + '/' + path_to_find
    full_path = full_path.split('/')
    full_path = full_path[:-change_back_count]
    full_path = '/'.join(full_path) + '/' + path_to_find.replace("../", "")
    return full_path

app = Flask(__name__)
path = f'{os.path.dirname(os.path.abspath(__file__))}\\livros'.replace("\\", "/")

@app.route('/')
def index():
    livros = os.listdir(path)
    return render_template('index.html', livros=livros)

@app.route('/livros')
def ler_livro():
    print()
    livro = request.args.get('livro')
    if livro:
        content = ""
        try:
            path_param = livro
            with open(path_adaptation(path, path_param), 'r') as f:
                content = f.read()
            return content
        except:
            return "Book not found"

    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
