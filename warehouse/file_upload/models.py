class Upload:

    def __init__(self, id=0, access_key='0', file_name='', title='', text='', file_route='', data_upload='', data_download='',):
        self.id = id
        self.accec_key = access_key
        self.file_name = file_name
        self.title = title
        self.text = text
        self.file_route = file_route
        self.data_upload = data_upload
        self.data_download = data_download

    def __str__(self):
        return "File info: { accec_key: %d, file_name: %s, title: %s, data_upload: %s }" % (self.accec_key, self.file_name, self.title, self.data_upload)
