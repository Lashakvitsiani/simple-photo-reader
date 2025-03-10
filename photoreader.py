import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    try:
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image, lang="eng+kat")
        print(extracted_text)
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


image_path = "static/photo.png"
extract_text(image_path)
