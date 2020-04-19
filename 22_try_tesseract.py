from PIL import Image
import pytesseract
file_path = "./data/test.png"
img = Image.open(file_path)
print(pytesseract.image_to_string(img))