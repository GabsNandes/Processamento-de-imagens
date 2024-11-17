# -*- coding: utf-8 -*-


import cv2 
from utils.generalutils import *
from utils.colorutils import negative_color, combine_bgr


nomeimagem = select_imagem()    
    
imagem = cv2.imread(nomeimagem)


print("lenght: ")

print(imagem.shape[1])

print("height: ")
print(imagem.shape[0])


print("Channels: ")
print(imagem.shape[2])
        
gray, blue, green, red = split_colors(imagem)

target_size = (200, 200)

neg_blue = negative_color(blue, 0)
neg_grenn = negative_color(green, 1)
neg_red = negative_color(red, 2)


new_img = combine_bgr(imagem, neg_blue, neg_grenn, neg_red)
cv2.imshow("Combined", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




cv2.imwrite("out.jpg", imagem)