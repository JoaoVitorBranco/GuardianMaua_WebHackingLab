from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

with open("4_vulnerabilidades2/ex0_rce/output/output.txt", "w") as f:
 f.write("") 

comments = []

@app.route('/')
def index():
    return render_template('index.html', comments=comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['comment']
    os.system(f'echo "{comment}" >> 4_vulnerabilidades2/ex0_rce/output/output.txt')
    try:
      with open("4_vulnerabilidades2/ex0_rce/output/output.txt", "r") as f:
        lines = f.readlines()
        return jsonify({'success': True, 'comment': lines[len(lines)-1]})
    except Exception as err:
      return jsonify({'error': 'Error ao ler arquivo'})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
