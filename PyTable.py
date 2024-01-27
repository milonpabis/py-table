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
        img = self.__prepare_image(img_path)
        try:
            res = self.__clear_lines(pytesseract.image_to_string(img, lang=language).split("\n"))
        except Exception:
            print("DEBUG!")
        return res
    

    def __prepare_image(self, img, th=190):
        image = cv2.imread(img)
        # - normalization

        # - skew correction

        # - img scaling

        # - noise removal

        # - thinning and skeletonization

        # - grayscale

        # - thresholding and binarization

        return image
    


    
    def __delete_savages(self, line: str) -> str:
        return line.replace("|", "")

    def __clear_lines(self, lines: list) -> list:
        return [self.__delete_savages(item).split() for item in lines if item != ""]
    


class ImageClarify:

    def normalize(img):
        h, w, _ = img.shape
        filter = np.zeros((w, h))
        return cv2.normalize(img, filter, 0, 255, cv2.NORM_MINMAX)
    
    def deskew(img):
        #
        ...
    
    def set_image_dpi(img):
        #
        ...
        