from flask import Flask
from flask import render_template
from flask import request
import recommend

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    user = request.args.get('user')
    dic = recommend.recommend(user)
    return render_template('search.html',Data=dic)

if __name__ == '__main__':
    app.run(debug=True)
