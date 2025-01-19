import os
import io
import zipfile
from flask import Flask, request, send_file, jsonify
from flask_restful import Resource, Api, reqparse
from werkzeug.utils import secure_filename
import tempfile
from docx import Document


UPLOAD_FOLDER = 'uploads'
TEMP_FOLDER = 'temp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

class FileUploadResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('file', type=reqparse.FileStorage, location='files', required=True, help='No file provided')
        super(FileUploadResource, self).__init__()

    def post(self):
        args = self.parser.parse_args()
        file = args['file']

        if file:
            original_filename = file.filename
            print(f"Original filename: {original_filename}")  # Debugging line
            filename=original_filename
            if not filename:
                return {'message': 'Invalid filename'}, 400

            file_path = os.path.join(UPLOAD_FOLDER, filename)
            temp_file_path = os.path.join(TEMP_FOLDER, filename)

            # Save the uploaded file to the upload folder
            file.save(file_path)
            print(f"Saved to upload folder: {file_path}")  # Debugging line

            # Save the uploaded file to the temp folder
            with open(temp_file_path, 'wb') as temp_file:
                file.seek(0)  # Ensure the file pointer is at the beginning
                temp_file.write(file.read())
            print(f"Saved to temp folder: {temp_file_path}")  # Debugging line

            # Read text content from the file
            text_content = self.read_text_from_file(temp_file_path, os.path.splitext(filename)[1])

            # Compress the text content
            compressed_data = self.compress_text(text_content)

            # Return the compressed data
            return send_file(
                io.BytesIO(compressed_data),
                mimetype='application/zip',
                as_attachment=True,
                download_name=f'{os.path.splitext(filename)[0]}.zip'
            )
        else:
            return {'message': 'No file provided'}, 400

    def read_text_from_file(self, file_path, file_extension):
        if file_extension == '.docx':
            return self.read_docx(file_path)
        elif file_extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as txt_file:
                return txt_file.read()
        else:
            return 'Unsupported file type'

    def read_docx(self, file_path):
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)

    def compress_text(self, text_content):
        # Create an in-memory byte stream
        byte_stream = io.BytesIO()
        with zipfile.ZipFile(byte_stream, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('content.txt', text_content)
        return byte_stream.getvalue()
