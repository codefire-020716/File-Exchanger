#!./venv/bin/python
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'skjdjdjdajasdkasdl1231jdsjdsc'
app.config['path'] = 'C:/Users/user/Uploadtest/'


@app.route('/')
def index():
    return render_template('index.html')


# http://plugins.krajee.com/file-input
@app.route('/upload', methods=['GET'])
def upload_show_view():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_process_data():
    f = request.files['data']
    f.save(app.config['path'] + secure_filename(f.filename))
    # send if all done
    return '{}'
    # send if error
    #return '{"error":"Test error response!"}'


if __name__ == '__main__':
    app.run(debug=True)
