import pytesseract
from PIL import Image
import sys
from pathlib import Path
import platform

if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

folder = Path(sys.argv[1])

for img in sorted(folder.glob('*')):
    if img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
        text = pytesseract.image_to_string(Image.open(img), lang='rus+eng')
        print(text.strip())
        print()
