# -*- coding: utf-8 -*-


import cv2 
from utils import *


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = grayFunction(imagem)

f1, f2, f3 = contraste(imagem, gray)
negimg = negativo(imagem, gray)
parbol = parboltone(imagem, gray)


target_size = (200, 200)  # Adjust this size as needed

# Resize each image to the target size

f1_resized = cv2.resize(f1, target_size)
f2_resized = cv2.resize(f2, target_size)
f3_resized = cv2.resize(f3, target_size)
neg_resized = cv2.resize(negimg, target_size)
gray_resized = cv2.resize(gray, target_size)
parbol_resized = cv2.resize(parbol, target_size) 

# Stack images horizontally in pairs and then vertically to form a single image
top_row = cv2.hconcat([gray_resized, f1_resized])
middle_row = cv2.hconcat([f2_resized, f3_resized])
bottom_row = cv2.hconcat([parbol_resized, neg_resized])
combined_image = cv2.vconcat([top_row, middle_row, bottom_row])


# Display the combined image
cv2.imshow("Combined Image", combined_image)


plot(f1,f2,f3,gray,negimg,parbol)


cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)

