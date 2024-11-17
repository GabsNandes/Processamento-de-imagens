# -*- coding: utf-8 -*-


import cv2 
from utils.generalutils import *
from utils.graphutils import calcHists, plothists


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)

target_size = (200, 200)  # Adjust this size as needed

# Resize each image to the target size
imagem_resized = cv2.resize(imagem, target_size)
blue_resized = cv2.resize(blue, target_size)
green_resized = cv2.resize(green, target_size)
red_resized = cv2.resize(red, target_size)
gray_resized = cv2.resize(gray, target_size)

# Stack images horizontally in pairs and then vertically to form a single image
top_row = cv2.hconcat([imagem_resized, blue_resized])
bottom_row = cv2.hconcat([green_resized, red_resized])
combined_image = cv2.vconcat([top_row, bottom_row])

# Display the combined image
cv2.imshow("Combined Image", combined_image)
cv2.imshow("gray", gray_resized)



# Plotting the histograms separately

base, data, blue_hist, green_hist, red_hist = calcHists(gray, blue, green, red, imagem)

# Original dataset (grey)
plothists(base, blue_hist, green_hist, red_hist, data)



cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("out.jpg", imagem)

