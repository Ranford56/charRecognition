import cv2
import numpy as np
import pytesseract
from openpyxl import Workbook
def ocr_core(img):
        text = pytesseract.image_to_string(img)
        return text
def getGreyscale(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def removeNoise(img):
        return cv2.medianBlur(img, 5)

def treshholding(img):
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def all(img):
        img = removeNoise(img)
        return img

img = all(cv2.imread('img.png'))
img2 = all(cv2.imread('img2.png'))
img3 = all(cv2.imread('img3.png'))
img4 = all(cv2.imread('img4.png'))
img5 = all(cv2.imread('img5.png'))

images = [img, img2, img3, img4, img5]
c=[]
for img in images:
        s = ocr_core(img)
        a = np.array(s.split())
        a = a.astype(np.int64)
        for mina in a:
                c.append(mina)

wb = Workbook()
ws = wb.active
i=1
for p in c:
        ws['A'+str(i)] = p
        i += 1
wb.save('quince.xlsx')