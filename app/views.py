import datetime
import hashlib
import os

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
    return render_template('upload.html')


@application.route('/upload', methods=['POST'])
def upload_process_data():
    # Get uploaded file
    f = request.files['data']
    filename = secure_filename(f.filename)

    # Hashing file data
    md5 = hashlib.md5()
    md5.update(f.read())
    checksum = md5.hexdigest()

    # Save uploaded file
    store_file = os.path.join(application.config.get('STORE_PATH'), checksum)
    f.seek(0)
    f.save(store_file)

    # Save record for file
    uploadFile = Upload(access_key=checksum, file_name=filename, date_upload=datetime.datetime.now())
    db.session.add(uploadFile)
    db.session.commit()

    # send if all done
    return '{}'
    # send if error
    # return '{"error":"Test error response!"}'
