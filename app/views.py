import datetime
import hashlib
import os

from flask import request, render_template
from flask import send_file
from werkzeug.utils import secure_filename

from app import db
from app.models import Upload
from main import application


@application.route('/')
def index():
    return render_template('index.html', context={})


@application.route('/search', methods=['GET'])
def search_view():
    q = request.args['q']

    found = Upload.query.filter(Upload.file_name.like('%' + q + '%')).all()

    return render_template('search.html', context={
        'found': found
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


@application.route('/download/<string:key>', methods=['GET'])
def download_action(key):
    download_file = Upload.query.filter(Upload.access_key == key).first()

    return send_file(os.path.join(application.config.get('STORE_PATH'), download_file.access_key),
                     attachment_filename=download_file.file_name, as_attachment=True)
