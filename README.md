# photos_script

**Windows:**
1. Скачать https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.5.0.20241111.exe
2. Установить (отметить Russian language data)
3. Добавить в PATH: `C:\Program Files\Tesseract-OCR`

**Linux:** `apt-get install tesseract-ocr tesseract-ocr-rus`

```
pip install -r requirements.txt
python recognize.py <folder>
```