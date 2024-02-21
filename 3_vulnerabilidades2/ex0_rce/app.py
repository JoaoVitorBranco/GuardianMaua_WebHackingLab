from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    # Receives the command from the HTML form
    command = request.form['command']

    # Execute the command
    try:
      os.system(command + " > " + path + "/output/output.txt")
    except:
      return jsonify({'error': 'Command execution failed'})
  
    # Read the output from the file
    with open(path+'/output/output.txt', 'r') as file:
        output_content = file.read()

    return jsonify({'output': output_content})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
