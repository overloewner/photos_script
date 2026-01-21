import easyocr
import sys
from pathlib import Path

reader = easyocr.Reader(['ru', 'en'], gpu=False)
folder = Path(sys.argv[1])

with open('output.txt', 'w', encoding='utf-8') as f:
    for img in sorted(folder.glob('*')):
        if img.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
            result = reader.readtext(str(img), detail=0, paragraph=True)
            f.write('\n'.join(result) + '\n')
            f.write('_____________________________________________________\nНовый слайд\n')
