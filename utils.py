import base64

from settings import YA_OCR_AVAILABLE_EXT


def get_file_extension(file_name):
    return file_name.split('.')[-1] if '.' in file_name else None

def encode_file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        return base64.b64encode(file_data).decode('utf-8')
    except IOError as e:
        raise Exception(f"Ошибка при чтении файла: {e}")

def generate_request_headers(iam_token, folder_id):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iam_token}",
        "x-folder-id": folder_id,
        "x-data-logging-enabled": "true"
    }

def create_request_body(mime_type, base64_file_content):
    return {
        "mimeType": mime_type,
        "languageCodes": ["*"],
        "model": "page",
        "content": base64_file_content
    }

def get_mime_type_from_extension(extension):
    return YA_OCR_AVAILABLE_EXT.get(extension)