import pytesseract
from pytesseract import Output
from PIL import Image
import cv2
from PyTable import PyTable, ImageClarify
import csv


TESSERACT_PATH = "F:\\Tesseract\\tesseract.exe"
IMG_PATH = "test4.JPG"

#def delete_savages(line: str) -> str:
#    return line.replace("|", "")

#def clear_lines(lines: list) -> list:
#    return [delete_savages(item) for item in lines if item != ""]


#pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

#text = pytesseract.image_to_string(img_path, lang="eng")
#print(text.split("\n"))
#lines = text.split("\n")
#print(clear_lines(lines))


if __name__ == "__main__":
    image = cv2.imread(IMG_PATH)
    normalized = ImageClarify.normalize(image)
    deskewed = ImageClarify.deskew(normalized)
    cv2.imshow("test", image)
    cv2.imshow("result", normalized)
    cv2.imshow("desk", deskewed)
    if cv2.waitKey(0) == ord('q'):
        pass
    
    engine = PyTable(TESSERACT_PATH)
    res = engine.convert_image(IMG_PATH)
    print(res)
    cols = ["StudentID", "Name", "English", "Math", "Physics", "History", "Art"]

    with open("test.csv", "w") as f:
        writer = csv.writer(f)

        writer.writerow(cols)
        writer.writerows(res[1:])


#   TODO:
# - normalization
# - skew correction
# - img scaling
# - noise removal
# - thinning and skeletonization
# - grayscale
# - thresholding and binarization