from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# http://plugins.krajee.com/file-input
@app.route('/upload', methods=['GET'])
def upload_show_view():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_process_data():
    # send if all done
    return '{}'
    # send if error
    #return '{"error":"Test error response!"}'


if __name__ == '__main__':
    app.run(debug=True)
