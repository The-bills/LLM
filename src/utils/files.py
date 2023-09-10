def is_pdf(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}