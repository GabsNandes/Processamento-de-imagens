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

target_size = (200, 200)  # Adjust this size as needed


# Plotting the histograms separately

base, data, blue_hist, green_hist, red_hist = calcHists(gray, blue, green, red, imagem)

normalized_blue_hist = normalized_gray(gray, blue_hist)
print("Blue done!")
normalized_green_hist = normalized_gray(gray, green_hist)
print("Green done!")
normalized_red_hist = normalized_gray(gray, red_hist)
print("Red done!")

normalized_blue_img, accumulated = generate_normalized_colored_img(imagem, normalized_blue_hist,0)
print("Blue done!")

normalized_green_img, accumulated = generate_normalized_colored_img(imagem, normalized_green_hist,1)
print("Green done!")

normalized_red_img, accumulated = generate_normalized_colored_img(imagem, normalized_red_hist,2)
print("Red done!")


new_img = combine_bgr(imagem, normalized_blue_img, normalized_green_img, normalized_red_img)
cv2.imshow("Combined", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




cv2.imwrite("out.jpg", imagem)
