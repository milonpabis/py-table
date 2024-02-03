import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
from PyTable import PyTable, ImageClarify
import csv


TESSERACT_PATH = "F:\\Tesseract\\tesseract.exe"
IMG_PATH = "test4.JPG"


if __name__ == "__main__":
    engine = PyTable(TESSERACT_PATH)
    engine.convert_image(IMG_PATH, "mycsv1.csv", readNames=1)
