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


hash_user = "1532e76dbe9d43d0dea98c331ca5ae8a65c5e8e8b99d3e2a42ae989356f6242a"
hash_pass = "274298cfc022bbf4da968f84f1f6519e4787ca7430c74265af3ec8328091c4ba"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', message='')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['nome']
    password = request.form['senha']
    if encrypt_sha256(username) != hash_user:
        return render_template('login.html', message='Invalid username.')
    
    if encrypt_sha256(username) == hash_user and encrypt_sha256(password) != hash_pass:
        return render_template('login.html', message='Invalid password for this username.')
    
    else:
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return "Parabéns! Você concluiu o último exercício 💻😁"
 
if __name__ == '__main__':
    app.run(debug=True)
