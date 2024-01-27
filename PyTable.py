import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
import numpy as np

class PyTable:

    def __init__(self, tesseract_dir):
        self.engine_dir = tesseract_dir
        pytesseract.pytesseract.tesseract_cmd = self.engine_dir





    def convert_image(self, img_path, language="eng"):
        
        try:
            res = self.__clear_lines(pytesseract.image_to_string(img_path, lang=language).split("\n"))
        except Exception:
            print("DEBUG!")
        return res
    

    def __prepare_image(self, img, th=190):
        image = Image.open(img)
        image = image.convert('L')
        image = image.point(lambda p: 255 if p > th else 0)
        return image

    
    def __delete_savages(self, line: str) -> str:
        return line.replace("|", "")

    def __clear_lines(self, lines: list) -> list:
        return [self.__delete_savages(item).split() for item in lines if item != ""]
        