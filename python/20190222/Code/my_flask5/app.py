from flask import Flask, render_template, request, jsonify
import recommend
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search')
def search():
  user_id = request.args.get('user')
  results = recommend.recommend(user_id)
  return render_template('search.html', data=results)

@app.route('/search/api', methods=['GET'])
def get_data():
  user_id = request.args.get('user')
  results = recommend.recommend(user_id)
  return jsonify(results)
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8089, debug=True)