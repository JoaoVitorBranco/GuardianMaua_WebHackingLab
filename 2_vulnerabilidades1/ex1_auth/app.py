from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reset_password.html')

@app.route('/reset_senha', methods=['POST'])
def reset_senha():
    data = request.json
    email = data.get('email')
    username = data.get('username')

    if email == "hacker@security.com":
        return "Parabéns, você completou o exercício 1 😎"
    return f'email: {email} & username: {username}'

@app.route('/senha_resetada')
def senha_resetada():
    output = request.args.get('output', '')  # Obter o output da query parameter
    if output == "Parabéns, você completou o exercício 1 😎":
        return output
    return f'Senha resetada para {output}'

if __name__ == '__main__':
    app.run(debug=True)
