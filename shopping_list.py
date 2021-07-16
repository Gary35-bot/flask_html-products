from flask import *

app = Flask(__name__)


@app.route('/')
def pick_items():
    return render_template('Wallmart.html')


@app.route('/product_table', methods=['POST', 'GET'])
def table():
    if request.method == 'POST':
        result = request.form
        return render_template('item_table.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
