import os

from dotenv import load_dotenv


load_dotenv()

IAM_TOKEN = os.getenv("IAM_TOKEN")

FOLDER_ID = os.getenv("FOLDER_ID")

OCR_URL = "https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText"

YA_OCR_AVAILABLE_EXT = {
    'png': 'PNG',
    'jpg': 'JPEG',
    'jpeg': 'JPEG',
}
