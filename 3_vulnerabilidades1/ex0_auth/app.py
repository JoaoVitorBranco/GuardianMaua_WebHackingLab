from flask import Flask, render_template, request, redirect, url_for
import hashlib

def encrypt_sha256(text):
    # Cria um objeto de hash SHA-256
    sha256_hash = hashlib.sha256()

    # Atualiza o objeto de hash com a string fornecida
    sha256_hash.update(text.encode('utf-8'))

    # Retorna a representação hexadecimal do hash
    encrypted_text = sha256_hash.hexdigest()

    return encrypted_text

cookie = "7e1d832cf135a97fd7bee2b10a8dac7e7c0d370c97142b7d5d63b34e504b0e21"


app = Flask(__name__)

def go_to_admin():
    return render_template('admin.html', message='')

@app.route('/')
def index():
    return render_template('index.html', message='')

@app.route('/admin', strict_slashes=True)
def admin():
    if encrypt_sha256(request.cookies.get('session', "cookie")) == cookie:
        return go_to_admin()
    return "Acesso negado"

@app.route('/<path:path>', strict_slashes=True)
def any_other_route(path):
    print(request.base_url)
    path = '/'.join(request.base_url.split('/')[3:]).lower() # ex: in http://google.com/images, path = images
    
    if path.lower() == 'admin':
        return go_to_admin()
    else:
        return 'Página não encontrada'

if __name__ == '__main__':
    app.run(debug=True)