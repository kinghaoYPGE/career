from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
  name_list = ['java', 'javascript', 'mysql', 'mongo']
  name_dict = {'1': 'java', '2': 'python', '3': name}
  return render_template('index.html', name=name_dict or 'Flask')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8089, debug=True)