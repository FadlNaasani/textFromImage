# This is a sample Python script.
import cv2
import easyocr
from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

img = cv2.imread('text.png')
img1 = np.zeros((350, 700, 3), dtype = np.uint8)

reader= easyocr.Reader(['en'], gpu=False) # bedre om du har gpu og raaskere
result= reader.readtext(img)  # matrise av ordene

#result = reader.readtext(img, detail=0, blocklist="-.:';,",
#slope_ths=0.1,ycenter_ths=0.2)
print(result)

blank_img = np.zeros(shape=(500,700,3),dtype=np.int16)

for text in result:
    p1= text[0][0]
    p2=text[0][2]
    y1= p1[1]
    y2= p2[1]
    x1=p1[0]
    x2=p2[0]
    cpx= text[0][2]
    detectedText=text[1]
    #for fordeleText in detectedText:
        # rektangel mellom elementer
    #print(p1,p2)
    #rec= cv2.rectangle(img,p1,p2, (0,255,0), 3)
    cropped= img[y1:y2, x1:x2]
    blank_img = cv2.line(blank_img, p1,p2, color=(0, 158, 255), thickness=5)
    cv2.rectangle(blank_img, p1,p2, color=(0, 158, 255), thickness=5)

    cv2.imwrite("cropped_image.jpg", cropped)



    #cv2.putText(img,detectedText, p1,cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0))



#img = cv2.imread('cropped_image.jpg')

#cv2.imshow('text', cropped)
#cv2.imshow('Image', img1)
cv2.imshow('Hei',blank_img)
cv2.imwrite('image.png', blank_img)
cv2.waitKey(0)



"""

with open("output.txt","w") as txt_file:
    for line in result:
        txt_file.write(" ".join(line) + "\n")
##print (result)              # kan besteme hva vi skal hente fra matrisen
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# open the text file in read mode
f = open("output.txt", "r")

# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output("mygfg.pdf")


"""