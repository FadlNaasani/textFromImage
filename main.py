# This is a sample Python script.
import cv2
import easyocr
from fpdf import FPDF

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

img = cv2.imread('bilde.png')

reader= easyocr.Reader(['en'], gpu=False) # bedre om du har gpu og raaskere
#result= reader.readtext(img)  # matrise av ordene
result = reader.readtext(img, detail=0, blocklist="-.:';,",
slope_ths=2.5,ycenter_ths=0.2)


with open("output.txt", "w") as txt_file:
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
for text in result:
    p1=text[0][0]
    p2=text[0][2]
    detectedText=text[1]
    #print(p1,p2)
    #cv2.rectangle(img,p1,p2, (0,255,0), 3 )
    #cv2.putText(img,detectedText, p1,cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0))
"""

#cv2.imshow('Image', img)
#cv2.waitKey(0)
