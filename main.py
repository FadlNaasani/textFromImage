# This is a sample Python script.
import cv2
import easyocr
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

img = cv2.imread('bilde.png')

reader= easyocr.Reader(['en'], gpu=False) # bedre om du har gpu og raaskere
result= reader.readtext(img)  # matrise av ordene
##print (result)              # kan besteme hva vi skal hente fra matrisen


for text in result:
    p1=text[0][0]
    p2=text[0][2]
    detectedText=text[1]
    print(p1,p2)
    cv2.rectangle(img,p1,p2, (0,255,0), 3 )
    cv2.putText(img,detectedText, p1,cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0))
    
cv2.imshow('Image', img)
cv2.waitKey(0)

