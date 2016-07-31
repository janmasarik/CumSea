from flask import Flask, render_template, request, redirect
from cum_sea import CumSea

app = Flask(__name__)


@app.route('/hello',methods=['GET'])
def hello_world():
    return 'Hello World.'


@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.tpl')


@app.route('/search', methods=['GET', 'POST'])
def cum_search():
    query = request.form.get('query')
    if not query:
        return redirect('/')
    c = CumSea(query)
    results = c.cum_search()
    print results
    return render_template('cum_search.tpl', results=results)


if __name__ == "__main__":
    app.run(port=13370, debug=True)