from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    response = requests.get(f'http://localhost:5001/search/{keyword}')
    data = response.json()
    return render_template('search_results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

