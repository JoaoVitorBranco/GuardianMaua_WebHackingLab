import hashlib
from flask import Flask, render_template, request, session, make_response
import base64

def encrypt_sha256(text):
    # Cria um objeto de hash SHA-256
    sha256_hash = hashlib.sha256()

    # Atualiza o objeto de hash com a string fornecida
    sha256_hash.update(text.encode('utf-8'))

    # Retorna a representação hexadecimal do hash
    encrypted_text = sha256_hash.hexdigest()

    return encrypted_text

def encrypt_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def decrypt_base64(text):
    return base64.b64decode(text.encode('utf-8')).decode('utf-8')

hash_user = "YWRtaW4="
hash_pass = "7e1d832cf135a97fd7bee2b10a8dac7e7c0d370c97142b7d5d63b34e504b0e21"

session = {
    'db': {
        hash_user: hash_pass
    }
}

app = Flask(__name__)

# Rota para a página de login
@app.route('/')
def index():
    return "Faça seu login em /login"

# Rota para a página de criação de conta
@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Criar usuário
        username_encrypted = encrypt_base64(request.form['username'])
        print(username_encrypted)
        print(session['db'])
        if session['db'].get(username_encrypted, None) != None:
            print("salve")
            return render_template('create_account.html', message='Username already exists.')
        session['db'][username_encrypted] = encrypt_sha256(request.form['password'])
        
        response = make_response(render_template("index.html"))
        response.set_cookie("session", encrypt_base64(request.form['username']))
        
        
        # Redirecionar para a página de login
        return response
    return render_template('create_account.html', message="")

# Rota para o processamento do login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if session['db'].get(encrypt_base64(request.form['username'])) != None:
            if session['db'][encrypt_base64(request.form['username'])] == encrypt_sha256(request.form['password']):
                return f"Login com sucesso na conta {request.form['username']}"
            else:
                return render_template('index.html', message='Invalid username or password.')
        else:
             return render_template('index.html', message='Invalid username or password.')
         
    elif request.method == "GET":
        if request.cookies.get("session", "") == hash_user:
            return "Parabéns, você completou o exercício 2 😎"
        elif request.cookies.get("session", "") in session['db'].keys():
            return f"Login com sucesso na conta {decrypt_base64(request.cookies.get('session', ''))}"
        return render_template('index.html', message="")
        
    return "Login successful"


if __name__ == '__main__':
    app.run(debug=True)
