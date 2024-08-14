import requests
from settings import IAM_TOKEN, FOLDER_ID, OCR_URL
from utils import (
    get_file_extension,
    generate_request_headers,
    encode_file_to_base64,
    create_request_body,
    get_mime_type_from_extension,
)


def extract_text_from_file(file_path):

    file_extension = get_file_extension(file_path)
    if not file_extension:
        raise ValueError("Не удалось определить расширение файла.")

    mime_type = get_mime_type_from_extension(file_extension)
    if not mime_type:
        raise ValueError(f"Расширение '{file_extension}' не поддерживается.")

    headers = generate_request_headers(IAM_TOKEN, FOLDER_ID)
    file_base64 = encode_file_to_base64(file_path)
    request_body = create_request_body(mime_type, file_base64)

    response = requests.post(url=OCR_URL, headers=headers, json=request_body)
    response.raise_for_status()

    return response.json()['result']['textAnnotation']['fullText']


print(extract_text_from_file('image_with_text.png'))