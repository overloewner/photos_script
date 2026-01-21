import pytesseract
from PIL import Image
import sys
from pathlib import Path
import platform

if platform.system() == 'Windows':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

folder = Path(sys.argv[1])

with open('output.txt', 'w', encoding='utf-8') as f:
    for img in sorted(folder.glob('*')):
        if img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
            text = pytesseract.image_to_string(Image.open(img), lang='rus+eng')
            f.write(text.strip() + '\n')
            f.write('_____________________________________________________\nНовый слайд\n')
