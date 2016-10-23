from app import db


class Upload(db.Model):
    # __tablename__  = 'upload'

    id = db.Column(db.Integer, primary_key=True)
    # MD5 sum
    access_key = db.Column(db.String(32), nullable=False)
    # File
    file_name = db.Column(db.String(255), nullable=False)
    # Access
    date_upload = db.Column(db.DateTime, nullable=False)
    last_download = db.Column(db.DateTime)

    def __init__(self, access_key=None, file_name='Unknown', date_upload=None, last_download=None):
        self.access_key = access_key
        self.file_name = file_name
        self.date_upload = date_upload
        self.last_download = last_download

    def __str__(self):
        return "File info: { accec_key: %d, file_name: %s, data_upload: %s }" % (
            self.access_key, self.file_name, self.date_upload)
