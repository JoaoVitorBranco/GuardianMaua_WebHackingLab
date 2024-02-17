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

hash_user = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
hash_pass = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', message='')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if encrypt_sha256(username) == hash_user and encrypt_sha256(password) == hash_pass:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', message='Invalid username or password.')

@app.route('/dashboard')
def dashboard():
    return "Parabéns! Você concluiu o exercício 0 😁"

if __name__ == '__main__':
    app.run(debug=True)
