import datetime
from flask import request, render_template
from werkzeug.utils import secure_filename

from app import db
from app.models import Upload
from main import application


@application.route('/')
def index():
    return render_template('index.html', context={
        'store': application.config.get('STORE_PATH')
    })


# http://plugins.krajee.com/file-input
@application.route('/upload', methods=['GET'])
def upload_show_view():
    uploadFile = Upload(access_key='d41d8cd98f00b204e9800998ecf8427e', date_upload=datetime.datetime.now())

    # db.session.add(uploadFile)
    # db.session.commit()

    return render_template('upload.html')


@application.route('/upload', methods=['POST'])
def upload_process_data():
    f = request.files['data']

    f.save(application.config.get('path', '~/Downloads/') + secure_filename(f.filename))
    # send if all done
    return '{}'
    # send if error
    # return '{"error":"Test error response!"}'
