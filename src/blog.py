from flask import Flask, render_template, redirect
import unittest

app = Flask(__name__)


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/linux', methods=['GET'])
def linux():
    # context = {
    #         'items': '12345',
    #         'name': 'Tinchoram',
    #     }
    # return render_template('linux.html', **context)
    return render_template('linux.html')


@app.route('/python', methods=['GET'])
def note_python():
    return render_template('python.html')


@app.route('/docker', methods=['GET'])
def note_docker():
    return render_template('docker.html')

@app.route('/kubernetes', methods=['GET'])
def note_kubernetes():
    return render_template('kubernetes.html')


@app.route('/go', methods=['GET'])
def note_go():
    return render_template('go.html')


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
    app.run(host="0.0.0.0", port=5000, debug=False)
