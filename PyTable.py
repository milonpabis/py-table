import pytesseract
from pytesseract import Output
import csv
import cv2
import numpy as np

class PyTable:

    def __init__(self, tesseract_dir):
        self.engine_dir = tesseract_dir
        pytesseract.pytesseract.tesseract_cmd = self.engine_dir


    def convert_image(self, img_path, output="result.csv", language="eng", readNames=0):
        img = self.__prepare_image(img_path)
        try:
            res = self.__clear_lines(pytesseract.image_to_string(img, lang=language).split("\n"))
        except Exception:
            print("ERROR while reading!")
        print(res)
        try:
            with open(output, "w") as f:
                writer = csv.writer(f)
                if readNames == 0:
                    writer.writerows(res)
                else:
                    if readNames == 1:
                        cols = [input(f"COLUMN_{_}: ") for _ in range(len(res[1]))]
                    elif readNames == 2:
                        cols = [f"col{i}" for i in range(len(res[1]))]
                    writer.writerow(cols)
                    writer.writerows(res[1:])
        except Exception:
            print("ERROR while writing!")
        

    def __prepare_image(self, img):
        image = cv2.imread(img)
        image = ImageClarify.gray_scale(image)
        image = ImageClarify.contrast(image, 1.01)
        image = ImageClarify.adjust_gamma(image, 1.01)
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
    
    def resize(img, x=1.0):
        width = img.shape[1] * x
        height = img.shape[0] * x
        dim = (width, height)
        return cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)

    def gray_scale(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def athreshold(img, neigh=11, c=2):
        return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neigh, c)
    
    def biblur(img):
        return cv2.bilateralFilter(img, 9, 75, 75)
    
    def contrast(img, a=1):
        beta = 0
        return cv2.convertScaleAbs(img, alpha=a, beta=beta)
    
    def adjust_gamma(image, gamma=1.0):
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                        for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)
        