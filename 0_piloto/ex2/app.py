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

hash_user = "00e3fa7ad96d08bd0705322ca2a30874de09aedb096c2e7fb449282131bba1e7"
hash_pass = "ad4941386c090ac54142d38b390d313075deff4d873a1c82e3a25540cf611127"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', message='')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['user']
    password = request.form['pass']
    if encrypt_sha256(username) == hash_user and encrypt_sha256(password) == hash_pass:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message='Invalid username or password.')

@app.route('/dashboard')
def dashboard():
    return "Parabéns! Você concluiu o exercício 2 😁"

if __name__ == '__main__':
    app.run(debug=True)
