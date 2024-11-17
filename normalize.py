# -*- coding: utf-8 -*-


import cv2 
from utils.generalutils import *
from utils.grayutils import normalized_gray, generate_normalized_img
from utils.graphutils import calcHists, compareplotGrayOnly, plotGrayOnly


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


# Plotting the histograms separately

base, data, _, _, _ = calcHists(gray, blue, green, red, imagem)

normalized_hist = normalized_gray(gray, data)

compareplotGrayOnly(base, data, normalized_hist)
normalized_img, accumulated = generate_normalized_img(gray, normalized_hist)

plotGrayOnly(base, accumulated)


target_size = (400, 400)  # Adjust this size as needed

# Resize each image to the target size
grayN_resized = cv2.resize(normalized_img, target_size)
gray_resized = cv2.resize(gray, target_size)

# Stack images horizontally in pairs and then vertically to form a single image
top_row = cv2.hconcat([gray_resized, grayN_resized])
combined_image = cv2.vconcat([top_row])

# Display the combined image
cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


base, data_norm, _, _, _ = calcHists(normalized_img, blue, green, red, imagem)
compareplotGrayOnly(base, data, data_norm)



cv2.imwrite("out.jpg", imagem)
