from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/linux', methods=['GET'])
def linux():
    # context = {
    #         'items': '12345',
    #         'name': 'Tinchoram',
    #     }
    #return render_template('linux.html', **context)
    return render_template('linux.html')

@app.route('/notes', methods=['GET'])
def notes():
    return render_template('notes.html')

@app.route('/blog', methods=['GET'])
def blog():
    return redirect('notes')

@app.route('/', methods=['GET'])
def index():
    return redirect('notes')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)